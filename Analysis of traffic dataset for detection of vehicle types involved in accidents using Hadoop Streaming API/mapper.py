#!/usr/bin/env python

import sys
import re
for line in sys.stdin:
                count = 0
                #striping whitespaces in a line
                line = line.strip()
                
                #replacing the content in "" by none
                line = re.sub(r'".*"', '', line)
                
                #splitting the line in to words seperated by comma
                words=line.split(',')
                
                #To skip header part from the file
                if words[0] != "DATE" :
                        for word in words:
                                count = count + 1
                                if count >= 25 and word != "" :   
        #columns with vehicle types are from 25-29
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
                                        print '%s\t%s' %(word,1)                         
