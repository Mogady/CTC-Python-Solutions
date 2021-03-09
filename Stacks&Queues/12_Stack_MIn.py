# Stack MIN

# first idea is to keep track if the element order in another list

class Stack:
    def __init__(self):
        self.__array = []
        self.__order = []
        self.__minimum = 0

    def push(self, val):
        self.__array.append(val)
        if not len(self.__order):
            self.__minimum = val
            self.__order.append(val)
        if val < self.__minimum:
            self.__minimum = val
            self.__order.append(val)
        return
        
    def pop(self):
        if not len(self.__array):
            print("stack is already empty")
            return
        val = self.__array.pop()
        if val == self.__minimum:
            self.__order.pop()
            if self.__order:
                self.__minimum = self.__order[-1]
            else:
                self.__minimum = None
        return 
    
    def min(self):
        if not len(self.__array):
            print("stack is already empty No Min")
        return self.__minimum

    def print_all(self):
        return self.__array

st = Stack()
st.push(4)
st.push(5)
st.push(1)
print(st.print_all())
print(st.min())
st.pop()
st.pop()
print(st.print_all())
print(st.min())
st.push(6)
st.push(7)
st.push(9)
print(st.print_all())
print(st.min())
st.push(8)
st.push(2)
st.push(3)

print(st.print_all())
print(st.min())    
st.pop()
st.pop()
print(st.print_all())
print(st.min())    
        
