import time

seconds = 0

while seconds != 45:

    seconds += 1

    print(seconds)

    if seconds == 45:
        print('OFF')

    time.sleep(1)