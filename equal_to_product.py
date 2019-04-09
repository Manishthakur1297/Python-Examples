for i in range(int(input())):
    n,p = map(int,input().split(' '))
    arr = list(map(int,input().split()))
    flag = 0
    for j in range(n):
        #print(arr[j])
        if(p%arr[j]==0):
            num = int(p/arr[j])
            #print(num)
            l = arr[:j] + arr[j+1:]
            #print(l)
            count = l.count(num)
            #print(count)
            if(count>=1):
                flag = 1
                break
    if(flag==0):
        print('No')
    else:
        print('Yes')