from datetime import datetime
#Current Time

now = datetime.now().strftime("%H:%M:%S")
print("Current Time =", now)

print()
print(datetime.today())

import time
for i in range(60):
    print(i+1,now)
    time.sleep(0.25)

#Current DATE
now = datetime.now().date() # time object
print("Current Date =", now)



#Current TIME
from datetime import datetime
now = datetime.now().time() # time object
print("Time =", now)



