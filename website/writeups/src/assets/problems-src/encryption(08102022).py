T = int(input())

letters_Og = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



count = 1

encrypted_word = ""

for i in range(0,T):
    
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    word,keyword = input().split()
    
    U = []
    
    for j in keyword:
        if(j in U):
            pass
        else:
            U.append(j)
    
    for j in range(0,len(U)):
        if(U[j] in letters):
            letters.remove(U[j])
        else:
            pass
        
    ref_list = U+letters
    
    #print(ref_list)
    
    indices = []
    
    for j in word:
        indices.append(letters_Og.index(j))
    #print(indices)
    
    for i in range(0,len(indices)):
        print(ref_list[indices[i]],end='')
    print()
    
    
    
    
    
    
    
    
    
    



