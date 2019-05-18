# 筛选供应商X或part number>6000的行
import csv
input_file = 'C:/Users/AwesomeRick/Desktop/Study/机器学习/csv文件/supplier_data.csv'
output_file = 'C:/Users/AwesomeRick/Desktop/new 1.csv'
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader) # header为列表变量
        filewriter.writerow(header)
        for row_list in filereader:
            supplier = str(row_list[0]).strip()
            part_num = str(row_list[2]).strip()
            if supplier == 'Supplier X' or int(part_num)>6000:
                filewriter.writerow(row_list)