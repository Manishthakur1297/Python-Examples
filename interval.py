for i in range(int(input())):
    ml = []
    nl = []
    for j in range(int(input())):
        l = list(map(int,input().split(' ')))
        ml.append(l)
    nl = sorted(ml)
    print(nl)
    x = len(nl)-1
    j = 0
    while j<=x-1:
        ll1 = []
        if(nl[j][1]>nl[j+1][0]):
            if(nl[j][1]<nl[j+1][1]):
                ll1.append(nl[j][0])
                ll1.append(nl[j+1][1])
                j = -1
            else:
                ll1.append(nl[j][0])
                ll1.append(nl[j][1])
                j = -1
        nl.insert(j+2,ll1)
        del nl[j]
        del nl[j]
        x = len(nl)-1
        j = j+1
    print(nl)
            
    
    