l = input().split()
n = int(l[0])
m = int(l[1])

dN = int((m-3)/2)
dotN = 1
for i in range(n):
    print('-' * dN,end='')
    
    #print (i,n/2)
    
    if(i<int(n/2)):
        print('.|.' * dotN,end='')
        dotN = dotN+2
    elif(i==int(n/2)):
        print('-' * int((m-6)/2),end='')
        print('WELCOME',end='')
        print('-' * int((m-6)/2),end='')
        dotN = dotN-2
    else:
        #print('WELCOME',end='')
        print('.|.' * dotN,end='')
        dotN = dotN-2
    
    print('-' * dN,end='\n')
    
    dN = int((m-(3*dotN))/2)
    #print("dN = ",dN,"dotN = ",dotN , "i = ",i)
#print (n , m)