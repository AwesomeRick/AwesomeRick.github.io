
import csv
input_file = 'C:/Users/AwesomeRick/Desktop/Study/机器学习/csv文件/supplier_data.csv'
output_file = 'C:/Users/AwesomeRick/Desktop/new 1.csv'
important_datas = ['Supplier X', 'Supplier Y']
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_data = row_list[0]
            if a_data in important_datas:
                filewriter.writerow(row_list)