a=[9,8,7,6,5,20]
large=a[0]
small=a[0]
for i in a:
    if i>large:
        large=i
    else:
        small=i
print("largest element",large,"smallest element",small)







