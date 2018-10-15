#Input
num = input ("Last four digits: ")
int(num)

#Process
if num[0] == 8 or num[0] == 9:
        if num[3] == 8 or num[3] == 9:
                if num[1] == num[2]:
                        print ("Ignore")

else:
        print ("Answer")
