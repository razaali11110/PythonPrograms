a=2
b=4
a,b=b,a
print(a)
print(b)


a=5
b=8
temp=a
a=b
b=temp
print("a: ",a)
print("b: ",b)

a=5
b=8
a=a+b
b=a-b
a=a-b
print("a: ",a)
print("b: ",b)

a=10
b=22
c=12
d=15
a,b,c,d = d,c,b,a
print(c)