# IS Unique

# with DS
# O(N)
def is_unique_ds(string):
    d = set()
    for i in range(0, len(string)):
        if string[i] in d:
            print("Stirng not Unique")
            return 0
        else:
            d.add(string(i))
    print("String is Unique")
    return 1
# is_unique_ds("#171")

# without DS
# O(N^2)
def is_unique_n2(string):
    for i in range(0, len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                print("String not Unique")
                return 0
    print("String is Unique")
    return 1

# is_unique_n2("#133")


# sorting then checking
# O(Nlog(N))

def is_unique_so(string):
    # O(NlogN)
    string_sorted = sorted(string)

    for i in range(0, len(string_sorted)-1):
        if string_sorted[i] == string_sorted[i+1]:
            print("String not Unique")
            return 0
    
    print("String is Unique")
    return 1

is_unique_so("123")