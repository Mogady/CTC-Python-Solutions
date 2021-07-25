# O(N)
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
    

def check_palindrome(ls):
    slow = ls
    fast = ls
    s = []
    while fast is not None and fast.next is not None:
        s.append(slow.data)
        fast = fast.next.next
        slow = slow.next
    if (fast != None):
        slow = slow.next
    while slow is not None:
        if s.pop() != slow.data:
            return False
        slow = slow.next
    return True

ls1 = SLinkedList()
ls1.Atbegining("r")
ls1.Atend("a")
ls1.Atend("a")
ls1.Atend("r")

print(check_palindrome(ls1.head))