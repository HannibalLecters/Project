import os
import datetime
import sched, time

path_to_folder = ('C:\\WG\\WoT_trunks\\win64\\Reports\\')

timer = sched.scheduler(time.time, time.sleep)
alarm = 0

def play_script(go):

    if len(os.listdir(path_to_folder)) == 0:
        print('Объекты не найдены')

    for f in (os.listdir(path_to_folder)):
        os.chdir(path_to_folder)
        print('Объект найден -->', f, datetime.datetime.fromtimestamp(os.path.getctime(f)).strftime('[%d %B, %Y, %H:%M:%S]')) 
    timer.enter(5, 1, play_script, (go,))

if len(os.listdir(path_to_folder)) == 0:
    timer.enter(5, 1, play_script, (timer,))
    timer.run()
