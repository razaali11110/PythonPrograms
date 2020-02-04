n=input("Enter 1 : ")
x=input("Enter 2 : ")

rev=""
for i in x:
    rev=i+rev

if n==rev:
    print("PAIN AND DROP")
else:
    print("NOT PAIN AND DROP")