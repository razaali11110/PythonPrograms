print("""1.  Fahrenheit
2.  Celcius 
3.  Kelvin
""")
n=int(input("Enter Value in which scale :"))
if n==1:
    f=int(input("Enter value in Fahrenheit : "))
    c=(f-32)/1.8
    k=c+273
    print("Celius       :",c)
    print("Kelvin       :",k)

elif n==2:
    c=int(input("Enter value in Celcius : "))
    f=(1.8*c)+c
    k=c+273
    print("Fahrenheit   :",f)
    print("Kelvin       :",k)

elif n==3:
    k=int(input("Enter value in Kelvin : "))
    c=k-273
    f=f=(1.8*c)+c
    print("Celius       :",c)
    print("Fahrenheit   :",f)




