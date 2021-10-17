import random

rollByComputer=random.randrange(1,6)
rollByUser=int(input("Enter a number from 1 to 6: "))
if(rollByUser==rollByComputer):
    print(True)
print("Number from computer is: ",rollByComputer)