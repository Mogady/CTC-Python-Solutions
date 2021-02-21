# Check Permutation

#O(N)
def check_per_N(string1, string2):
    if len(string1) != len(string2) or len(string1) == 0 or len(string2) == 0:
        print("Permutaion test failed due to length mismatch")
        return 0

    ds = dict()

    for i in range(len(string1)):
        if string1[i] in ds:
            ds[string1[i]] += 1
        else:
            ds[string1[i]] = 1 

    for j in range(len(string2)):
        if string2[j] not in ds:
            print("Permutaion test failed")
            return 0
        
        ds[string2[j]] -= 1
        if ds[string2[j]] < 0:
            print("Permutaion test failed")
            return 0
        
    print("Permutation test succeeded")
    return 1

check_per_N('abcd', 'dcab') # success
check_per_N('a','a') #success
check_per_N('', '') #fail
check_per_N(' ', ' ')#success
check_per_N('abd','bad       ')#fail
check_per_N('aabf', 'bbaf')#fail
check_per_N('abdf','fbac')#fail
