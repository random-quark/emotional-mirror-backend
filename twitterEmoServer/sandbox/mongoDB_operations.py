from pymongo import MongoClient
from bson.objectid import ObjectId
import re
from flask import request, jsonify

client = MongoClient('mongodb://localhost:27017/')
db = client["emotional_mirror_db"]
tweets = db["tweets"]

# checking if field exists
##########################
#allTweets = tweets.find({"user.profile_image_loc":{"$exists":True}})
#for a in allTweets:
#    print a

# print regex linked entries
##############################
# regex = re.compile(r'sad')
# results = tweets.find({"text":regex})
# print results.count()
# for p in results:
# 	try:
# 		print p["text"]
# 	except:
# 		print unicode(p["_id"])

# list DBs and drop emotional_mirror_db
##############################
print client.database_names()
client.drop_database("emotional_mirror_db")
print client.database_names()

# list collections + drop tweets
##############################
# print client.emotional_mirror_db.collection_names()
# client.emotional_mirror_db.drop_collection("tweets")
# print client.emotional_mirror_db.collection_names()
