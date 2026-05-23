a="aabbcddd"
count={}
for ch in a:
    if ch in count:
        count[ch]+=1
    else:
        count[ch] = 1
print(count)









