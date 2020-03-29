def rev(m,n):
    if int(m) * int(n) == int(m[::-1]) * int(n[::-1]):
        n = int(n)
        m = int(m)
        return m, n, m * n

# m=input("Enter Number a : ")
# n=input("Enter Number b : ")

