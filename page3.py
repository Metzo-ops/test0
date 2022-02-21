from don_inv import don_inv
import csv
import re
with open('donnees.csv', encoding='utf8') as File:
    reader = csv.reader(File)
don_inv(reader)
