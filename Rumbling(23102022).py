
N = int(input())

List_Pair = []

count = 0

if(N<10000):
    for i in range(1,N+1):
        for j in range(1,N+1):
            Pair = [i,j]
            #print(Pair)
            List_Pair.append(Pair)
    
    print(List_Pair)
    
    for i in range(0,len(List_Pair)):
        if((List_Pair[i][0]+List_Pair[i][1])%2 != 0):
            count+=1
    
    print(count)
            
