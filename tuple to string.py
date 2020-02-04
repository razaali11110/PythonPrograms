a=("2","3","4","5","6","7")
sep=" "
print(sep.join(a))
print(a)
# create tuple object and assign it to variable t
t = ('Jan','Feb','Mar','Jan')

# create single space string and assign it to variable separator
separator = ' '

# call join() method on separator by passing tuple t as an argument
output = separator.join(t)

# print the value of variable output
print(output)