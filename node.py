# A class implementing a node.


class Node:

    def __init__(self, data, next=None):
        """
        Produces a newly constructed empty node.
        __init__: Any -> Node
        Fields: item stores any value
            next points to the next node in the list
        """
        self.data = data
        self.next = next

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.data)
