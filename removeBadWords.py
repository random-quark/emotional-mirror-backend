import re
import config

myString = "Miserable bitchee with no money"
# rude_words = ['bitch']
# def containsRudeWords(aString, rudeWords):
#     for r in rudeWords:
#         if r in aString.lower(): return True
#     return False

def containsRudeWords(aString, rudeWords):
    for rw in rudeWords:
        expression = r'\b' + rw + r'\b'
        match = re.search(expression, aString.lower())
        if match:
            print "**** EXCLUDING: ", rw, " TWEET: ", aString
            return True
    return False


# print config.rude_words
print containsRudeWords(myString, config.rude_words)
# print containsRudeWords(myString, rude_words)
