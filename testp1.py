import csv
import os



with open('P1DataA.csv', 'r') as mycsv:
    reader= csv.reader(mycsv)
    mylist=list(reader)
    header=next(reader) #firstline is heade
    for i in reader:

        d={}
        d['First']=i[0]
        d['Last']=i[1]
        d['Email']=i[2]
        d['Class']=i[3]
        d['DOB']=i[4]
    ##for h in i:
    print(i)
