def no_dups(s):
    cache = {}
    results = ''

    for i in s.split():
        if i not in cache and i != '':
            cache[i]=1
        elif i != '':
            cache[i]+=1
    
    for i in cache:
        results += f'{i} '

    return results.strip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))