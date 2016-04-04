### step 0: getting ready
* Clone or download this repo.
* Go to directory of the repo downloaded and open a terminal there.
* For MAC only: You will need [homebrew](http://brew.sh/). Run the command in the terminal.
* __IMPORTANT:__ make sure the shared variables inside the _config.py_ files of twitterEmoServer and twitterEmoSpider are the same (they are by default). Also make sure in twitterEmoServer you have filled the twitter credentials which you need to have access to the twitter API. See the Tweepy ([documentationA](http://www.tweepy.org/), [documentationB](https://github.com/tweepy/tweepy)) if you need help.

### step 1: setup mongodb + pymongo
__For OSx:__ (more info in [this link](https://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/)):
```
brew install mongodb
```
__For Linux:__
```
sudo apt-get install mongodb-server
```

### step 2: creating database directory
If you want to run it locally then go to the root directory of the two programmes of the repo and run:
```
mkdir db
mongod --dbpath ./db --nojournal --smallfiles
```
else:
```
sudo mkdir /data/
sudo mkdir /data/db/
mongod --dbpath /data/db/ --nojournal --smallfiles
```

### step 3: installing and setting up tools
```
sudo easy_install pip
sudo pip install virtualenv
```
cd into directory _twitterEmoServer_ and run:
```
virtualenv venv
source venv/bin/activate
```
setup modules needed:
```
virtualenv virtualenv
source venv/bin/activate
```
setup Flask and related modules
```
pip install Flask
pip install flask-bootstrap
pip install pymongo
pip install Flask-WTF
```

### run twitterEmoServer:
Every time you want serving data you need to make sure the database is running by executing:
```
mongod --dbpath ./db --nojournal --smallfiles
```
from where your _db_ directory is located. Then cd inside the _twitterEmoServer_ directory and execute:
```
virtualenv venv
source venv/bin/activate
python twitterEmoServer
```
Go to [http://localhost:5000/form](http://localhost:5000/form) and fill out the API form to get the link for the front-end.

To drop tables and other db operations see:
```
/twitterEmoServer/sandbox/mongoDB_operations.py
```

### things to still add/fix
* add exceptions
* add references to [original paper](https://github.com/cjhutto/vaderSentiment)
* make it return a max of 4 tweets and increase a counter for each in the db. Ask for 10, choose random 4 to send, update their counter.
* save in db how many expressions have there been and what type
* replace prepare function in tweetServer with projection: https://docs.mongodb.org/manual/reference/method/db.collection.find/
* possibly better way to randomly pick tweets to return:
  * http://philipp-burckhardt.com/2015/05/16/sampling-from-a-mongodb-database/
  * http://bdadam.com/blog/finding-a-random-document-in-mongodb.html
* if I search for max_results=2 and there's only 1 left it resets the list. it should return that 1 and take whatever is needed from list.
* line for getting latest tweets: lastTweetOnly = posts.find().sort([("created_at", pymongo.DESCENDING)]).limit(1)
* [unicode](https://docs.python.org/2/howto/unicode.html)
* [mongo db queries](https://docs.mongodb.org/manual/reference/operator/query/)
* gunicorn

### good information
* [good tutorial](http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/)
* [online class](https://university.mongodb.com/courses/M101P/about)
