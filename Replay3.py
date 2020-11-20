import time

seconds = 0

num = '000111000666000222'

while seconds != 33:

    seconds += 1

    print(seconds)

    if seconds == 33:
        print('OFF')

    if seconds == 9:
        with open('C:\\WG\\WoT_trunks\\win64\\Reports\\Crash000111000666000222.txt', 'a') as sec:
            letter = 'ERROR__'+ num + '__Send me please to CAT.'
            sec.write(str(letter))

    time.sleep(1)