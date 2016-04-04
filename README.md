## Emotional mirror backend.
The backend is comprised of two parts:
* __twitterEmoSpider:__ which connects to the twitter stream and collects data to build the database.
* __twitterEmoServer:__ Once the database is built, the twitterEmoServer connects to the database and serves data on localhost.

Start by setting up the spider and once the database is somewhat populated setup and run the server.
