T = int(input())


Word_List=[]
Hashed_Words = []
count_list = []


for i in range(0,T):
    
    L = int(input())
    Word = input()
    
    
    
    if(len(Word) == L):
        
        Hashed_Word = ""
    
        
    
        for j in range(0,L):
            if(j != (L-1)):
                if(Word[j].lower()==Word[j+1].lower()):
                    Word_List.append(Word[j])
                    Word_List.append("#")
                else:
                    Word_List.append(Word[j])
            else:
                Word_List.append(Word[j]+" ")
    
        
        for j in range(0,len(Word_List)):
            Hashed_Word += Word_List[j]
        #print(Hashed_Words)
        
        Hashed_Words.append(Hashed_Word)
        #print(Hashed_Words)
        
        Ar = Hashed_Words[len(Hashed_Words)-1].split()
        
        #print(Ar)
        
        for j in range(0,len(Ar)):
            count = 0
            for k in Ar[j]:
                if(k == "#"):
                    count += 1
            count_list.append(count)
        #count_list.pop(0)
        
        for j in range(1,len(count_list)):
            print(count_list[j])
        
