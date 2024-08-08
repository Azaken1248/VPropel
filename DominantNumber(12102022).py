m = int(input())
n = int(input())

sum_1 = 0
sum_2 = 0

for i in range(2,m):
    if(m%i==0):
        sum_1 += i

for i in range(2,n):
    if(n%i==0):
        sum_2 += i

#print(sum_1)
#print(sum_2)

if(sum_1 > sum_2):
    print(m)
elif(sum_1 < sum_2):
    print(n)
else:
    print("No dominance")
