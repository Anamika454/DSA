a=[9,8,7,6,5,9]
larg=0
count=0
for i in a:
    if i>larg:
        larg=i
        count=1
    elif i==larg:
        count+=1
print("largest",larg,"count",count)

