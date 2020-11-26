#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as file:
    data = file.readlines()
    new_data = []
    final_data = []
    for line in data:
        new_data.append(line.strip())
    #print(new_data)
    for line in new_data:
        final_data.append(line.replace('jane', 'jdoe'))
    #print(final_data)

    for line in new_data:
        index = 0
        #print('mv ' + line + ' ' + final_data[index])
        subprocess.run('mv ' + line + ' ' + final_data[index], shell=True)
        index = index+1