#Three in one

# simply have an index for each stack , since python lists is flexible 
# i don't need to worry about allocating and shiftig 
# this can be more generalized for more than 3 stacks , so that it 
# accepts N as the number of stacks required.

class stack:
    def __init__(self):
        self.__array = []
        self.__d = {1: 0, 2:0, 3: 0}

    def push(self, stack_num, val):
        self.__array.insert(self.__d[stack_num], val)
        self.__update_dic(stack_num, +1)
        # print(self.__array[self.__d[stack_num]:self.__d.get(stack_num+1, len(self.__array))])

    
    def pop(self, stack_num):
        if self.__d[stack_num] != self.__d.get(stack_num+1, len(self.__array)):
            self.__array.pop(self.__d[stack_num])
            self.__update_dic(stack_num, -1)
            # print(self.__array[self.__d[stack_num]:self.__d.get(stack_num+1, len(self.__array))])

        else:
            print("stack is already empty")

    def __update_dic(self, current, val):
        k = current+1
        while k<=3:
            self.__d[k] = self.__d[k] + val
            k += 1

    def print_all(self):
        print(self.__array)

st = stack()
st.push(2,4)
st.push(2,5)
st.push(2,6)
st.push(3,7)
st.push(3,8)
st.push(3,9)
st.push(1,1)
st.push(1,2)
st.push(1,3)

st.pop(1)
st.pop(3)
st.pop(3)
st.pop(3)
st.pop(3)
st.print_all()


