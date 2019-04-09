for _ in range(int(input())):
    l = list(input())
    l1 = []
    if(len(set(l))==1):
        print(len(l)-1)
    else:
        last=l[0] 
        l1.append(last)
        for i in l:
            if i==last:
                continue
            else:
                last=i
                l1.append(i)
        print(len(l)-len(l1))
        