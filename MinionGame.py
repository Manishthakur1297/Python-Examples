def minion_game(str):
    string = str.lower()
    stuart = {}
    kevin = {}
    k_c = 0
    s_c = 0
    for i in range(len(string)):
        for j in range(i,len(string)):
            if string[i] in ('a','e','i','o','u'):
                
                #kevin.append(string[i:j+1])
                count = string.count(string[i:j+1])
                if string[i:j+1] in kevin:
                    continue
                    #kevin[string[i:j+1]].append(pagenumber)
                else:
                    kevin[string[i:j+1]] = [count]
                    k_c+=count
            else:
                #stuart.append(string[i:j+1])
                count = string.count(string[i:j+1])
                if string[i:j+1] in stuart:
                    continue
                    #kevin[string[i:j+1]].append(pagenumber)
                else:
                    stuart[string[i:j+1]] = [count]
                    kevin[string[i:j+1]] = [count]
                    s_c+=count
                
    #k = set(kevin)
    #s = set(stuart)
    #print(stuart)
    #print(kevin)
    #print(s_c)
    #print(k_c)
    
    if(s_c>k_c):
        print("Stuart",s_c)
    else:
        print("Kevin",k_c)



if __name__ == '__main__':
    s = input()
    minion_game(s)