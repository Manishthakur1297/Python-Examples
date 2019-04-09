l1 = list(input().strip())
l2 = list(input().strip())

d1 = dict()
d2 = dict()

for i in l1:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i]+=1

print('d1 = ',d1)
for j in l2:
    if j not in d2:
        d2[j] = 1
    else:
        d2[j]+=1
print('d2 = ',d2)
res = 0        
for k,v in d1.items():
    if k in d2:
        d2[k] = abs(d2[k] - v)
    else:
        d2[k] = v
        
for k,v in d2.items():
    res+=v
print(res)
