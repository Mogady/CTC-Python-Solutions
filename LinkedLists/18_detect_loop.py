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
    
        return new_node
    
    def Atend(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
        return new_node
    
    def detect_loop(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer  = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                break
        
        if fast_pointer is None or fast_pointer.next is None:
            return None
        
        slow_pointer = self.head
        while slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        return fast_pointer


llist = SLinkedList()
loop_node = llist.Atbegining(4)
llist.Atbegining(3)
llist.Atbegining(2)
llist.Atbegining(1)
llist.Atend(5)
llist.Atend(6)
llist.Atend(7)
last_node = llist.Atend(8)
last_node.next = loop_node
print(llist.detect_loop().data)