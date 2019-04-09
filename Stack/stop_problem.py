def stock(l,n):
    nl = []
    st = []
    nl.append(l[0])
    #print("nl = ",nl)
    st.append(1)
    for i in range(1,n):
        c = 1
        #print("c = ",c)
        if(len(nl)>0 and nl[-1]>=l[i]):
            nl.append(l[i])
            st.append(c)
            #print("nl = ",nl)
            #print("st = ",st)
            
        else:
            j = -1
            print(" i = ",i,"nl = ",nl,"st = ",st,"l = ",l)
            while(len(nl)>0 and nl[-1]<l[i]):
                c+=1
                nl.pop()
            #print("nl = ",nl)
            #print("st = ",st)
            if(len(nl)==0):
                st.append(i)
                nl.append(l[i])
                print("index = ",index," i = ",i,"nl = ",nl,"st = ",st,"l = ",l)
            else:
                index = l.index(nl[-1])
                print("index = ",index," i = ",i,"nl = ",nl,"st = ",st,"l = ",l)
                st.append(i-index)
                nl.pop()
                
    return st

# l = list(map(int,input().split(' ')))
l = [90,50,60,70,40,90,100]
n = len(l)
st = stock(l,n)
print(*st)
#print(' '.join(st))