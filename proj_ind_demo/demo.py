from base_classes.network import Network

pipeline = Network()

pipeline.add_vertex(0)
pipeline.add_vertex(1)
pipeline.add_vertex(2)
pipeline.add_vertex(3)
pipeline.add_vertex('A')

pipeline.add_pipe(0, 1, 10)
pipeline.add_pipe(1, 2, 20)
pipeline.add_pipe(1, 3, 5)
pipeline.add_pipe('A', 3, 2)

pipeline.print_network()
pipeline.plot_network()
