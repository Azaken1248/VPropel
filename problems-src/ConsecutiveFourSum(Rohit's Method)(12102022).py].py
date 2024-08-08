n = int(input())

def sumOfConsecutiveNumbers(start,stop,step):
    sum = ((stop*(stop+1))/2) - (((start-1)*(start))/2) 
    return sum

#print(sumOfConsecutiveNumbers(3,6))

res = 0

for i in range(1,n+1,4):
    #print(i)
    temp_sum = sumOfConsecutiveNumbers(1,i)
    #print(temp_sum)

    if(temp_sum == n):
        print(1)
        print(i)
        break
    else:
        res = 1

if(res == 1):
    print(0)
        
    
    
    
