#!/usr/bin/python
import redis
from flask import Flask, jsonify, request
# redis config
## update host and port and redis_key if required
r = redis.Redis(host='127.0.0.1',port=6379)

redis_key='test'

app = Flask(__name__)

#Homepage endpoint
@app.route('/', methods = ['GET'])
def home():
    return "Home Page!! Add word or Autocomplete can be performed "

#Add_word endpoint
@app.route('/add_word/word=<word>', methods = ['GET'])
def add_word(word):
    dic={}
    dic[word]=1
    r.zadd(redis_key,dic)
    return f"{word} is word added"

#Autocomplete endpoint for a valid query
@app.route('/autocomplete/query=<query>', methods = ['GET'])
def autocomplete(query):
    redis_start='['+query #query start point
    redis_end='('+query[:-1]+ chr(ord(query[-1])+1) #query end point
    data=r.zrangebylex(redis_key,redis_start,redis_end)
    response=[]
    for i in data:
        response.append(i.decode())
    return response

#Autocomplete endpoint if query is empty
@app.route('/autocomplete/query=', methods = ['GET'])
def default():
    data=r.zrange(redis_key,0,-1)
    response=[]
    for i in data:
        response.append(i.decode())
    return response

@app.errorhandler(404)
def notfound(e):
    return "Error 404 occured"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
