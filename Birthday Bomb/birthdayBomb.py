def birthdayBomb(n,arr):
    small = 9999999
    s_index = 0
    for i,j in enumerate(arr):
        if j<small:
            s_index = i
            small = j
    max_kicks = n//small
    res = []
    lll = [s_index]*max_kicks
    res.append(lll)
    ll = list(arr[0:s_index+1])
    sm = 0
    print(' ll = ',ll)
    for i in range(len(ll)):
        index = []
        sm = ll[i]
        ln = 1
        index.append(i)
        smm = sm
        lnn = ln
        indexx = index
        print('s = ',sm)
        for j in range(i+1,len(ll)):
                #smm+=ll[j]

                if smm<=n:
                    #print('smm  =  ',smm)
                    #indexx.append(j)
                    #lnn+=1
                    mm = (n-smm)//ll[j]
                    smm+=ll[j]*mm
                    lnn+=mm
                    #print('mm = ',mm)

                    if mm!=0:
                        indexx.extend([j]*mm)
                    #print('indexx = ',indexx)
                    if lnn==max_kicks:
                        res.append(indexx)
                else:
                    #print('lnn = ',lnn)
                    #print('max = ',max_kicks)

                    if lnn==max_kicks:
                        res.append(indexx)
                        #return indexx
                    smm = sm
                    lnn = ln

    sm = 0
    for i in range(len(ll)):
        index = []
        #m_k = n//ll[i]
        #sm = ll[i]*m_k
        #ln = m_k
        #index.extend([i]*m_k)
        sm = ll[i]
        ln = 1
        index.append(i)
        smm = sm
        lnn = ln
        indexx = index
        if sm<=n:
            for j in range(i+1,len(ll)):
                smm+=ll[j]
                #print('smm = ',smm)
                if smm<=n:
                    indexx.append(j)
                    lnn+=1
                else:

                    if lnn==max_kicks:
                        res.append(indexx)
                    smm = sm
                    lnn = ln
                    indexx = index
            if lnn == max_kicks:
                res.append(indexx)
    print(res)
    res = list(sorted(res))
    return res[0]




n = int(input())
arr = list(map(int,input().split(' ')))
print(birthdayBomb(n,arr))
