def cost(l):
    
    sum = 0
    for j in range(len(l)-2):
        n1_max = l[j]
        c_max = l[j+1]
        n2_max = l[j+2]
        n1_min = 1
        n2_min = 1
        c_min = 1
        ml = []
        ml.append(abs(n1_min-c_max) + abs(c_max - n2_min))
        ml.append(abs(n1_max-c_min) + abs(c_min - n2_max))
        ml.append(abs(n1_max-c_min) + abs(c_min - n2_min))
        ml.append(abs(n1_min-c_min) + abs(c_min - n2_max))
        ml.append(abs(n1_min-c_max) + abs(c_max - n2_max))
        ml.append(abs(n1_max-c_max) + abs(c_max - n2_min))
        ml.append(abs(n1_max-c_max) + abs(c_max - n2_max))
        ml.append(abs(n1_min-c_min) + abs(c_min - n2_min))
        
        l_max = max(ml)
        print(ml)
        print(l_max)
        
        sum = sum + l_max
#    if(len(l)>3):
#        return sum-l_max
#    else:
#        return sum
    return sum
    



t = int(input())

for i in range(t):
    
    n = int(input())
    l = list(map(int,input().split()))
    result = cost(l)
    
    print(result)