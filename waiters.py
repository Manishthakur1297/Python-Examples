for _ in range(int(input())):
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #a_s = sorted(a)
    #b_s = sorted(b)
    q = 0
    w = 0
    l = []
    print("a = ",a)
    print("b = ",b)
    for i in range(n):
        if a[i]>=b[i] and q<x:
            l.append(a[i])
            print("l >= ",l)
            q+=1
        elif a[i]<b[i] and w<y:
            l.append(b[i])
            print("l <= ",l)
            w+=1
        else:
            if q<x:
                a_s = sorted(a[w:],reverse=True)
                print("a_s = ",a_s)
                c = 0
                while(q<x):
                    l.append(a_s[c])
                    print("l_w <= ",l)
                    c+=1
                    q+=1
                break
            elif w<y:
                b_s = sorted(b[q:],reverse=True)
                print("b_s = ",b_s)
                c = 0
                while(w<y):
                    l.append(b_s[c])
                    print("l_w >= ",l)
                    c+=1
                    w+=1
                break
        
    print("l === ",l)
    print(sum(l))
