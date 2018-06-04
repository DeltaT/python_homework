import os
import re

lor = 37  # length of report
path = input('Please enter the specified working directory:')  # input the path

try:
    files = os.listdir(path)  # try to get the list of directory

except FileNotFoundError:
    print('The path is not exist.')  # exception

else:
    sof = set()  # create a set to save extension of files
    file_counter = 0  # count total files in path

    for i in range(0, len(files)):
        ex = re.split('\.', files[i], len(files))  # use Regular Expression to get the string after dot(.)

        if len(ex) == 2:  # check file or folder
            file_counter += 1
            sof.add(ex[1])

    lof = list(sof)  # convert the type

    print('File type which exist:', lof)  # show what kind of extension is available

    assign_file = input('Please enter the specified file type:')  # input the type of file
    files = os.listdir(path)
    file_type = assign_file[1:]

    print('HW5 Report'.center(lor, '='))
    print(''.center(lor, '_'))
    print('Matching file name:')

    amount = 0

    for i in range(0, len(files)):
        if re.search('{}$'.format(file_type), files[i]):
            amount += 1
            print('\t%d. %s' % (amount, files[i]))

    print(''.center(lor, '_'))
    print('There are {} files in this directory,\n of which {} are "{}" file types.'.format(file_counter, amount,
                                                                                            assign_file))
    print('End Of Report'.center(lor, '='), '\n\n')
