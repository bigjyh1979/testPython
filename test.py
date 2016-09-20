#-*- coding: utf-8 -*-
'''

@author: birdlin
'''
import csv
avg_money = 0
money = [0] * 10
i = 1
with open ('testCSV.txt', 'r', encoding='utf-8') as fin:
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
            if i >= 10 :
                i = 10
            j = i-1
            while j > 0 :
                money[j] = money[j-1]
                j -= 1
            money[0] = row[5]
            avg_money = sum(money)
            row.append(avg_money)
            row.append(avg_money/i)
            i+=1
            print (row)
            csvwriter.writerow(row)

