#*******************************************************************************************************#
#Name:              陳信志                                                                                                                                                             #
#Class:               企管3C                                                                                                                                                            #
#SID:                 S04410376                                                                                                                                                     #
#Program Name: hw5.py                                                                                                                                                           #
#Function:          將使用者所指定工作目錄下含有多少檔案(不含目錄)及使用者指定檔案副檔名為[.txt|.pdf|.exe|.doc|others]型式的檔有多少個    #
#Homework:       No.5                                                                                                                                                               #
#Limitations:      Run on Python 3.X                                                                                                                                           #
#Date:               2018/6/3                                                                                                                                                        #
#*******************************************************************************************************#

import os
import re

lor = 37  # length of report
path = input('Please enter the specified working directory:')  # input the path

try:
    files = os.listdir(path)  # try to get the list of directory

except FileNotFoundError:
    print('The path is not exist.')  # exception

else:
    assign_file = input('Please enter the specified file type\n')  # input the type of file
    file_type = re.search('\w+', assign_file)  # use Regular Expression to get the string after dot(.)

    files = os.listdir(path)  # get the list of directory
    acc_files = []  # save actual file(exclude  folder)
    res = []  # save the result

    for item in files:  # use for loop to do Regular Expression for exclude  folder
        check = re.split('\.', item)
        if len(check) != 1:
            acc_files.append(item)

    for i in acc_files:  # use for loop to do Regular Expression for select the assign file type
        file = re.search('{}$'.format(file_type[0]), i)
        if file is not None:
            res.append(i)  # save the matching value

    print('HW5 Report'.center(lor, '='))
    print(''.center(lor, '_'))
    print('Matching file name:')

    for j in range(len(res)):  # use for loop to orderly output the results
        print('\t{}. {}'.format(j+1, res[j]))

    total = len(acc_files)
    compared = len(res)

    print(''.center(lor, '_'))
    print('There are {} files in this directory,\n of which {} are "{}" file types.'.format(total, compared, assign_file))
    print('End Of Report'.center(lor, '='), '\n\n')
