from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import vaderSentiment
from pymongo import MongoClient
import urllib
import os
import config #from config import * # edit this file with your twitter credentials

# db-related
client = MongoClient(config.mongodb_address)
db = client[config.db_name]
tweets = db[config.table_name]

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

class StdOutListener(StreamListener):
	""" A listener handles tweets that are received from the stream.
	This is a basic listener that just prints received tweets to stdout.
	"""
	def on_data(self, data):
		jData = json.loads(data)
		filteredjData = self.filterStream(jData)
		# if tweet is acceptable (see filterStream for details)
		if filteredjData:
			sentimentScore = self.getSentiment(filteredjData['text'])
			if sentimentScore:
				imagePath = filteredjData["user"]["profile_image_url"]
				imageName = imagePath[imagePath.rfind("/")+1:]
				urllib.urlretrieve(imagePath, config.profile_dir+"/"+imageName)
				filteredjData["user"]["local_image_loc"] = "/"+config.profile_dir+"/"+imageName
				filteredjData["sentiment"] = sentimentScore
				print filteredjData["user"]["screen_name"] + " ===> " + filteredjData['text']
				post_id = tweets.insert_one(filteredjData).inserted_id
				#print post_id
				#json.dump( filteredjData['retweeted'], myfile )
				#myfile.write('\n\n\n')
		else:
			pass
		return True

	def on_error(self, status):
		print(status)

	def getSentiment(self, text):
		#if vaderSentiment.sentiment(text)['neg']>0.3: #let only extreme feelings in
		if True:
			return vaderSentiment.sentiment(text)
		else: return None

	def filterStream(self, t):
		if (t['retweeted'] == False		 						#no retweets
			and 'RT @' not in t['text'] 					#no retweets
			and not t['is_quote_status'] 					#no tweets that are quotes
			and t['in_reply_to_screen_name']==None			#no tweets that are replies
			and not t['entities']['user_mentions']			#no tweets that contain user mentions
			and not t['entities']['urls']					#no tweets that contain url links
			and not t['user']['contributors_enabled']		#no tweets from accounts that have multiple authors (rarely the occasion)
			and 'media' not in t['entities'].keys()			#no tweets that have media (images, videos etc)
			and t['lang']=='en'								#no foreign language tweets
			):
			cleanTweet = {k: v for k, v in t.items() if k not in config.tweetfields_exluded}
			user = t['user']
			cleanUser =  {k: v for k, v in user.items() if k not in config.userfields_exluded}
			cleanTweet['user'] = cleanUser
			return cleanTweet
		else: return None

	def flagFields(self, t):
		for k, v in t.items():
			if v==0: print k, v
			elif v is None: v=None
			elif v==False: print k, v


if __name__ == '__main__':
	if not os.path.exists(config.profile_dir):
		os.makedirs(config.profile_dir)

	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)
	stream.filter(track=config.words_to_track)

#import vaderSentiment
#print vaderSentiment.sentiment("The service here is EXTREMELY good, but the service is horrible.")


	# ###### Is this needed? ######
	# def formatedFields(self, x):
	# 	if x:
	# 		ret = copy.deepcopy(x)
	# 		# Handle dictionaries. Scrub all values
	# 		if isinstance(x, dict):
	# 			for k,v in ret.items():
	# 				ret[k] = scrub(v)
	# 		# Handle None
	# 		if x == 0: ret = 0
	# 		elif x == False: ret = False
	# 		elif t == "null": ret = None
	# 		elif t == None: ret = None
	# 		# Finished scrubbing
	# 		return ret
