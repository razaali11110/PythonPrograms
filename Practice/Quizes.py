c=20
score=0
print("Chances :\t",c)
print("Score :\t\t",score)
print("Wrong answer :\t-1\nRight answer:\t+2")
print("""1.Karachi
2.Islamabad
3.Lahore
4.Sukkur""")
a=int(input("Which is the largest city of Pakistan : "))

if a==1:
    score+=2
else:
    score-=1
print("Score :\t",score)