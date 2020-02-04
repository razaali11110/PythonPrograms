

n=int(input("Enter Number of stars in first row: "))

for i in range(n):
    for j in range(n):
        if i==j or i==n-1 :
            print("*",end=" ")
        else:
            print(end=" ")
    print()

for x in range(n,0,-1):
    print((n-x)*" "+"*")

