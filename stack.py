from arrays import DynamicArray
from node import Node


class Stack:
    def push(self, data):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        raise NotImplementedError


class StackDynamicArray(Stack):
    """An array-based stack implementation."""

    def __init__(self):
        '''Sets the initial state of self.'''
        self.__arr = DynamicArray()

    def push(self, data):
        '''Inserts item at top of the stack.'''
        self.__arr.append(data)

    def pop(self):
        '''
        Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack.
        '''
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self.__arr.pop()

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self.__arr[len(self.__arr) - 1]

    def clear(self):
        """Makes self become empty."""
        self.__arr = DynamicArray()

    def __len__(self):
        '''
        Returns the length of stack
        :return: int
        '''
        return len(self.__arr)

    def __str__(self):
        '''
        Returns a string description of Stack
        :return: str
        '''
        text = ""
        for i in range(len(self.__arr)):
            text += self.__arr.__getitem__(i)
        return text

    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self):
            yield self.__arr[cursor]
            cursor += 1


class StackLinkedList(Stack):
    """A link-based stack implementation."""

    def __init__(self):
        '''Sets the initial state of self.'''
        self._head = None
        self._size = 0

    def push(self, data):
        """Adds item to the top of the stack."""
        self._head = Node(data, self._head)
        self._size += 1

    def pop(self):
        """ Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        head = self._head
        self._head = head.next
        self._size -= 1
        return head.data

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self._head.data

    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._head = None

    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""

        def visitNodes(node):
            """Adds items to tempList from tail to head."""
            if not node is None:
                visitNodes(node.next)
            tempList.append(node.data)

        tempList = list()
        visitNodes(self._items)
        return iter(tempList)

    def __len__(self):
        '''Returns the length of stack
        :return: int'''
        return self._size


if __name__ == "__main__":
    st = StackDynamicArray()
    st.push("a")
    st.push("b")
    # print(str(stack_to_queue(st)))
    assert str(st) == "ab"
    assert st.pop() == "b"
    st.push("c")
    st.clear()
    assert st.isEmpty()
    assert len(st) == 0
    sk = StackLinkedList()
    sk.push("a")
    sk.push("b")
    assert sk.pop() == "b"
    sk.push("c")
    assert not sk.isEmpty()
    assert len(sk) == 2
