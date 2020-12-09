from flask import Flask
from flask import request
from flask import render_template ,jsonify
from flask_cors import CORS
import pymongo

app=Flask(__name__)
CORS(app)

myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['test']
mycollection=mydb['blog']

@app.route('/')
def home():
    print('home router called')
    return render_template('home.html')

@app.route('/administer',methods=['GET','POST','DELETE'])
def administer():
    if request.method=='GET':
        return  render_template('administer.html',test='test')
    elif request.method=='POST':
        return 'administer posted'
    else:
        return 'administer delete'

@app.route('/administer_data')
def data():

    return {'greeting':'greeting from flask'}

@app.route('/blog')
def blog():
    bloglist=[]
    for blog in mycollection.find({"type" : "blog"}):
        print(blog)
        bloglist.append(blog)
    print(bloglist)
    return  render_template('blog.html',
                                normaldata='normal data',
                                list=[{"context":'blog1'}],
                                blog=bloglist,
                            )

@app.route('/recommendation',methods=['GET','POST'])
def recommenddation():
    if request.method=='GET':
        return  render_template('recommendation.html')
    else:
        return 'recommendation posted'




# @app.route('/index')
# def index():
#     return 'index'
# """send hello_world() into app function ,hello_world became a new fuction"""
#
# @app.route('/user/<username>')
# def user(username):
#     return "welcome %s" % username
#
# '''the methods allowed.why no hint in pycharm???'''
# @app.route('/login/<username>',methods=['GET','POST'])
# def login(username):
#     print(request)
#     if request.method =='POST':
#         return 'LOGIN POST USERNAME:%s' % username
#     else:
#         return render_template('login.html',username=username)