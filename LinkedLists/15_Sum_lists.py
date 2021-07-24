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
    

# def sum_lists(ls1, ls2):
#     carry = 0
#     last1 = ls1
#     last2 = ls2
#     len_l1 = 0
#     len_l2 = 0

#     res = SLinkedList()

#     while last1.next is not None:
#         last1 = last1.next
#         len_l1+=1
    
#     while last2.next is not None:
#         last2 = last2.next
#         len_l2+=1

#     if len_l1>len_l2:
#         while len_l1>len_l2:
#             zero_node = Node(0)
#             last2.next = zero_node
#             last2 = zero_node
#             len_l2+=1
#     else:
#         while len_l2>len_l1:
#             zero_node = Node(0)
#             last1.next = zero_node
#             last1 = zero_node
#             len_l1+=1
    
#     while ls1 is not None:
#         sum = ls1.data + ls2.data + carry
#         dig = sum%10
#         carry = 1 if sum>=10 else 0
#         res.Atbegining(dig)
#         ls1 = ls1.next
#         ls2 = ls2.next
    
#     res.print_all()

# follow up assuming padding is done separatly
def sum_lists(ls1, ls2, carry, res):
    if ls1.next is not None:
        res, carry = sum_lists(ls1.next, ls2.next, carry, res)
    

    sum = ls1.data + ls2.data + carry
    dig = sum%10
    carry = 1 if sum>=10 else 0
    res.Atbegining(dig)
    return res, carry



ls1 = SLinkedList()
ls1.Atbegining(6)
ls1.Atend(1)
ls1.Atend(7)

ls2 = SLinkedList()
ls2.Atbegining(2)
ls2.Atend(9)
ls2.Atend(5)

res = SLinkedList()

res, carry = sum_lists(ls1.head, ls2.head, 0, res)

res.print_all()
    
