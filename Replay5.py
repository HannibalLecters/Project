import time

seconds = 0

while seconds != 28:

    seconds += 1

    print(seconds)

    if seconds == 28:
        print('OFF')

    time.sleep(1)