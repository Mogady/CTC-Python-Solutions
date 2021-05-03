#O(N), using hashmaps

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
    
        return

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
    
    def remove_dups(self):
        current = self.head
        prev = None
        s = set()
        while current is not None:
            if current.data in s:
                prev.next = current.next
                del current
                current = prev.next
                continue
            s.add(current.data)
            prev = current
            current = current.next

        return


llist = SLinkedList()
llist.Atbegining(1)
llist.Atbegining(1)
llist.Atbegining(1)
llist.Atbegining(1)
llist.Atend(1)
llist.Atend(1)
llist.Atend(1)
llist.Atend(1)
llist.print_all()
llist.remove_dups()
print('after removing')
llist.print_all()

        
