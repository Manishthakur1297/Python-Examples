def print_rangoli(size):
    
    dN = size*2-2
    l = 1
    for i in range(size):
        print("-" * dN,end='')
        k = 0
        for j in range(l):
            if(j<int(l/2)):
                print(chr(96+size-j),end="")
                print("-",end="")
            elif(j>int(l/2)):
                k = k+1
                print("-",end="")
                print(chr(k),end="")
                
            else:
                print(chr(96+size-j),end="")
                k = 96+size-j
        print("-" * dN,end='\n')
        dN = dN-2
        l = l+2
        
        
    dN = dN+4
    l = l-4
    for i in range(size-1,0,-1):
        print("-" * dN,end='')
        k = 0
        for j in range(l):
            if(j<int(l/2)):
                print(chr(96+size-j),end="")
                print("-",end="")
            elif(j>int(l/2)):
                k = k+1
                print("-",end="")
                print(chr(k),end="")
                
            else:
                print(chr(96+size-j),end="")
                k = 96+size-j
        print("-" * dN,end='\n')
        dN = dN+2
        l = l-2
        
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)