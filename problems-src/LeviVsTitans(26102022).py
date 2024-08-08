Levi_Pos = int(input())
Moves = int(input())

Distance_Per_Move = list (map(int,input().split()))

#print(Distance_Per_Move)

Beast_Pos = int(input())

Final_Levi_Pos = Levi_Pos+sum(Distance_Per_Move)

#print(Final_Levi_Pos)
if(Final_Levi_Pos > Beast_Pos):
    print("Jaw")
elif(Final_Levi_Pos < Beast_Pos):
    print("Beast")
else:
    print("Levi")
