# -*- coding: utf-8 -*-
import vaderSentiment

fileObj = open("clean_emojis.txt", 'r')

for line in fileObj.readlines():
    print "{}\t{}".format(line.split("\t")[0], vaderSentiment.sentiment(line.split("\t")[0])['compound'])
