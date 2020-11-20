import time

seconds = 0

while seconds != 51:

    seconds += 1

    print(seconds)

    if seconds == 51:
        print('OFF')

    time.sleep(1)