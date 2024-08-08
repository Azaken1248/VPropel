n = int(input())

#digit_list = []
   
result = 0
num_1 = 0

for i in range(1,n//2):
    if((i+3)<=n//2):
        temp_sum = 4*i+6
        if(temp_sum == n):
            result = 1
            num_1 = i
            break
        else:
            result = 0
        
if(result==1):
    print(1)
    print(num_1)
else:
    print(0)
