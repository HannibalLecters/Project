import os
import datetime
import time

path_to_folder = ('C:\\WG\\WoT_trunks\\win64\\Reports\\')

def start_script():

    alarm = 0

    while alarm == 0:

        if len(os.listdir(path_to_folder)) == 0:
            print('Объекты не найдены')

        for f in (os.listdir(path_to_folder)):
            os.chdir(path_to_folder)
            print('Объект найден -->', f, datetime.datetime.fromtimestamp(os.path.getctime(f)).strftime('[%d %B, %Y, %H:%M:%S]')) 

        if len(os.listdir(path_to_folder)) != 0: #Действия после краша
            alarm += 1

        time.sleep(5)

start_script()