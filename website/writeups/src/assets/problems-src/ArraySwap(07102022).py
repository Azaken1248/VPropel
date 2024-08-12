n = int(input())

array1 = list(input().split())
array2 = list(input().split())

for i in range(0,n):
    if(array1[i]>array2[i]):
        array1[i],array2[i] = array2[i],array1[i]

for i in range(0,n):
    print(array1[i],end = " ")
    
print()

for i in range(0,n):
    print(array2[i],end = " ")
