# socrt stack
# O(N^2)
from collections import deque

class Stack:
    def __init__(self):
        self.__stack = deque()
    
    def pop(self):
        if not self.isEmpty():
            val = self.__stack.pop()
        else:
            val = None

        return val
    def peek(self):
        if not self.isEmpty():
            val = self.__stack[-1]
        else:
            val = None

        return val
    
    def isEmpty(self):
        if not len(self.__stack):
            return True
        return False

    def push(self, val):
        self.__stack.append(val)
        return

    def print_all(self):
        if not self.isEmpty():
            print(self.__stack)
        else:
            print("stack is empty")
    

def sort_stack(s):
    temp_stack = Stack()
    while not s.isEmpty():
        tmp = s.pop()
        while (not temp_stack.isEmpty() and temp_stack.peek()>tmp):
            s.push(temp_stack.pop())
        temp_stack.push(tmp)
    while not temp_stack.isEmpty():
        s.push(temp_stack.pop())
    return s

stack = Stack()

stack.push(2)
stack.push(9)
stack.push(7)
stack.push(2)
stack.push(9)
stack.push(7)
stack.print_all()
sort_stack(stack).print_all()

