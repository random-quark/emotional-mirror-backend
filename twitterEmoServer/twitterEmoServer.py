from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask import request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask.ext.wtf import Form
from random import randint
from name_form import *
import os
import config

client = MongoClient(config.mongodb_address)
db = client[config.db_name]
tweets = db[config.table_name]

app = Flask(__name__)
app.config['SECRET_KEY'] = config.app_secret_key
Bootstrap(app)
pastResults = []


@app.route('/')
def index():
    return '<h1>Tweet Server is running!</h1>'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    http_call = ''
    randomize_results = False
    query = {}
    if form.validate_on_submit():
        http_call = "http://localhost:5000/search?"
        if form.neg_rel.data:
            query.update({"sentiment.neg":{form.neg_rel.data:form.neg_value.data}})
            http_call += "&neg_rel="+form.neg_rel.data+"&neg_value="+str(form.neg_value.data)
        if form.pos_rel.data:
            query.update({"sentiment.pos":{form.pos_rel.data:form.pos_value.data}})
            http_call += "&pos_rel="+form.pos_rel.data+"&pos_value="+str(form.pos_value.data)
        if form.neu_rel.data:
            query.update({"sentiment.neu":{form.neu_rel.data:form.neu_value.data}})
            http_call += "&neu_rel="+form.neu_rel.data+"&neu_value="+str(form.neu_value.data)
        if form.comp_rel.data:
            query.update({"sentiment.compound":{form.comp_rel.data:form.comp_value.data}})
            http_call += "&comp_rel="+form.comp_rel.data+"&comp_value="+str(form.comp_value.data)
        if form.exclude_past.data:
            query.update({"_id": {"$nin": pastResults}})
            http_call += "&exclude_past="+str(form.exclude_past.data)
        if form.randomize_results.data:
            randomize_results = True
            http_call += "&randomize_results="+str(randomize_results)
        http_call += "&max_results="+str(form.max_results.data)
        #print form.errors

    allTweets = make_query(query, form.max_results.data, randomize_results)
    allTweets = select_fields(allTweets)
    return render_template("form.html", form=form, allTweets=allTweets, http_call=http_call)

@app.route('/search')
def search():
    query = {}
    randomize_results = False
    if request.args.get('neg_rel') and request.args.get('neg_value'):
        query.update({"sentiment.neg":{request.args.get('neg_rel'):float(request.args.get('neg_value'))}})
    if request.args.get('pos_rel') and request.args.get('pos_value'):
        query.update({"sentiment.pos":{request.args.get('pos_rel'):float(request.args.get('pos_value'))}})
    if request.args.get('neu_rel') and request.args.get('neu_value'):
        query.update({"sentiment.neu":{request.args.get('neu_rel'):float(request.args.get('neu_value'))}})
    if request.args.get('comp_rel') and request.args.get('comp_value'):
        query.update({"sentiment.compound":{request.args.get('comp_rel'):float(request.args.get('comp_value'))}})
    if request.args.get('exclude_past'):
        query.update({"_id": {"$nin": pastResults}})
    if request.args.get('randomize_results'):
        randomize_results = True
    max_results = request.args.get('max_results') or 1
    max_results = int(max_results)

    allTweets = make_query(query, max_results, randomize_results)
    allTweets = select_fields(allTweets)
    return jsonify({"tweets": allTweets})


def make_query(query, max_results=0, randomize_results=False):
    # if not enough results left on db, reset pastResults list
    results_available = tweets.count(query)
    if results_available<max_results:
        del pastResults[:]
        query.update({"_id": {"$nin": pastResults}})

    # randomize results
    random_jump = 0
    if randomize_results:
        if max_results <= results_available: #if there are enough results left in database to afford a skip()
            random_jump = randint(0, results_available - max_results)

    # final query - getting actual tweets
    allTweets = tweets.find(query).limit(max_results).skip(random_jump)
    return allTweets

def select_fields(resultList):
    results = []
    for tweet in resultList:
        tempDict = {}
        tempDict["username"] = tweet["user"]["screen_name"]
        tempDict["text"] = tweet["text"]
        tempDict["profile_image"] = os.path.dirname(os.path.realpath(__file__)) + tweet["user"]["local_image_loc"]
        tempDict["location"] = tweet["user"]["location"]
        tempDict["timestamp"] = tweet["created_at"]
        tempDict["sentiment"] = tweet["sentiment"]
        tempDict["mongodb_id"] = str(tweet["_id"])
        pastResults.append(ObjectId(tweet["_id"]))
        results.append(tempDict)
    return results

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
