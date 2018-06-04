import os
import re

path = r'D:\tHUbA\2018s\Python\pp'

assign_file = '.py'

files = os.listdir(path)

file_type = assign_file[1:]

for i in range(0, len(files)):

    if re.search('{}$'.format(file_type), files[i]):
        
        print(counter, files[i])
