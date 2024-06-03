import random

class AntColonyOptimization:
    def __init__(self, num_ants, num_iterations, pheromone_evaporation_rate=0.5):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.pheromone_evaporation_rate = pheromone_evaporation_rate
        self.pheromones = {}  # دیکشنری برای نگهداری مقادیر فریب بر روی یال‌ها

    def initialize_pheromones(self, graph):
        for node in graph:
            self.pheromones[node] = {neighbor: 1.0 for neighbor in graph[node]}

    def update_pheromones(self, paths):
        for path in paths:
            path_length = len(path)
            for i in range(path_length - 1):
                current_node = path[i]
                next_node = path[i + 1]
                self.pheromones[current_node][next_node] += 1.0 / path_length
                self.pheromones[next_node][current_node] += 1.0 / path_length

    def select_next_node(self, current_node, candidate_nodes):
        pheromone_values = [self.pheromones[current_node][node] for node in candidate_nodes]
        total_pheromone = sum(pheromone_values)
        probabilities = [value / total_pheromone for value in pheromone_values]
        return random.choices(candidate_nodes, weights=probabilities)[0]

    def find_shortest_path(self, graph, start_node, end_node):
        self.initialize_pheromones(graph)
        best_path = []
        best_path_length = float('inf')

        for iteration in range(self.num_iterations):
            paths = []
            for ant in range(self.num_ants):
                current_node = start_node
                path = [current_node]
                while current_node != end_node:
                    candidate_nodes = [node for node in graph[current_node] if node not in path]
                    if not candidate_nodes:
                        break
                    next_node = self.select_next_node(current_node, candidate_nodes)
                    path.append(next_node)
                    current_node = next_node
                paths.append(path)
                if path[-1] == end_node and len(path) < best_path_length:
                    best_path = path
                    best_path_length = len(path)

            self.update_pheromones(paths)

        return best_path

# مثالی از استفاده از الگوریتم بهینه‌سازی مورچه برای یافتن مسیر کوتاه‌ترین بین گره‌ها در یک گراف:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

aco = AntColonyOptimization(num_ants=5, num_iterations=50)
shortest_path = aco.find_shortest_path(graph, 'A', 'D')
print("Shortest Path:", shortest_path)
