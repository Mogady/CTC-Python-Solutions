#O(N)

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
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
        return
    
    # def partition(self, x):
    # using another LList 
    #     current = self.head
    #     new = SLinkedList()
    #     prev = self.head

    #     while current.next is not None:
    #         if current.data < x:
    #             prev = current
    #             current = current.next
            
    #         else:
    #             prev.next = current.next
    #             current.next = None
    #             new.Atend(current.data)
    #             current = prev.next
        
    #     current.next = new.head
    def partition(self, x):
        current = self.head
        last = self.head
        prev = self.head
        
        while last.next is not None:
            last = last.next
        flag = last
        while current != flag:
            if current.data < x:
                prev = current
                current = current.next
            
            else:
                prev.next = current.next
                current.next = None
                last.next = current
                last = last.next
                current = prev.next
        
                

llist = SLinkedList()
llist.Atbegining(3)
llist.Atend(5)
llist.Atend(8)
llist.Atend(5)
llist.Atend(10)
llist.Atend(2)
llist.Atend(1)

llist.print_all()
llist.partition(5)
print('after partition')
llist.print_all()

        
        
        
