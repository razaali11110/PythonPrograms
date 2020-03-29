a = "3,5,7,23"
A=[]
for i in range(len(a)):
    for j in a[i]:
        if j==",":
            A.append(a[i-1])
print(A)

# 8. Write a Python program to display the first and last colors from the following list.
# Go to the editor

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Go to the editor
# Sample value of n is 5
# Expected Result : 615

# n=int(input("Enter Number : "))
n=5
a=0
for i in range(1,4):
    a+=n**i
print(a)
n=5
A=list(range(1,n+1))
for i in A:
    print("*"*i)

# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)

# x1=int(input("Enter x1 : "))
# x2=int(input("Enter x2 : "))
# y1=int(input("Enter y1 : "))
# y2=int(input("Enter y2 : "))
#
# d=((x2-x1)+(y2-y1))**1/2
# print(d)