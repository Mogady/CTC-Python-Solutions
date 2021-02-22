#Palindrome Permutation

#O(N)
def palin_N(string):

    if len(string)<=1:
        return True

    d = dict()
    for i in range(len(string)):
        if string[i].isalnum():
            if string[i] in d:
                d[string[i]] += 1
            else:
                d[string[i]] = 1

    # num_uniq_char*x = sum
    # num_uniq_char-1*x +1 = sum
    # O(S): S> Unique chars
    s = sum(d.values())
    if s == len(d.keys()):
        return False
    if s%len(d.keys()) == 0:
        return True
    elif (s-1)%(len(d.keys())-1) == 0:
        return True
    else:
        return False



# using string.count()
# O(N^2):
def palin_N_count(string):

    if len(string)<=1:
        return True

    values = []
    uniqu_chars = set(string)
    for i in uniqu_chars:
        if i.isalnum():
            values.append(string.count(i))

    # num_uniq_char*x = sum
    # num_uniq_char-1*x +1 = sum
    # O(S): S> Unique chars
    s = sum(values)
    if s == len(values):
        return False
    if s%len(values) == 0:
        return True
    elif (s-1)%(len(values)-1) == 0:
        return True
    else:
        return False


print(palin_N('taco cat')) #true
print(palin_N('taco catos')) # true
print(palin_N('taco')) # false
print(palin_N('t')) # true
print(palin_N('ta')) # false
print(palin_N('tat')) # true
