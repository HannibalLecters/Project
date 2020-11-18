import os
import datetime

path_to_folder = ('C:\\WG\\WoT_trunks\\win64\\Reports\\')

if len(os.listdir(path_to_folder)) == 0:
    print('Объекты не найдены')

for f in (os.listdir(path_to_folder)):
    os.chdir(path_to_folder)
    print('Объект найден -->', f, datetime.datetime.fromtimestamp(os.path.getctime(f)).strftime('[%d %B, %Y, %H:%M:%S]')) 