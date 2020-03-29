def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n=int(input("Enter n : "))
r=int(input("Enter r : "))

num=fact(n)
den=fact(n-r)
den_r=fact(r)

p=num//den
print("Permutation : ",p)

c=num//(den*den_r)
print("Combination : ",c)

#Hanshakes nC2

def handshakes(n):
    return (n*(n-1))//2

# n=int(input("Enter Number : "))
n=30
print(handshakes(n))

