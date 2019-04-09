t = int(input())
for i in range(t):
    a = input().strip()
    b = input().strip()
    if(len(a)!=len(b)):
        print('0')
    else:
        first = b[0:2]
        last = b[-2:]
        check1 = b[2:] + first
        check2 = last + b[:-2]
        if(a == check1):
            print('1')
        elif(a == check2):
            print('1')
        else:
            print('0')