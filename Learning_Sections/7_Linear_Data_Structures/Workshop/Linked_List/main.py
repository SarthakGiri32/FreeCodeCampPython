class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next
        self.length -= 1

    def __str__(self):
        linked_list_str = ""
        current_node = self.head
        i = 1
        while current_node is not None:
            linked_list_str += f"{i}. {current_node.element}\n"
            current_node = current_node.next
            i += 1
        return linked_list_str.rstrip("\n")


def main():
    my_list = LinkedList()
    print(f"my_list.is_empty(): {my_list.is_empty()}")

    print("\nAdding elements...")
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    print(f"my_list.is_empty(): {my_list.is_empty()}")
    print(f"my_list.length: {my_list.length}")
    print(f"my_list:\n{my_list}")

    print("\nRemoving one element...")
    my_list.remove(2)
    print(f"my_list.length: {my_list.length}")
    print(f"my_list:\n{my_list}")

if __name__ == "__main__":
    main()
