a=[2,7,11,15]
target=9
seen={}
for i in a:
    required=target-i
    if required in seen:
        print(required,i)
        break
     seen[i]=True





