# String Compression

# O(N)
# using set as stack
# my first dump idea
def compress_N(string):
    if len(string)<=2:
        return string

    new_string = [string[0]]
    stack = set()
    count = 1
    stack.add(string[0])
    for i in range(1, len(string)):
        if len(new_string) >= len(string):
            return string
        if string[i] in stack:
            count += 1
        else:
            stack.pop()
            stack.add(string[i])
            new_string.append(str(count))
            new_string.append(string[i])
            count = 1
    
    new_string.append(str(count))

    return ''.join(new_string)

# O(N)
# no need to stack just cheking next element similiar or not
def compress_N_better(string):
    if len(string)<=2:
        return string

    new_string = []
    count = 0
    for i in range(0, len(string)):
        if len(new_string) >= len(string):
            return string
        count += 1
        if i+1== len(string) or string[i] != string[i+1]:
            new_string.append(string[i])
            new_string.append(str(count))
            count = 0
    

    return ''.join(new_string)
    
print(compress_N_better('aabccccaaa'))
print(compress_N_better('abcaaaaab'))
print(compress_N_better('abc'))





