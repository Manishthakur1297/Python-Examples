# def jump(arr):
#     n = len(arr)
#     dp = [0]*(n+1)
#     #[16,0,0,0,12,13,11,0,0]
#     if n==1:
#         return 1
#     if arr[0]==0:
#         return 0
#     dp[0] = 0
#     mx = arr[0]
#     index = 0
#     for i in range(1,n):
#         limit = arr[i]
#         if mx<i+limit:
#             mx = i+limit
#         if i+mx>=n-1:
#             dp[i] = dp[index]+1
#             print(dp)
#             return dp[i]
#         if mx==i and mx==i+arr[i]:
#                 print(dp)
#                 return -1
#         for j in range(i,i+mx):
#             elem = j+arr[j]
#             if elem<=mx:
#                 dp[j] = dp[i]
#             else:
#                 mx = elem
#                 dp[j] = dp[i]+1
#                 index = j
#     print(dp)
#     return dp[n-1]

def jump(A):

	    last = len(A) - 1
	    jumps = 0
	    reachable = 0      # reachable with current number of jumps
	    next_reachable = 0 # reachable with one additionnal jump
	    for i, x in enumerate(A):

	        if reachable >= last:
	            break

	        if reachable < i:
	            reachable = next_reachable
	            jumps += 1
	            if reachable < i:
	                return -1
	        next_reachable = max(next_reachable, i+x)

	    return jumps




arr = list(map(int,input().split(' ')))
print(jump(arr))
