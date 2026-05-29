a=[1,2,3]
is_sorted=True
for i in range (len(a)-1):
    if a[i]>a[i+1]:
        is_sorted=False
if is_sorted:
    print("sorted")
else:
    print("not sorted")









