#!/usr/bin/python3.8
# script to add demarkation line to log file - to differentiate runs
# takes title of new test, put config and stuff here as input

import os
import sys

resultsdir = './results/'
title = sys.argv[1]

for filename in os.listdir(resultsdir):
    with open(os.path.join(resultsdir, filename), 'a') as f:
        f.write(f'--- {title} ---\n')

print('book keeping done')