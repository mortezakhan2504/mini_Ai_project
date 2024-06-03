# این مثال ساده‌ای است که متغیرهای فازی مانند حضور، تکالیف و مشارکت را برای ارزیابی نمره کلاس‌های درس در نظر می‌گیرد.
# به جای تعریف دقیق توابع عضویت و قواعد فازی، 
# می‌توانید مقادیر و محدوده‌های دلخواه خود را برای هر متغیر تعریف کنید و قواعد منطقی خود را بر اساس شرایط مد نظرتان ایجاد کنید.





# تعریف متغیرهای فازی
attendance = ctrl.Antecedent(np.arange(0, 101, 1), 'attendance')
homework = ctrl.Antecedent(np.arange(0, 101, 1), 'homework')
participation = ctrl.Antecedent(np.arange(0, 101, 1), 'participation')
grade = ctrl.Consequent(np.arange(0, 101, 1), 'grade')

# تعریف توابع عضویت برای هر متغیر
attendance['low'] = fuzz.trimf(attendance.universe, [0, 0, 50])
attendance['high'] = fuzz.trimf(attendance.universe, [50, 100, 100])
# مشابه برای homework، participation و grade

# تعریف قواعد فازی
rule1 = ctrl.Rule(attendance['low'] & homework['low'] & participation['low'], grade['low'])
rule2 = ctrl.Rule(attendance['high'] | homework['high'] | participation['high'], grade['high'])
# اضافه کردن قواعد به سیستم فازی
grade_ctrl = ctrl.ControlSystem([rule1, rule2])
grade_evaluator = ctrl.ControlSystemSimulation(grade_ctrl)

# ارزیابی با ورودی‌ها
grade_evaluator.input['attendance'] = 75
grade_evaluator.input['homework'] = 60
grade_evaluator.input['participation'] = 80
grade_evaluator.compute()

# گرفتن خروجی
print(grade_evaluator.output['grade'])



