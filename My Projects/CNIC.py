#first digit
#People whose CNIC number starts with 1, are residents of Khyber Pakhtunkhwa province,
#similarly, 2 represents FATA, 3 for Punjab, 4 for Sindh, 5 represents Balochistan,
# 6 for Islamabad and 7 represents Gilgit-Baltistan province.

#LAST DIGIT
#   man,   1, 3, 5, 7, 9   and     woman, 2, 4, 6, 8
prov={"1":"KPK","2":"FATA","3":"Punjab","4":"Sindh"}

n=(input("Enter CNIC of 13 digit : "))
if len(n)==13:

    f=n[0]


    print("Province : ",prov[f])

    male=[1,3,5,7,9]
    female=[2,4,6,8]
    g=n[12]
    for i in g:
        if i in male:
            print("Gender : Male")
        else:
            print("Gender : Female")
else:
    print(" P l e a s e E n t e r 13 d i g i t n u m b e r ")


# if n[0]==1:
#     p="KPK"
# elif n[0]==2:
#     p="FATA"
# elif n[0]==3:
#     p="Punjab"
# elif n[0]==4:
#     p="Sindh"
# elif n[0]==5:
#     p="Balouchistan"
# elif n[0]==6:
#     p="Islamabad"
# elif n[0]==7:
#     p="GB"
# print("Province :",p)