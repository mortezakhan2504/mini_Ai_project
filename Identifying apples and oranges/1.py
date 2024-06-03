import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

# تصاویر مورد استفاده و ویژگی‌های مربوط به سیب و پرتقال را بارگذاری کنید
# X: تصاویر، Y: برچسب‌های مربوط به هر تصویر (برای مثال، سیب = 0، پرتقال = 1)

# ایجاد یک مدل شبکه عصبی
model = Sequential()

# لایه‌های کانولوشن و پولینگ برای استخراج ویژگی‌ها
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(image_width, image_height, num_channels)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# تبدیل ویژگی‌های استخراج شده به بردار
model.add(Flatten())

# لایه‌های کاملا متصل برای طبقه‌بندی
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # یک خروجی برای تشخیص سیب یا پرتقال

# کامپایل مدل با تعیین تابع هزینه و بهینه‌ساز
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# آموزش مدل با داده‌های آموزشی
model.fit(X_train, Y_train, epochs=10, batch_size=32, validation_data=(X_val, Y_val))
