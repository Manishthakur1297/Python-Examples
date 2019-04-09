def binarySearch(l,elem,minn,maxx):
    #print('minn = ',minn)
    #print('max = ',maxx)
    if maxx>minn:
        mid = (minn+maxx)//2
        if elem == l[mid]:
            return mid
        else:
            if elem<l[mid]:
                #if(elem)
                minn = minn
                maxx = mid-1
                return binarySearch(l,elem,minn,maxx)
                # maxx
            else:
                minn = mid+1
                maxx = maxx
                return binarySearch(l,elem,minn,maxx)
                # maxx
    else:
        return maxx
        
#def binarySearch (arr,x, l, r):
# 
#    # Check base case
#    if r >= l:
# 
#        mid = int(l + (r - l)/2)
# 
#        # If element is present at the middle itself
##        if r==l:
##            return r
#        #print('mid = ',mid)
#        #print('arr len = ',len(arr))
#        if arr[mid] == x:
#            return mid
#         
#        elif(r==l):
#            return r
#        # If element is smaller than mid, then it 
#        # can only be present in left subarray
#        elif arr[mid] > x:
#            return binarySearch(arr, x, l, mid-1)
# 
#        # Else the element can only be present 
#        # in right subarray
#        else:
#            return binarySearch(arr,x, mid+1, r)
# 
#    else:
#        #return r
#        # Element is not present in the array
#        return -1  

n,d = map(int,input().split(' '))
l = list(map(int,input().split(' ')))
nfy = 0

j=0
mid = 0
ll = sorted(l[j:d])
for i in range(d,n):
    if(d%2==0):
        n1 = ll[d//2]
        n2 = ll[d//2-1]
        med = (n1+n2)/2
    else:
        med = ll[d//2]
    if(2*med<=l[i]):
        nfy+=1
        minn = d//2
        maxx = d-1
    else:
        if(med>=l[i]):
            minn = 0
            maxx = d//2
        else:
            minn = d//2
            maxx = d-1
         
    #print('lll = ',ll[j:i])
    index = binarySearch(ll[j:i],l[i],minn,maxx)
    #j+=1
    #print('index = ',index)
    
    ll.insert(index,l[i])
    #print('ll = ',ll)
    del ll[0]
    #print('del ll = ',ll)
print(nfy)
    