

#PLUS SHAPE
n=5
for row in range(0,n):
    for col in range(0,n):
        if col==n//2 or row==n//2:
            print("*", end="")
        else:
            print(end=" ")
    print()

n=10
for row in range(0,n):
    for col in range(0,n):
        if col==0 or row==0 or row==n-1 or col==n-1:
            print("*", end="")
        else:
            print(end=" ")
    print()
#                   J shape
n=5
for row in range(0,n):
    for col in range(0,n):
        if col==2 or row==0 or (col==0 and row==4) or (col==0 and row==3):
            print("*", end="")
        else:
            print(end=" ")
    print()

n=5
for row in range(0,n):
    for col in range(0,n):
        if col+row==n-1:
            print("*", end="")
        else:
            print(end=" ")
    print()

n=5
for i in range(n):
    print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))

n=5
for i in range(n):
    print(" "*(n-i-1)+("*"+" ")*(i+1))


