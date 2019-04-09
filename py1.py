if __name__ == '__main__':
    list1 = []
    list2 = []
    for q in range(int(input())):
        name = input()
        score = float(input())
        list1.append([])
        list1[q].append(score)
        
        list1[q].append(name)
        
    list1.sort()
    #list2.sort()
    
    
    list2 = list1[:][0]
    
    n = list2.count(list2[0])
    n1 = list2.count(list2[n])
    n2 = n+n1
    r1 = list2[n:n2]
    
    for i in range(len(r1)):
        
        e  = list1[:][0].index(list2[0])
        print(list1[e][1])
        #print(list2[i])
    
    '''
    print(list1)
    print(list2)
'''