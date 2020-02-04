#SCRAMBLING Words

from random import randint
n=input("Enter Word : ")
A=[]
b=len(n)
l=len(n)
while l>0:
    r=randint(0,b-1)
    for i in n[r]:
        if r in A:
            l+=1
            continue
        else:
            print(n[r],end=" ")
            A.append(r)
            l-=1

#SCRAMBLING SENTENCE

from random import randint
n=input("Enter your sentence : ")
n=n.split()
print(n)
b=len(n)
l=len(n)
A=[]
while len(n)>0:
    r=randint(0,b-1)
    for i in n[r]:
        if r in A:
            l+=1
            continue
        else:
            print(n[r],end=" ")
            A.append(r)
            l-=1


#Input next word
# a=input("Enter letter")
# for i in a:
#     b=0
#     b=ord(i)+1
#     print(chr(b),end="")



#How can I determine if a number n is a power of 3?
# n=int(input("Enter Number : "))
# r=list(1,n)
# print(r,end=" ")
