#-*- coding: utf-8 -*-
'''

@author: birdlin
'''
import csv
money = 0

with open ('C:\\Users\\birdlin\\Dropbox\\Program_Workplace\\testPython\\testCSV.csv', 'r', encoding='utf-8') as fin:
    with open ('newtestCSV.txt', 'w', encoding='utf-8') as fout :
        csvreader = csv.reader(fin, delimiter=',')
        csvwriter = csv.writer(fout, delimiter=',')
        header = next(csvreader)
        csvwriter.writerow(header)
        for row in csvreader:
            row[1]= int(row[1].replace(',', ''))/1000
            row[2]= round(int(row[2].replace(',', ''))/100000000, 3)
            row[3]= int(row[3].replace(',', ''))
            row[4]= float(row[4].replace(',', ''))
            row[5]= float(row[5].replace(',', ''))
            money += row[5]
            row.append(money)
            print (row)
            csvwriter.writerow(row)

