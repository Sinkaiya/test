#!/usr/bin/env python3

import os
import re

path = input("Enter a path to folder:")

list_of_files = os.listdir(path)
count_of_files = len(list_of_files)
os.chdir(path)

# way = str(input('Is it Photo or Screenshot? Type \"p\" or \"s\": '))

# if way == 'p':
for i in range(0, count_of_files):
    if list_of_files[i][:3] == 'IMG':
        n = list_of_files[i][4:8] + '-' + list_of_files[i][8:10] + '-' + list_of_files[i][10:12] + '-' + list_of_files[i][13:15] + '-' + list_of_files[i][15:17] + '-' + list_of_files[i][17:19] + list_of_files[i][-4:]
    elif list_of_files[i][:10] == 'Screenshot':
        n = list_of_files[i][11:]
    elif list_of_files[i][:3] == '201' and list_of_files[i][4:5] != '-':
        n = list_of_files[i][:4] + '-' + list_of_files[i][4:6] + '-' + list_of_files[i][6:8] + '-' + list_of_files[i][9:11] + '-' + list_of_files[i][11:13] + '-' + list_of_files[i][13:15] + list_of_files[i][-4:]
    else:
        continue
    print(n)
    os.rename(list_of_files[i], n)
