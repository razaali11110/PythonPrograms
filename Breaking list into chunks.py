A=list(range(1,20))
print(A)

l=len(A)
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + 4]

    # How many elements each

# list should have
n = 4
x = list(divide_chunks(A, n))
print(x)



# A = []
# for i in range( 1 , ( len(l)//4 )+1 ):              #to make it easy to compare 4 digit values for hex
#     A.append( l [ (i-1)*4 : (4*i) ])                #get every 4 bit range and append
# print(A)
