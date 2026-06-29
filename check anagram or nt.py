def check(a,b):
    if len(a) != len(b):
        return (" not Anagram")
    for i in a:
        if a.count(i)!=b.count(i):
            return ("Not Anagram")
    else:
        return (" Anagram")
print(check("listen","silentl "))
