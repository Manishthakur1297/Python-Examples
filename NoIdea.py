n,m = map(int,input().split())
n_arr = set(list(map(int,input().split())))
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))

print(len(n_arr.intersection(a)) - len(n_arr.intersection(b)))