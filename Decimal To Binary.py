A=[]
def dtb(num):
    if num>1:
        dtb(num//2)
    print(num%2,end=" ")
    # A.append(num%2)
n=int(input("Enter number: "))
dtb(n)
# print(A)

#IN SIMPLE FORM
num=int(input('Enter Number :'))
bi=""
while num>0:
    bi=str(num%2)+bi
    num//=2
print(bi)

