import csv

with open("C:\\Users\\kachanta\\Downloads\\OfficeSupplies.csv",'r') as file:
    read=csv.reader(file)
    # print(type(read))
    for line in read:
         print(line[0],line[-1])