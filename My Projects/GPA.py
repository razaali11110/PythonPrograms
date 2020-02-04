pf=int(input("Enter PF :"))
ap=int(input("Enter AP :"))
dic=int(input("Enter DIC :"))
fit=int(input("Enter FIT :"))
isl=int(input("Enter ISL :"))

B=[pf,ap,dic,fit,isl]

print(B)
A=[]
for j in B:
        if j<=59:
            A.append(1.7)
        elif j<=63:
            A.append(2.0)
        elif j<=66:
            A.append(2.4)
        elif j<=69:
            A.append(2.7)
        elif j<=74:
            A.append(3.0)
        elif j<=79:
            A.append(3.4)
        elif j<=84:
            A.append(3.7)
        elif j<=100:
            A.append(4.0)

print(A)

pf=A[0]
ap=A[1]
dic=A[2]
fit=A[3]
isl=A[4]

gpa=( (pf*4)+(ap*4)+(dic*3)+(fit*3)+(isl*2) ) / 16
print(gpa)

#INTENDED
# pf="50"                               #11 from 20     mid
#                                     #32 / 40     sessional
# dic="60"                              # 9 / 20        mid
#                                       # 19 / 20        dic assignment
# fit="60"
# isl="60"

# pf=12+20
# ap=25.5
# dic=9
# fit=75
# isl=75



# pf=11                                     #11 from 20     mid
# ap=25.5                             #25.5 from 40   sessional marks of AP
# dic=9+19                                      # 9 / 20  mid
#                                             #19 / 20    dic assignment
# fit=40
# isl=50





