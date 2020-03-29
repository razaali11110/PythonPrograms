# #If len is odd return middle letter if even return two middle chrs
# def middle(a):
#     l = len(a) // 2
#     if len(a) % 2 == 1:
#         return a[l]
#     else:
#         return a[l - 1:l + 1]
#
# a=input("Enter Anything : ")
# print(middle(a))
#
# s1="Hello !"
# s3="sir..."
# s2=input("Enter Your name : ")
# s2=s2.title()
# print(s1,s2,s3)

a="PyNaTive"
b=""
for i in a:
    if i == i.lower():
        b+=i
for j in a:
    if j == j.upper():
        b+=j
print(b)

#Balanced Characters : if all the chars in s1 are in s2...

s1="Junaid"
s2="ai"
for i in s2:
    if i in s1:
        pass
    else:
        print("NOT BALANCED DUE TO",i)

        
