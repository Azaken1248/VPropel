S1 = input()
S2 = input()

n = int(input())

L = []

for i in range(n-2):
    LS1 = list(S1)  
    LS2 = list(S2)

    Odd_LS1 = LS1[::2]
    Even_LS2 = LS2[1::2]


    for i in range(len(Odd_LS1)):
        if(Odd_LS1[i] != 'z'):
            Odd_LS1[i] = chr(ord(Odd_LS1[i])+1)
        else:
            Odd_LS1[i] = 'a'
    
    for i in range(len(Even_LS2)):
        if(Even_LS2[i] != 'z'):
            Even_LS2[i] = chr(ord(Even_LS2[i])+1)
        else:
            Even_LS2[i] = 'a'

    
    #print(Odd_LS1)
    #print(Even_LS2)

    element = ''

    Combined_L = [Odd_LS1,Even_LS2]


    transpose = [[Combined_L[j][i]for j in range(len(Combined_L))] for i in range(len(Combined_L[0]))]

    for i in transpose:
        for j in i:
            element+=j

    
    
    S1 = S2
    S2 = element
    
    L.append(element)
    #print(element)
        
print(L[len(L)-1])

    
