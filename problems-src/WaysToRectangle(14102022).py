n = int(input())

U_List = []
U_List_Final = []

for i in range(1,n//2):
    tup = ()
    if(n%i == 0):
        tup += (i,n//i)
        U_List.append(tup)

#print(U_List)

for i in range(0,(len(U_List)//2)+1):
    U_List_Final.append(U_List[i])

print(len(U_List_Final))

for i in U_List_Final:
    print(i[0],i[1])
