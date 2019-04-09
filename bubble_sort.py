n = int(input())
l = list(map(int,input().split(' ')))
count = 0
for _ in range(n):
    for i in range(n-1):
        if l[i]>l[i+1]:
            count+=1
            l[i],l[i+1] = l[i+1],l[i]
print('Array is sorted in {} swaps.'.format(count))
print('First Element: {}'.format(l[0]))
print('Last Element: {}'.format(l[n-1]))