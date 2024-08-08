time_earth = input()

time_val_list = time_earth.split(":")

time_val = ""

for i in range(0,len(time_val_list)):
    time_val += time_val_list[i]

#print(time_val)

L = time_val.split() 
#print(L)

time = L[0]
time_num = int(L[0])
#suffix = L[1]

if(time_num == 120000 ):
    print("08:00:00 midnight")
    
if(time_num>0 and time_num<=75959):
    print(time[0:2]+":"+time[2:4]+":"+time[4:6]+" A.M")
    
if(time_num == 80000):
    print(time[0:2]+":"+time[2:4]+":"+time[4:6]+" midmorning")


if(time_num>80000 and time_num<=155959 and time_num!=120000):
    
    Ar =[]
    for i in time[0:2]:
        Ar.append(i)
    
    if(Ar[0] == "0"):
        temp_num = int(Ar[1])
        temp_num -= 8
        print(temp_num)
        print("0"+str(temp_num)+":"+time[2:4]+":"+time[4:6]+" B.M")
    else:
        temp_num_1 = ""
        temp_num = 0 
        for i in range(0,len(Ar)):
            temp_num_1 += Ar[i]
        temp_num = int(temp_num_1) 
        temp_num -= 8
        print("0"+str(temp_num)+":"+time[2:4]+":"+time[4:6]+" B.M")

if(time_num == 160000):
    print("08:00:00 midevening")
    
if(time_num>160000 and time_num<=235959 and time_num!=120000):
    Ar =[]
    for i in time[0:2]:
        Ar.append(i)
    
    if(Ar[0] != "0"):
        temp_num = int(Ar[1])
        temp_num -= 8
        print("0"+str(temp_num)+":"+time[2:4]+":"+time[4:6]+" C.M")
    else:
        temp_num_1 = ""
        temp_num = 0 
        for i in range(0,len(Ar)):
            temp_num_1 += Ar[i]
        temp_num = int(temp_num_1) 
        temp_num -= 8
        print(str(temp_num)+":"+time[2:4]+":"+time[4:6]+" C.M")
