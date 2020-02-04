n=4
A=[]
for i in range(n):
    x=int(input("Enter Number : "))
    A.append(x)
print(A)

# n=3
# A=[]
# for i in range(n):
#     B=[]
#     for j in range(n):
#         x=int(input("Enter Number : "))
#         B.append(x)
#     A.append(B)
# print(A)


# n=int(input("Enter Number :"))
# try:
#     d=5/n
# except ZeroDivisionError:
#     print("ZERO DIVISION ERROR")
# else:
#     print("DIVISION SUCCESSFUL")
#     print("THANKS FOR USING THIS SOFTWARE")
#
# n=9
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


# n=153
#
# l=len(str(n))
# orig=n
# sum=0
# while n>0:
#     sum=sum+(n%10)**l
#     n=n//10
# if orig == sum:
#     print("A")
# else:
#     print("NA")
