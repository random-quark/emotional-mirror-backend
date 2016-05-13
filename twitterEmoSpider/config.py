# mongodb stuff:
mongodb_address = "mongodb://localhost:27017/"
db_name = "emotional_mirror_db"
table_name = "tweets"

# misc:
profile_dir = "../db/profile_images"
words_negative = ['angry','depressed','helpless','irritated','lousy','upset','enraged','disappointed','insulting','ashamed','annoyed','embarrassed','upset','guilty','hateful','dissatisfied','unpleasant','miserable','stupefied','detestable','disillusioned','bitter','repugnant','despair','despicable','frustrated','resentful','disgusted','pathetic','infuriated','bad','pessimistic','fuming','indignant','hurt','sad','tearful','terrified','tormented','anxious','anguish','weary','panic','dejected','rejected','desperate','worried','offended','unhappy','frightened','heartbroken','appalled','humiliated']
words_positive = ['happy','great','playful','lucky','amazed','fortunate','optimistic','pleased','delighted','encouraged','overjoyed','gleeful','satisfied','thankful','content','festive','spirited','ecstatic','thrilled','satisfied','wonderful','serene','glad','cheerful','blessed','merry','elated','jubilant','excited','enthusiastic']
words_to_track= words_positive + words_negative
track_keywords = True	# True for keywords, false for random sample from the twitter-sphere

# twitter credentials:
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret=""

# fields to exclude:
tweetfields_exluded = ["source", "in_reply_to_status_id", "in_reply_to_status_id_str", "in_reply_to_user_id", "in_reply_to_user_id_str", "in_reply_to_screen_name", "extended_entities" ]
userfields_exluded = ["url", "protected", "verified", "profile_background_image_url", "profile_background_image_url_https", "profile_background_tile", "profile_background_color", "profile_link_color", "profile_sidebar_border_color", "profile_sidebar_fill_color", "profile_text_color", "profile_use_background_image", "profile_banner_url", "profile_image_url_https", "contributors_enabled", "is_translator", "default_profile"]
