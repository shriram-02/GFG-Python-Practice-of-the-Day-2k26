def setInsert(arr, n):
    #code here
    return set(arr)
def setDisplay(s):
    #code here
    for i in sorted(s):
        print(i,end=" ")
    print()

def setErase(s, x):
    #code here
    if x in s:
        s.remove(x)
        print("erased", x)
    else:
        print("not found")