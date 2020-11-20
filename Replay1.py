import time

seconds = 0

while seconds != 60:

    seconds += 1

    print(seconds)

    if seconds == 60:
        print('OFF')

    time.sleep(1)
