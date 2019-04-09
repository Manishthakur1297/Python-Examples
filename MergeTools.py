import textwrap

def merge_the_tools(str, k):
    l = textwrap.wrap(str,k)
    
    #print(l)
    for i in range(len(l)):
        s = l[i]
        string = ""
        for j in range(k):
            if s[j] not in string:
                string+=s[j]
                
        print(string)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)