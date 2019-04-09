def count_substring(string, sub_string):
    c=0
    str = string
    while(True):
        n = str.find(sub_string)
        if(n!=-1):
           # n1 = str.index(sub_string)
            #print(n," str = ", str)
            str = str[n+1:]
            c+=1
            #print(n," str = ", str)
        else:
            break
    
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)