############### DOCUMENTATION ################
# using this module: https://pypi.python.org/pypi/emoji/
# copy-pasted this emoticon to emoji aliases from here: http://git.emojione.com/demos/ascii-smileys.html
# the aliases list is here: http://www.emoji-cheat-sheet.com/ but I am not using it as it is contained in the module
# NOTE: the vader lexicon has emoticons from both directions :)  and (:
# for the sake of simplicity I stuck by the more usual ones :)
# also, there are many emoticons that correspond to the same emoji :) :-) :)) etc.
# because there was no way to calculate the average sentimentality of each emoticon I kept the
# one that was about in the middle.
##############################################

import emoji
import vaderSentiment
# needed in order to be able to save emojis to file
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# open vader lexicon and turn into dictionary
vaderLexicon = open("vader_sentiment_lexicon.txt", 'r')
vaderDict = {}
for line in vaderLexicon.readlines():
    vaderDict[line.split("\t")[0]] = "\t".join((line.split("\t")[1], line.split("\t")[2], line.split("\t")[3]))

emoticons = open("emoticon_to_emojiAlias_table.txt", 'r') # file containing emoticons
output = open("output.txt", 'w')
for line in emoticons.readlines():
    emoticon = line.split(" ")[0]
    alias = line.split(" ")[1]
    tempString = ""
    if vaderDict.get(emoticon, None):
        tempString += emoji.emojize(alias, use_aliases=True) + "\t"
        tempString += str(vaderSentiment.sentiment(emoticon)['compound']) + "\t"
        tempString += emoticon + "\t"
        tempString += alias + "\t"
        tempString += vaderDict.get(emoticon, None)
        output.write(tempString)
        print tempString
