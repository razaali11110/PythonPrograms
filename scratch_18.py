print("Good Luck!")
print("1\t2\t3\t4\na\tb\tc\td\ne\tf\tg\th\ni\tj\tk\tl\nm\tn\to\tp\nq\tr\ts\tt\nu\tv\tw\tx\ny\tz")
# list=(("a\te\ti\tm\tq\tu\ty"),
#       ("b\tf\tj\tn\tr\tv\tz"),
#       ("c\tg\tk\to\ts\tw"),
#       ("d\th\tl\tp\tt\tx"))
list=[["a","e","i","m","q","u","y"],["b","f","j","n","r","v","z"],["c","g","k","o","s","w"],["d","h","l","p","t","x"]]
strList=(("a\te\ti\tm\tq\tu\ty\n"),("b\tf\tj\tn\tr\tv\tz\n"),("c\tg\tk\to\ts\tw\n"),("d\th\tl\tp\tt\tx\n"))

n=int(input("Enter Number : "))
A=[]
for i in range(n):
    t=int(input("Enter Col "+ str(i+1) +" : "))
    A.append(list[t-1])
print()
print("\t1\t2\t3\t4\t5\t6\t7")
for x in range(len(A)):
        print(A[x])
print()
B=[]
for j in range(n):
    p=int(input("Enter Col "+ str(j+1) +" : "))
    B.append(A[j][p-1])
for y in range(len(B)):
    print(B[y],end="")