# The Vertex class represents a pipe with a given name
class Vertex:
    # Initialize a new Vertex object with a given name
    def __init__(self, name) -> None:
        self.name = name

    # Return a string representation of the Vertex object
    def __str__(self) -> str:
        return '{}'.format(self.name)

    # Return a string representation of the Vertex object
    def __repr__(self) -> str:
        return '{}'.format(self.name)

    # Get the name of a Vertex
    def get_name(self):
        return self.name