import copy

def transpose(Matrix):
    t = [[Matrix[j][i]for j in range(len(Matrix))] for i in range(len(Matrix[0]))]
    return t

def ChitTransition(Matrix,num,pi,qu):
    new_M = copy.deepcopy(Matrix)
    t = transpose(Matrix)
    
    if(num == pi):
        for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                if(Matrix[i][j] == num):
                    if(qu in Matrix[i] or qu in t[j]):
                        new_M[i][j] = qu
                    
    else:
        for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                if(Matrix[i][j] == num):
                    if(pi in Matrix[i] or pi in t[j]):
                        new_M[i][j] = pi
                    
    
    return new_M
            
    

m = int(input())
n = int(input())
p = int(input())
q = int(input())

kids_m = []
winners = []

for i in range(m):
    row = [int(i) for i in input().split()][:n]
    kids_m.append(row)

l = int(input())

kids_m_t = ChitTransition(kids_m,l,p,q)

#print(kids_m_t)

for i in range(len(kids_m_t)):
    for j in range(len(kids_m_t[i])):
        if(kids_m_t[i][j] == l):
            winners.append([i+1,j+1])

if(winners == []):
    print('No winner')
else:
    for i in winners:
        print(i[0],i[1])
        
