# For J
n=3
# n=int(input("Enter Number : "))
for i  in range(n):
    for j in range(n):
        if i==0 or j==n//2 or (j<i and i==n-1):
            print("J",end="")
        else:
            print(end=" ")
    print()
print()


# For U
for i  in range(n):
    for j in range(n):
        if j==0 or i==n-1 or j==n-1:
            print("U",end="")
        else:
            print(end=" ")
    print()
print()


# FOr N
for i  in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("N",end="")
        else:
            print(end=" ")
    print()
print()


# For A
for i  in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2 or i==0:
            print("A",end="")
        else:
            print(end=" ")
    print()
print()


# For I
for i  in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print("I",end="")
        else:
            print(end=" ")
    print()
print()


# For D
for i  in range(n):
    for j in range(n):
        if j==0 or (i==0 and j!=n-1) or (i==n-1 and j!=n-1) or (j==n-1 and i!=0 and i!=n-1):
            print("D",end="")
        else:
            print(end=" ")
    print()
