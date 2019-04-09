def longestSubsequence(arr,n):
    if n==0:
        return 0
    maximum = 1
    dp = [1]*(n)
    inc = [1]*(n)
    dec = [1]*(n)
    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i] and inc[j]>=inc[i]:
                inc[i] = inc[j]+1
            # elif arr[j]>arr[i] and dec[j]>=dec[i]:
            #     dec[i] = dec[j]+1

    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if arr[i]>arr[j] and dec[j]>=dec[i]:
                dec[i] = dec[j]+1

    print('inc = ',inc)
    print('dec = ',dec)

    #dec = dec[::-1]
    for i in range(n):
        maximum = max(maximum,inc[i]+dec[i])


    # mx = inc[0]
    # index = 0
    # for i in range(1,n):
    #     if inc[i]>mx:
    #         mx = inc[i]
    #         index = i
    #
    # elem = dec[index]
    # count = 0
    # #maximum = abs(dec[-1]-dec[index]) + mx
    # #index = 0
    # #mx = dec[0]
    # for j in range(index+1,n):
    #     if dec[j]>elem:
    #         elem = dec[j]
    #         count+=1
    # maximum = mx+count
    # mxx = max(dec)
    # maximum = max(maximum,mxx)

    return maximum-1

# 1 11 2 10 4 5 2 1  #6
# 1 3 5 6 4 8 4 3 2 1  #9
# 8 6 3 4 2 1  #5
# 7 6 8 10 2 5 12 30 31 20 22 18  #8
# 12 11 40 5 3 1  #5
# 148 333 306 200 397 361 458 209 4 436 282 221 358 126 235 489 444 134 42 257 240 305 480 195 102 175 44 345 224 452 249 49 173 200 241 285 438 -9 132 80 238 428 463 334 399 449 242 39 56 453 108 95 492 277 109 188 376 400 265 212 304 223 321 338 120 380 74 459 277 423 176 309 465 135 170 88 11 242 305 11 19 486 -7 414 442 419 3 49 201 150 127 285 -5 166 320 371 12 312 267 202 360 418 481 360 409 347 139 356 277 389 212 491 272 31 206 154 265 291 174 255 398 30 360 450 432 405 244 118 320 147 277 437 495 459 273 218 197 111 449 96 236 341 496 186 61 384 123 428 492 200 389 248 95 248 74 244 300 295 264 18 278 283 51 204 0 78 333 430 168 384 402 347 406 130 64 186 339 385 458 425 120 151 402  #34
for i in range(1):
    l = list(map(int,input().split(' ')))
    n = len(l)
    print(longestSubsequence(l,n))
