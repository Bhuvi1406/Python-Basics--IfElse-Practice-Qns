Score=int(input())
if(Score<35):
    print("Poor Student")
if(Score>=35 and Score<70):
    print("Average Student")
elif(Score>=70 and Score<=101):
    print("Good Student")
else:
    print("Invalid Input")
