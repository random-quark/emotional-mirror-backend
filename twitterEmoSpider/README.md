### step 0: getting ready
* Clone or download this repo.
* Go to directory of the repo downloaded and open a terminal there.
* For MAC only: You will need [homebrew](http://brew.sh/). Run the command in the terminal.
* __IMPORTANT:__ make sure the shared variables inside the _config.py_ files of twitterEmoServer and twitterEmoSpider are the same (they are by default).

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
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo easy_install pip
```
then do:
```
sudo pip install virtualenv
```
cd into directory _twitterEmoSpider_ and run:
```
virtualenv venv
source venv/bin/activate
```
setup modules needed:
setup Tweepy ([documentationA](http://www.tweepy.org/), [documentationB](https://github.com/tweepy/tweepy))
```
pip install tweepy
```
setup pymongo
```
pip install pymongo
```

### to run twitterEmoSpider:
Every time you want to start filling up the database with data you need to make sure the database is running by executing:
```
mongod --dbpath ./db --nojournal --smallfiles
```
Edit the ~/.bashrc file and copy paste the following text at the end of the file (after entering the values given to you by Twitter for your App):
```
export CONSUMER_KEY="your_data_here"
export CONSUMER_SECRET="your_data_here"
export ACCESS_TOKEN="your_data_here"
export ACCESS_TOKEN_SECRET="your_data_here"
```
from where your _db_ directory is located. Then cd inside the _twitterEmoSpider_ directory and execute:
```
virtualenv venv
source venv/bin/activate
python twitterEmoSpider.py
```
__Note:__ At the moment the last command should be ran for a little bit only just to get a few data (say 100 or so). Then, open the twitterEmoSpider.py and change the `words_to_track` variable from _sad_ to _happy_. I plan to make this process smarter. For the moment leave it as is.

To drop tables and other db operations see:
```
/utilities/mongoDB_operations.py
```
