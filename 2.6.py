import csv
import glob
import os
input_path = 'C:/Users/AwesomeRick/Desktop/Study/机器学习/csv文件'
file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    row_counter = 1
    with open(input_file,'r',newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader,None)
        for row in filereader:
            row_counter += 1
        print(os.path.basename(input_file),'\t',row_counter,'\t',len(header))
        file_counter += 1
    print('NUumber of files %d' %(file_counter))