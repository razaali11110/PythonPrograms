A=[["a","e","i","m","q","u","y"],["b","f","j","n","r","v","z"],["c","g","k","o","s","w"],["d","h","l","p","t","x"]]
for i in range(len(A)):
    for j in A[i]:
        print(j, end=" ")
    print()


A=list(range(20))
for i in range(len(A)):
    for j in str(A[i]):
        print(j, end=" ")
    print()

