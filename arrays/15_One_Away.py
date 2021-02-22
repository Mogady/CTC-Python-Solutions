# ONY AWAY

def check_similarity(string1, string2):
    diff = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diff += 1
        if diff > 1:
            return False
    return True   

def insert_remove_N(string1, string2):
    index1 = 0
    index2 = 0
    while((index1<len(string1)) and index2<len(string2)):
        if string1[index1] != string2[index2]:
            if index1 != index2:
                return False
            index1 += 1
        else:
            index1 += 1
            index2 += 1
    return True

def insert_remove_dic(string1, string2):
    d = dict()
    diff = 0
    for i in string2:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for j in string1:
        if j not in d:
            diff += 1
        else:
            d[j] -= 1
            if d[j] < -1:
                diff += 1
        if diff > 1 :
            return False
    return True
    
# O(N)
def One_N(string1, string2):
    # avoid creating extra ds for longer strings
    if abs(len(string1) - len(string2)) > 1:
        return False


    if len(string1) == len(string2):
        return check_similarity(string1, string2)

    
    if len(string1) > len(string2):
        return insert_remove_N(string1, string2)
    else:
        return insert_remove_N(string2, string1)


# O(N)
# using dictionary
def One_N_dic(string1, string2):
    # avoid creating extra ds for longer strings
    if abs(len(string1) - len(string2)) > 1:
        return False


    if len(string1) == len(string2):
        return check_similarity(string1, string2) 

    
    if len(string1) > len(string2):
        return insert_remove_dic(string1, string2)
    else:
        return insert_remove_dic(string2, string1)


print(One_N_dic("pale", "ple")) # True
print(One_N_dic("paaaa", "paa")) # False
print(One_N_dic("paaac", "paaa")) #true
print(One_N_dic("paaa", "paa")) # True
print(One_N_dic("pales", "pale")) # true
print(One_N_dic("pale", "bale")) # true
print(One_N_dic("pale", "bake")) # False
