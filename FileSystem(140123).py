def checkValidity(Action,edges,IDs):
    source,destination,filename = Action.split()
    
    current_file_path = [1]
    destination_path = [1]
    
    moving_file_ID = IDs[filename]
    
    #print(moving_file_ID)
    
    #print(source.split('/'))
    
    for i in source.split('/'):
        if(i!=''):
            current_file_path.append(IDs[i])
    
    #print(current_file_path)
    
    for i in destination.split('/'):
        if(i!=''):
            destination_path.append(IDs[i])
    
    #print(destination_path)
    
    final_directory = destination_path[len(destination_path)-1]
    
    #print(final_directory)
    
    nodes_in_final = []
    
    
    for i in edges:
        if(i[0]==final_directory):
            nodes_in_final.append(i[1])
    
    #print(nodes_in_final)
    
    if moving_file_ID not in nodes_in_final:
        print('yes')
    else:
        print('no')
            
            
        
    
    
    

N = int(input())
M = int(input())

Edge_File_IDs = []
File_IDs = dict({})

for i in range(M):
    id1,id2 = input().split()
    Edge_File_IDs.append((int(id1),int(id2)))

#print(Edge_File_IDs)

files = [i for i in input().split()][:N]

for i in range(1,len(files)+1):
    File_IDs.update({files[i-1]:i})
    
#print(File_IDs)

Q = int(input())

Queries = []

for i in range(Q):
    query = input()
    Queries.append(query)

#print(Queries)

for i in Queries:
    checkValidity(i,Edge_File_IDs,File_IDs)

    
