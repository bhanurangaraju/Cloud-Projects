#!/usr/bin/env python

from operator import itemgetter
import sys

#initialing the variables
word = None
cur_count = 0
cur_word = None

for line in sys.stdin:
        #stripping the whitespaces
        line=line.strip()
        #spliting the line to word,count
        word,count = line.split('\t')
        #converting count variable from string to int
        try:
          count = int(count)
        except ValueError:
          continue
        #As mapreduce framework sorts the output of mapper based on key we are going to use it in counting
        if cur_word == word:
                cur_count += count
        else:
          if cur_word:
                print "%s\t%s" %(cur_word,cur_count)
          cur_count = count
          cur_word = word
if cur_word == word:
        print "%s\t%s" %(cur_word,cur_count)