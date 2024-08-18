import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from threading import Thread

# Sample graph for demonstration
def create_sample_graph():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 2),
        ("C", "D", 1),
        ("D", "A", 3),
        ("A", "C", 4),
        ("B", "D", 5)
    ])
    return G

class RouteOptimizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Route Optimization")

        # Initialize sample graph
        self.G = create_sample_graph()

        # Vehicle constraints
        self.vehicle_capacity = 10
        self.vehicle_max_distance = 10

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Delivery List Section
        tk.Label(self.root, text="Delivery Points (comma-separated addresses):").pack(pady=5)
        self.delivery_entry = tk.Entry(self.root, width=50)
        self.delivery_entry.pack(pady=5)

        # Vehicle Capacity
        tk.Label(self.root, text="Vehicle Capacity:").pack(pady=5)
        self.capacity_entry = tk.Entry(self.root, width=20)
        self.capacity_entry.insert(0, "10")  # Default capacity
        self.capacity_entry.pack(pady=5)

        # Max Driving Distance
        tk.Label(self.root, text="Max Driving Distance:").pack(pady=5)
        self.distance_entry = tk.Entry(self.root, width=20)
        self.distance_entry.insert(0, "10")  # Default distance
        self.distance_entry.pack(pady=5)

        # Algorithm Selection
        tk.Label(self.root, text="Select Optimization Algorithm:").pack(pady=5)
        self.algorithm_var = tk.StringVar(value="Nearest Neighbor")
        algorithms = ["Nearest Neighbor", "Dijkstra", "A*"]
        tk.OptionMenu(self.root, self.algorithm_var, *algorithms).pack(pady=5)

        # Optimize Button
        tk.Button(self.root, text="Optimize Route", command=self.optimize_route).pack(pady=5)

        # Result Area
        self.result_area = tk.Text(self.root, height=10, width=60)
        self.result_area.pack(pady=5)

    def optimize_route(self):
        # Multithreaded Optimization
        optimization_thread = Thread(target=self._optimize_route_thread)
        optimization_thread.start()

    def _optimize_route_thread(self):
        try:
            delivery_points = self.delivery_entry.get().split(',')
            delivery_points = [point.strip().upper() for point in delivery_points]
            if len(delivery_points) < 2:
                messagebox.showerror("Input Error", "At least two delivery points are required.")
                return

            self.vehicle_capacity = int(self.capacity_entry.get())
            self.vehicle_max_distance = int(self.distance_entry.get())

            algorithm = self.algorithm_var.get()
            path = self.optimize_with_algorithm(algorithm, delivery_points)
            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, f"Optimal Path: {path}\n")
            self.visualize_route(path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def optimize_with_algorithm(self, algorithm, nodes):
        if algorithm == "Nearest Neighbor":
            return self.nearest_neighbor_tsp(nodes)
        elif algorithm == "Dijkstra":
            return self.dijkstra_tsp(nodes)
        elif algorithm == "A*":
            return self.astar_tsp(nodes)
        else:
            raise ValueError("Unknown algorithm selected")

    def nearest_neighbor_tsp(self, nodes):
        start = nodes[0]
        path = [start]
        unvisited = set(nodes)
        unvisited.remove(start)

        current = start
        while unvisited:
            next_node = min(unvisited, key=lambda node: self.G[current][node]['weight'])
            path.append(next_node)
            unvisited.remove(next_node)
            current = next_node

        path.append(start)  # Return to start
        return path

    def dijkstra_tsp(self, nodes):
        # Implement Dijkstra-based TSP algorithm (simplified for demonstration)
        return self.nearest_neighbor_tsp(nodes)

    def astar_tsp(self, nodes):
        # Implement A*-based TSP algorithm (simplified for demonstration)
        return self.nearest_neighbor_tsp(nodes)

    def visualize_route(self, path):
        # Clear the previous plot
        plt.clf()

        # Draw the graph
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16)
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(self.G, pos, nodelist=path, node_color='lightgreen')
        nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("Route Visualization")
        plt.show()

def main():
    root = tk.Tk()
    app = RouteOptimizationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
