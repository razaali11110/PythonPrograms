a=13
ans=""
while a>0:
    b=a%2
    ans=str(b)+ans
    a=a//2
print(ans)

zero=0
one=0
for i in ans:
    if i=="0":
        zero+=1
    else:
        one+=1
print(zero)
print(one)

ans="1101"
zero=0
one=0
d={}
for i in ans:
    if i=="0":
        zero+=1
        d["Zeros"]=zero
    else:
        one+=1
        d["Ones"]=one
print(zero)
print(one)
print(d)

d={}
d["Zero"]=zero
d["One"]=one
print(d)
