# Shape of X
# n=int(input("Enter number: "))
n=5
for row in range(0,n):
    for col in range(0,n):
        if row==col or row+col==n-1 or (row<col and row==n-1):
            print("*", end="")
        else:
            print(end=" ")
    print()

print()

#square box
# n=int(input("Enter number: "))
for row in range(0,n):
    for col in range(0,n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*", end="")
        else:
            print(end=" ")
    print()


print()

# n = int(input("Enter Number : "))
for i in range(n):
    for j in range(n):
        if i == j or i > j:
            print("*", end="")
        else:
            print(end="  ")
    print()

for i in range(n):
    for j in range(n):
        if i == j or i < j:
            print("*", end="")
        else:
            print(end=" ")
    print()

