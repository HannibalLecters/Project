import os.path
import datetime

path_to_folder = (r'C:\WG\WoT_trunks\win64\\Reports')

success = 0
fail = 0
  
if os.path.exists(path_to_folder):
    print ('Объект найден -->', os.listdir(path_to_folder)) #datetime.fromtimestamp(str(os.path.getctime(path_to_folder)))

else:
    print ('Объект не найден', '--> Иди поищи ошибки')