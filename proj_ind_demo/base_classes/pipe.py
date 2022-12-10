# The Pipe class represents a pipe with a given length
class Pipe:
    # Initialize a new Pipe object with a given length
    def __init__(self, length) -> None:
        # TODO: Decide on default pipe length
        self.length = length

    # Return a string representation of the Pipe object
    def __str__(self) -> str:
        return '{}'.format(self.length)

    # Return a string representation of the Pipe object
    def __repr__(self) -> str:
        return '{}'.format(self.length)

    def get_length(self):
        return self.length