# mongodb stuff:
mongodb_address = "mongodb://localhost:27017/"
db_name = "emotional_mirror_db"
table_name = "tweets"

# misc:
profile_dir = "../db/profile_images"
words_to_track = ['sad']

# twitter credentials:
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret=""

# fields to exclude:
tweetfields_exluded = ["source", "in_reply_to_status_id", "in_reply_to_status_id_str", "in_reply_to_user_id", "in_reply_to_user_id_str", "in_reply_to_screen_name", "extended_entities" ]
userfields_exluded = ["url", "protected", "verified", "profile_background_image_url", "profile_background_image_url_https", "profile_background_tile", "profile_background_color", "profile_link_color", "profile_sidebar_border_color", "profile_sidebar_fill_color", "profile_text_color", "profile_use_background_image", "profile_banner_url", "profile_image_url_https", "contributors_enabled", "is_translator", "default_profile"]
