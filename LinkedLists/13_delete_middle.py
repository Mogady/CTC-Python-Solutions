class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        return
    
    def Atbegining(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node
    
        return
    
    def Atend(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
        return new_node

    def remove(self, data):
        current = self.head
        if (current is not None):
            if (current.data == data):
                self.head = current.next
                current = None
                return

        while (current is not None):
            if current.data == data:
                break
            prev = current
            current = current.next

        if (current == None):
            return

        prev.next = current.next

        current = None

        return 
    
    def remove_node(self, n: Node):
        if n is None or n.next is None:
            return False
        temp = n.next
        n.data = temp.data
        n.next = temp.next
        del temp
        return True

llist = SLinkedList()
llist.Atbegining(4)
llist.Atbegining(3)
llist.Atbegining(2)
llist.Atbegining(1)
llist.Atend(5)
llist.Atend(6)
node = llist.Atend(7)
llist.Atend(8)
llist.remove_node(node)
llist.print_all()