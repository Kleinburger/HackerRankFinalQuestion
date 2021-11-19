import csv

with open('input012.txt', 'r') as fin, open('input013.txt', 'w') as fout:
    o=csv.writer(fout)
    for line in fin:
        o.writerow(line.split())