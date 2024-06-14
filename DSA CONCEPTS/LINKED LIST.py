class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node and position + 1 != index:
                position += 1
                current_node = current_node.next
            if current_node:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node and position != index:
            position += 1
            current_node = current_node.next
        if current_node:
            current_node.data = val
        else:
            print("Index not present")

    def remove_first_node(self):
        if self.head:
            self.head = self.head.next

    def remove_last_node(self):
        if self.head:
            current_node = self.head
            if not current_node.next:
                self.head = None
                return
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def remove_at_index(self, index):
        if self.head:
            current_node = self.head
            position = 0
            if position == index:
                self.remove_first_node()
            else:
                while current_node and position + 1 != index:
                    position += 1
                    current_node = current_node.next
                if current_node:
                    current_node.next = current_node.next.next
                else:
                    print("Index not present")

    def remove_node(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.remove_first_node()
            return
        while current_node and current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node and current_node.next:
            current_node.next = current_node.next.next

    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


llist = LinkedList()

llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

print("Node Data:")
llist.printLL()

print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)

print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list:", end=" ")
print(llist.sizeOfLL())
