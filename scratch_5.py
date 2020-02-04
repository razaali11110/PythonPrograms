n=5
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1

n=153
orig=n
l=len(str(n))
sum=0
while i>0:
    sum+=(n%10)**l
    n=n//10
if n==orig:
    print("AMSTRONG NUMBER")
else:
    print("NOT AMSTRONG NUMBER ")

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=6
print(fact(n))