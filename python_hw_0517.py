import xlrd  # 負責讀取數據
import xlsxwriter  # 負責寫入數據

txt_line = []  # 創建串列
seq_file = open(r"C:\python_data\CP003940.gb")  # 開啟檔案
seq_file.seek(0)  # 使用"file.seek(0)"將指標指向開頭

for line in seq_file:
    txt_line.append(line)  # 將每一筆在seq_file中的資料，使用"[串列].append"存到txt_line串列中
    
#依欄位名稱分別創建相應串列
name = []  # 存放名字
position = []  # 存放位置
product = []  # 存放基因產物

number = 0  # 數量
flag = 0  # 旗標值
count = 0  # 計數器
line_cut = ''

for line in txt_line:  # 依序讀出每列資料
    if(line.find('locus_tag')) >= 0:  # 若資料包含locus_tag
        line_cut = line[line.find('"') + 1   :   len(line) - 2]  # 將該筆資料旗標為前"之後的內容到後"內容存放到line_cut變數中
        if number == 0:
            name.append(line_cut) # 當number為0時，將line_cut增加到name串列中
            number += 1  # 將number+1
            product.append('')  # 將空字串新增到product串列中
            
        elif name[number - 1] == line_cut:  #當line_cut與前一筆name串列中的值一樣時跳過繼續
            continue
            
        else :
            name.append(line_cut)  # 皆非，則將line_cut新增到name串列中
            number += 1  # 將串列數量+1
            product.append('')  # 新增空字串到product串列中
    
    if line.find('gene') == 5 and line.find('note') < 0 and line.find('reference') < 0:  # 如果資料裡面第5個旗標是gene且不存在note與reference
        position.append(line[line.find('gene') + 16:])  # 將gene後16旗標位的內容新增到position串列中

# 創建串列
start_list = []
stop_list = []
count = 0  # 創建計數器
join_pos= []

for k in position:  # 依序讀取position中的值
    if k.find('join') >= 0:  # 如果存在join
        join_pos.append(count) #將計數器值新增到join_pos串列中
        start = k[k.find('(')+1 : k.find('.')]  # k中的(到.中的資料加入start變數中
        stop = k[k.find('..')+2 : k.find(',')]  # k中的..到,中的資料加入stop變數中
        start_list.append(int(start))  #將start中的值轉換成整數型態並加入start_list串列中
        stop_list.append(int(stop))  # 將stop中的值轉換成整數型態並加入stop_list串列中
        count += 1  # 計數器+1

        k = k[k.find(',') + 1  :  ]  # 將原本k中,之後的值指定給k
        start = k[  :  k.find('.')]  # 將k變數中.之前的值指定給start
        stop = k[k.find('..') + 2  :  k.find(')')]  # 將k中..後兩位到)之前的值指定給stop變數
        start_list.append(int(start))  # 將start變數轉換成整數型態新增到start_list串列中
        stop_list.append(int(stop))  # 將stop中的值轉換成整數型態並加入stop_list串列中
        count += 1  # 計數器+1

    else :
        start = k[k.find('(')+1 : k.find('.')]  # (將(後一位到.前面的值存入start變數中
        stop = k[k.find('..')+2 : k.find(')')]  # (將..後兩位到)前面的值存入stop變數中
        start_list.append(int(start))  # 將start變數轉換成整數型態新增到start_list串列中
        stop_list.append(int(stop))  # 將stop中的值轉換成整數型態並加入stop_list串列中
        count += 1  # 計數器+1     

i = 0  # 宣告i變數為0

output = open(r"C:\python_data\HmNO.2.txt", "w")  # 開啟檔案，並使用寫入模式並將其指定給output變數
sum_str = ''  # 宣告sum_str為一空字串
seq_file2 = open(r"C:\python_data\PCC2702.fasta")  # 開啟檔案，並指定給seq_file2變數
seq_file2.seek(0)  # 使用"file.seek(0)"將指標指向開頭

for line in seq_file2:
    sum_str = sum_str + line #  將seq_file2中所有字串串接起來

str = sum_str  # 將sum_str指定給str變數
    
for j in name:  # 把name變數中的資料依序遞迴操作
    
    output.write('>' + j + '\n')  # 輸出> + 名字 + 換行
    
    if len(join_pos) > 0:  # 如果oin_pos長度>0
        if i == join_pos[0]:  # join_pos的第一個字如果是i的值
            output.write(str[start_list[i] + 69:stop_list[i]] + '\n')  # 寫入str字串中第start_list[i]後69的字元到stop_list[i]個字元並換行
            i += 1  # 並將i+1
            output.write('and'+'\n')  # 寫入and字串並換行
            output.write(str[start_list[i] + 69:stop_list[i]] + '\n')  # 寫入str字串中第start_list[i]後69的字元到stop_list[i]個字元並換行
            i += 1  # 並將i+1
            join_pos.pop(0)  #刪除join_pos串列中索引值為0的值

        else :
            output.write(str[start_list[i] + 69:stop_list[i]] + '\n')  # 寫入str字串中第start_list[i]後69的字元到stop_list[i]個字元並換行
            i += 1  # 並將i+1
    else :
        output.write(str[start_list[i] + 69:stop_list[i]] + '\n')  # 寫入str字串中第start_list[i]後69的字元到stop_list[i]個字元並換行
        i += 1  # 並將i+1

output.close()  # 關閉檔案
