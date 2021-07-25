
#O(N) recursive more specifically O(shorter list)
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
    
    def Atbegining(self, node):
        node.next = self.head
        self.head = node
    
        return
    
    def Atend(self, node):
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = node
        current = node
    
        return node


def intersect(ls1, ls2, inter_node):
    if ls1.next is not None and ls2.next is not None:
        inter_node = intersect(ls1.next, ls2.next, inter_node)
    
    if ls1==ls2:
        inter_node = ls1
    
    
    return inter_node


ls1 = SLinkedList()
ls1.Atbegining(Node(5))
ls1.Atend(Node(6))
inter_node = ls1.Atend(Node(7))
common_1 = ls1.Atend(Node(8))
common_2 = ls1.Atend(Node(10))

ls2 = SLinkedList()
ls2.Atbegining(Node(2))
ls2.Atend(Node(9))
ls2.Atend(inter_node)


print(intersect(ls1.head, ls2.head, None).data)
