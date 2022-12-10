import networkx as nx
import matplotlib.pyplot as plt

from base_classes.pipe import Pipe
from base_classes.vertex import Vertex

# Define Network class to represent Pipe Networks as a network of edges
class Network:
    # Initialize a new Network object
    def __init__(self) -> None:
        # Create an empty set of vertices
        self.vertices = set()

        # Create an empty adjacency list
        self.adj_list = {}

    # Add a new vertex to the network
    def add_vertex(self, vertex_name):
        # Create Vertex object
        vertex = Vertex(vertex_name)
        # Add the new vertex to the set of vertices
        self.vertices.add(vertex)
        # Create an empty adjacency list for the new vertex
        self.adj_list[vertex.name] = set()

    # Add a new pipe to the network, connecting two vertices together
    def add_pipe(self, vert1, vert2, length):
        # Create a new pipe with a given length
        pipe = Pipe(length)
        # Add pipe to adjacency list
        self.adj_list[vert1].add((vert2, pipe))
        self.adj_list[vert2].add((vert1, pipe))

    # Print the network, showing the connections between the vertices
    def print_network(self):
        for vertex in self.adj_list.keys():
            print(f"vertex {vertex} : {self.adj_list[vertex]}")

    def plot_network(self):
        graph = nx.Graph()
        for vertex in self.adj_list:
            graph.add_node(vertex)

        for vertex in self.adj_list:
            for neighbor, weight in self.adj_list[vertex]:
                graph.add_edge(vertex, neighbor, weight=weight.get_length())

        nx.draw(graph, with_labels=True)
        plt.show()