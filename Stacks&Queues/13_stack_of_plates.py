# Stack of Plates


# using single array
# using the advantage of python dynamic lists again
# we keep track of each stack using an index to the begning of the stack in dic
class SetOfStacks:
    def __init__(self, limit = 5):
        self.limit = limit
        self.__array = []
        # here we keep the stack number:index 
        self.__d = {}
        # mark which stack we are dealing with
        self.current = 0
        # counter to keep track of the stack limit
        self.counter = 5

    def push(self, val):
        # if limit exceeded create new stack
        if self.counter == self.limit:
            self.__d[self.current + 1] = self.limit*len(self.__d.keys())
            self.current += 1
            self.counter = 0
        # push the new element 
        self.__array.append(val)
        self.counter += 1

        return

    
    def pop(self):
        if len(self.__array):
            self.__array.pop()
            # if we poped till the current stack is empty remove it 
            # and move to the prev one
            if not self.counter:
                self.counter = self.limit
                self.__d.pop(self.current)
                self.current -= 1
            self.counter -= 1

        else:
            print("stack is already empty")
        return

    def popAt(self, stack_num):
        if not len(self.__array):
            print("stack is already empty")
            return
        
        # if we poped till stack no more exits
        # move to the prev one
        if stack_num not in self.__d.keys():
            print("there is no stack: ", stack_num, 
                "any more removing from the previous one")
            self.popAt(stack_num-1)
            return

        # if pop from the last stack then just call normal pop
        if stack_num == self.current:
            self.pop()
            return

        # if we poped from the middle stack till it is gone 
        # move the current to be the middle 
        if self.__d[self.current]-1 == len(self.__array):
            self.__d.pop(self.current, None)
            self.current -= 1
            self.counter = len(self.__array) - self.__d[self.current]


        self.__array.pop(self.__d[stack_num])
        self.counter -= 1
        return


    def print_all(self):
        print(self.__array)


st = SetOfStacks()
for i in range(0,20):
    st.push(i)
st.print_all()
for i in range(15,20):
    st.pop()
st.print_all()
for i in range(15, 25):
    st.push(i)

st.print_all()
for i in range(10,25):
    st.popAt(3)
st.print_all()

for i in range(0,4):
    st.pop()
st.print_all()


for i in range(0,5):
    st.push(i)
st.print_all()

for i in range(15,20):
    st.popAt(1)
st.print_all()