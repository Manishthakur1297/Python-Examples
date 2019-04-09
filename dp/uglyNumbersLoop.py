def divide(n,a):
    while(n%a==0):
        n = n//a
    return n

def isUgly(n):
    n = divide(n,2)
    n = divide(n,3)
    n = divide(n,5)
    return 1 if n==1 else 0


def getUnglyNo(num):
    count = 0
    i = 1
    while(count<num):
        if isUgly(i):
            count+=1
        i+=1
    return i-1



n = 15000
print(getUnglyNo(n))
