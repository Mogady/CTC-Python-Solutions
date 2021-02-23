# String Rotation
 
#O(N-M)*O(M)
# my solution
def isSubstring(string1, string2):
    i = 0
    while i <= (len(string1) - len(string2)):
        if string1[i] == string2[0]:
            j = 1 
            k = i+1
            while j < len(string2):
                if string2[j] != string1[k]:
                    break
                j += 1
                k += 1
            if j == len(string2):
                return True
        i+=1
    return False

# book Solution
# O(N)
def rotation(string1, string2):
    if len(string1) == len(string2) and len(string1)>0:
        repeated = []
        for i in range(len(string1)):
            repeated.append(string1[i])
        for i in range(len(string1)):
            repeated.append(string1[i])
        
        return isSubstring(repeated, string2)


print(rotation('erbottlewat', 'waterbottle'))
print(isSubstring('abdcrtyffff', 'ffff'))