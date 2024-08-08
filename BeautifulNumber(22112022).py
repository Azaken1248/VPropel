n = int(input())

L = []
if(n in range(1,999999999999999999)):
    def distinct(string):
        dis_str = ""
        for i in string:
            if i not in dis_str:
                dis_str += i
        return dis_str

    for i in range(8,n):
        str_i = str(i)
        if(distinct(str_i)=='89' or distinct(str_i)=='98'):
            L.append(i)


    val = False
    for i in L:
        if(n%i==0):
            val = True
    if(val == True):
        print('beautiful')
    else:
        print(-1)
