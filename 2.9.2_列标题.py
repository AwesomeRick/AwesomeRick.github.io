import csv
input_file = 'C:/Users/AwesomeRick/Desktop/Study/机器学习/csv文件/supplier_data.csv'
output_file = 'C:/Users/AwesomeRick/Desktop/new 1.csv'
my_columns = ['Supplier Name', 'Part Number']
my_columns_index = []
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader, None)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        filewriter.writerow(my_columns)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)