a="aabbbc"
res=""
seen =set()
for i in a:
    if i not in seen:
        res+=i
        seen.add(i)
print(res)









