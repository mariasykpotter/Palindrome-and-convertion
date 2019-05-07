from stack_and_queue import StackDynamicArray, QueueDynamicArray


def stack_to_queue(stack):
    '''
    Converts Stack into a Queue
    :param stack: StackDynamicArray
    :return: QueueDynamicArray
    '''
    queue = QueueDynamicArray()
    for el in stack:
        # print(el)
        queue.add(el)
    return queue


def queue_to_stack(queue):
    '''
    Converts Queue into a Stack
    :param queue: QueueDynamicArray
    :return: StackDynamicArray
    '''
    stack = StackDynamicArray()
    for el in queue:
        stack.push(el)
    return stack


if __name__ == "__main__":
    st = StackDynamicArray()
    st.push("a")
    st.push("b")
    st.push("c")
    st.push("d")
    print("stack: ", str(st))
    print("queue: ", str(stack_to_queue(st)))
    q = stack_to_queue(st)
    print("back to stack: ", str(queue_to_stack(q)))
    print("\n")
    q = QueueDynamicArray()
    q.add("z")
    q.add("i")
    q.add("p")
    print("queue: ", str(q))
    print("stack: ", str(queue_to_stack(q)))
    st_new = queue_to_stack(q)
    print("back to queue: ", str(stack_to_queue(st_new)))
