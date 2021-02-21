#URLify

#O(N^2)
def URLify_N2(string, length):
    for i in range(length):
        if string[i] == ' ':
            # python slicing is generally copy and takes
            # N^2 or more speccifically 
            # https://stackoverflow.com/questions/45198936/time-complexity-on-string-slicing-operation-in-python-3
            # https://stackoverflow.com/questions/35180377/time-complexity-of-string-slice/35181399
            string = string[:i] + "%20" + string[i+1:]
    
    return string

# print(URLify_N2("Mr John Smith   ", 13))

#O(X) where X is len pd STRING
def URLify_X(string, length):
    tmp = []
    for i in range(0, length):
        if string[i] == ' ':
            tmp.append("%20")
        else:
            tmp.append(string[i])
    
    #O(N)
    # join is faster than + 
    # https://stackoverflow.com/questions/39312099/why-is-join-faster-than-in-python
    string = ''.join(tmp)

    
    return string

print(URLify_X("Mr John Smith   ", 13))
