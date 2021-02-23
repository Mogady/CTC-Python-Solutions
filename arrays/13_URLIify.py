#URLify

#O(N^2)
def URLify_N2(string, length):
    for i in range(length):
        if string[i] == ' ':
            #O(N^2)
            string = string[:i] + "%20" + string[i+1:]
    
    return string

# print(URLify_N2("Mr John Smith   ", 13))

#O(X + M) where X is len of STRING
# M is the len of the new string
def URLify_X(string, length):
    tmp = []
    for i in range(0, length):
        if string[i] == ' ':
            tmp.append("%20")
        else:
            tmp.append(string[i])
    
    #O(N)
    string = ''.join(tmp)

    
    return string

print(URLify_X("Mr John Smith   ", 13))
