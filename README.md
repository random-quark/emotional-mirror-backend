## Emotional mirror backend.
The backend is comprised of two parts:
* __twitterEmoSpider:__ which connects to the twitter stream and collects data to build the database.
* __twitterEmoServer:__ Once the database is built, the twitterEmoServer connects to the database and serves data on localhost.

Start by setting up the spider and once the database is somewhat populated setup and run the server.

## bugs + future features
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
* export CONSUMER_SECRET="123235435"
* print os.environ['CONSUMER_SECRET']

## good sources of information
* [good tutorial](http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/)
* [online class](https://university.mongodb.com/courses/M101P/about)
