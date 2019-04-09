def minion_game(str):
    string = str.lower()
    stuart = []
    kevin = []
    #k_c = 0
    #s_c = 0
    for i in range(len(string)):
        for j in range(i,len(string)):
            if string[i] in ('a','e','i','o','u'):
                kevin.append(string[i:j+1])
            else:
                stuart.append(string[i:j+1])
    
    #print(len(stuart))
    #print(len(kevin))
    #print(s_c)
    #print(k_c)
    
    if(len(stuart)>len(kevin)):
        print("Stuart",len(stuart))
    else:
        print("Kevin",len(kevin))



if __name__ == '__main__':
    s = input()
    minion_game(s)