import re


def check1():

    while True:
        string = str(input())
        str_res = re.findall(r'\w+', string)
        if len(str_res) >= 3:
            return string
            break
        else:
            continue

def check2():  

    while True:
        string = str(input())
        str_res = re.findall(r'@\w+\.\w+', string)
        if len(str_res) >= 3:
            return string
            break
        else:
            continue

def check3():
    while True:
        string = str(input())
        str_res = re.findall(r'\d{2}-\d{2}-+\d{4}', string)
        if len(str_res) >= 3:
            return string
            break
        else:
            continue      
    
def function1(string):

    p1 = re.findall('.', string)
    p2 = re.findall(r'\w', string)
    p3 = re.findall(r'\w*', string)
    p4 = re.findall(r'\w+', string)
    p5 = re.findall(r'^\w+', string)
    p6 = re.findall(r'\w+$', string)
    p7 = re.findall(r'^.{1,2}', string)
    
    string2 = re.split(' ', string)
    p8 = []
    for str in string2:
        res = re.findall(r'^[a|e|i|o|u|A|E|I|O|U]\w+', str)
        if(res!=[]):
            p8.append(res)

    return p1, p2, p3, p4, p5, p6, p7, p8

def function2(string):

    p9  = re.findall(r'@\w+', string)
    p10 = re.findall(r'@\w+.\w+', string)
    p11 = re.findall(r'@\w+.(\w+)', string)
    p12 = re.findall(r'(\w+[\.]*\w+)@', string)
    return p9, p10, p11, p12

def function3(string):
    
    p13 = re.findall(r'\d\d-\d+-\d+', string)
    p14 = re.findall(r'\d{2}-+\d{2}-+(\d{4})', string)
    return p13, p14


def main():
    print('Please enter at least 3 words in a string and splite by space:')
    string1 = check1()
    #string1 = 'This is an apple'
    res1, res2, res3, res4, res5, res6, res7, res8 = function1(string1)
    print('\n')
    print('[P-1] Output:\n', res1)
    print('[P-2] Output:\n', res2)
    print('[P-3] Output:\n', res3)
    print('[P-4] Output:\n', res4)
    print('[P-5] Output:\n', res5)
    print('[P-6] Output:\n', res6)
    print('[P-7] Output:\n', res7)
    print('[P-8] Output:\n', res8)
    print('\n\n')
    
    print('Please enter at least 3 Email addresses in a string and splite by space:')
    string2 = check2()
    #string2 = 's102356@gmail.com, cia@test.gov.us, john@winworld.com, first.test@travel.biz'
    res9, res10, res11, res12 = function2(string2)
    
    print('[P-9] Output:\n', res9)
    print('[P-10] Output:\n', res10)
    print('[P-11] Output:\n', res11)
    print('[P-12] Output:\n', res12)
    print('\n\n')
    
    print('Please enter at least 3 date-format in a string and splite by space:')                       
    string3 = check3()
    #string3 = 'LIZ 88-1057 12-07-1998, XYZ 56-7893 12-10-2014, ABC 99-1011 05-31-2017'
    res13, res14 = function3(string3)
                           
    print('[P-13] Output:\n', res13)
    print('[P-14] Output:\n', res14)
                       
main()
