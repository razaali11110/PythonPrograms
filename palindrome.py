#a word, phrase, or sequence that reads the same backwards as forwards,
# e.g. madam or nurses run

a=input("Enter first string : ")
b=input("Enter second string : ")
a=a.lower()
b=b.lower()
c=""
for i in a:
        if i==" ":
            continue
        else:
            c+=i
print(c)

d=""
for j in b:
    if j==" ":
        continue
    else:
        d+=j
print(d)


if c==d[::-1]:
    print("Palindrome")


fruits=["banana","apple","orange","grapes",]
for fruit in fruits:
    print(fruit.title()[::-1],end=" ")

rev=""
n=input("Enter Name 1 : ")
m=input("Enter Name 2 : ")
for i in m:
    rev=i+rev
if n==rev:
    print("PAN AND DROP")

#Alternative

n=input('Enter Name 1 : ')
m=input('Enter Name 2 : ')
if n==m[::-1]:
    print("PANDROP")
