n , amt = map(int,input().split(' '))
l = sorted(list(map(int,input().split(' '))))
c  = 0
count = 0
for i in range(n):
    if ((c+l[i])<=amt):
        count+=1
        c+=l[i]
    else:
        break
print(count)

