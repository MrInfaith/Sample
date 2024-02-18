def vowelcount(s):
    cnt=0
    v=['a','e','i','o','u']
    for i in s:
        if i in v:cnt+=1

    return s


print(vowelcount("sachin"))
