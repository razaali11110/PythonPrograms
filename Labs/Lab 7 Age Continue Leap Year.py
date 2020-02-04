# Lab 7.1

age=int(input("Enter age: "))
if age<2:
    print("The person is a baby")
elif age<4:
    print("This person is a toddler")
elif age<13:
    print("The person is kid")
elif age<20:
    print("The person is teenager")
elif age<65:
    print("The person is adult")
else:
    print("The person is elder")

# Lab 7.2

# Print all the numbers from 1 to 20 except 9 and 13
for i in range(1,21):
    if i==9 or i==13:
        continue
    print(i," ",end="")

# Lab 7.3

n=int(input("Enter Year: "))
if n%4==0 and n%400==0 or n%100!=0:
    print("This is a Leap Year.")
else:
    print("This is not a leap year")

