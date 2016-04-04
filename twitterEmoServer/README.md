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
