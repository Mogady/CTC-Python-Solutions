# Queue via stacks

# using one stack as pushin and another one for poping 
# by moving elemnets from one to another using POP()

from collections import deque

class MyQueue:
    def __init__(self):
        self.__push_stack = deque()
        self.__pop_stack = deque()

    def push(self, val):
        if not len(self.__push_stack):
            while len(self.__pop_stack):
                self.__push_stack.append(self.__pop_stack.pop())
            
        self.__push_stack.append(val)

        return
    
    def pop(self):
        if not len(self.__pop_stack):
            while len(self.__push_stack):
                self.__pop_stack.append(self.__push_stack.pop())
        
        if len(self.__pop_stack):
            val = self.__pop_stack.pop()
        else:
            print("queue is empty")
            val = None

        return val
    
    def print_all(self):
        if len(self.__push_stack):
            print(self.__push_stack)
        elif len(self.__pop_stack):
            print(self.__pop_stack)
        else:
            print("queue is empty")

queue = MyQueue()

queue.print_all()

for i in range(0,10):
    queue.push(i)

queue.print_all()

for i in range(0,5):
    queue.pop()

queue.print_all()

for i in range(0,5):
    queue.push(i)

queue.print_all()

for i in range(0,11):
    print(queue.pop())

queue.print_all()