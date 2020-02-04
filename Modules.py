import math
x=6
print(math.factorial(x))
print(math.gcd(30,100))                         #Greatest common divisor

import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)