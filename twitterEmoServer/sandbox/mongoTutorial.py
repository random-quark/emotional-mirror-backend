from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database

buff = '''{"lang": "en", "favorited": false, "sentiment": {"neg": 0.327, "neu": 0.474, "pos": 0.199, "compound": -0.4002}, "entities": {"user_mentions": [], "symbols": [], "hashtags": [], "urls": []}, "contributors": null, "truncated": false, "text": "best weekend ive had in such a long time :( so sad its over", "created_at": "Sun Mar 20 20:20:13 +0000 2016", "retweeted": false, "coordinates": null, "timestamp_ms": "1458505213675", "is_quote_status": false, "place": null, "id_str": "711648562195599361", "filter_level": "low", "retweet_count": 0, "geo": null, "id": 711648562195599361, "favorite_count": 0, "user": {"lang": "en", "created_at": "Fri Apr 17 18:38:09 +0000 2009", "utc_offset": 0, "statuses_count": 31088, "follow_request_sent": null, "friends_count": 532, "time_zone": "Casablanca", "description": "\u2728sparkle", "location": "Reading ", "profile_image_url": "http://pbs.twimg.com/profile_images/694597006229127169/8pke87Nz_normal.jpg", "name": "Party Potts", "notifications": null, "followers_count": 746, "screen_name": "charlieepotterx", "id_str": "32515044", "default_profile_image": false, "following": null, "favourites_count": 6569, "geo_enabled": true, "id": 32515044, "listed_count": 5}}'''
jData = json.loads(buff)

posts = db.posts
post_id = posts.insert_one(jData).inserted_id
print post_id

