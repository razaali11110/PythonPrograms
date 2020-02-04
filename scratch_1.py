def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input("Enter Number :"))
print(fact(n))


# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(7))
#
# n=int(input("Enter Number : "))
# isprime = 0
# for i in range(2,n):
#     if n%i==0:
#         isprime==1
#         pass
# if isprime==0:
#     print("PRIME")
# else:
#     print("NP")
