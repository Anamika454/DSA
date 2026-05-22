a=[12,35,1,34,1]
largest=0
second=0
for i in a:
    if i >largest:
        second=largest
        largest=i
    elif i > second and i!=largest:
        second=i
print("second largest",second)