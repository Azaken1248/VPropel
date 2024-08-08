def checkValidity(reg_no):
    if (len(reg_no) == 9):

        L = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        Join_Year = reg_no[0:2]
        branch = reg_no[2:5]
        reg = reg_no[5:8]

        if ((Join_Year[0] in L) and (Join_Year[1] in L)):
            if ((branch.isupper()) and (branch[0]=='B') and (branch[1] in str) and (branch[2] in str)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


registration_number = input("ENTER A REG NUMBER : ")

if (checkValidity(registration_number)):
    print("YES")
    pass_year = int("20" + str(int(registration_number[0:2]) + 4))

    if (pass_year < 2003 and pass_year > 3000):
        pass
    else:
        print(pass_year)
else:
    print("NO")