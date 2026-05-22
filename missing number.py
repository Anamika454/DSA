a=[1,3,4,5]
n=5
expect_sum=n*(n+1)//2
actual_sum=sum(a)
missing=expect_sum-actual_sum
print(missing)
