# (1) The program starts by prompting the user to enter the time in seconds (e.g., 10 seconds). 
# (2) Then, the program starts printing out the seconds (e.g., 00:10, 00:09, etc.) one line every one second. 
# (3) At the end, the program prints out “Time is up!”

import time

def sectomins(secs):
    return int(secs / 60),int(secs % 60)

ctime = int(input("Enter the time in seconds: "))

while ctime != 0:
    mins, secs = sectomins(ctime)
    print(f"{mins:02}:{secs:02}")
    ctime = ctime - 1
    time.sleep(1)

else:
    print("Time's up!")
