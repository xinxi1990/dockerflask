#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from flask import Flask
# from flask.ext import restful
#
# app = Flask(__name__)
# api = restful.Api(app)
#
# class HelloWorld(restful.Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)


###########################################

"""
$ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo1
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo2 -d "data=Change my brakepads" -X PUT
{"todo2": "Change my brakepads"}
$ curl http://localhost:5000/todo2
{"todo2": "Change my brakepads"}
"""


from flask import Flask, request
from flask.ext.restful import Resource, Api
from flask.ext import restful
from flask.ext.restful import reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}
#
#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}
#
# api.add_resource(TodoSimple, '/<string:todo_id>')


class Todo1(Resource):


    def get(self,todo_id):
        # Default to 200 OK
        return {'task': 'Hello world'}



class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}




class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}



"""
curl http://localhost:5000/
等价
curl http://localhost:5000/hello
"""
api.add_resource(HelloWorld,'/','/hello') #

api.add_resource(Todo1,'/todo/<int:todo_id>', endpoint='todo_ep')
# api.add_resource(Foo, '/foo', endpoint="get_list")

"""
使用endpoint作为参数，则保证了url_for返回确定的 url
flask.url_for需要通过endpoint得到url,可以避免匿名函数的问题
"""

@app.route('/greeting/<name>', endpoint='good')
def give_greeting(name):
    return 'Hello-GOOD, {0}!'.format(name)


@app.route('/greeting/<name>', endpoint='bad')
def give_greeting(name):
    return 'Hello-BAD, {0}!'.format(name)



@app.route('/greeting',methods=['POST'], endpoint='post')
def give_greeting():
    parser = reqparse.RequestParser()
    parser.add_argument('rate', type=int, help='Rate to charge for this resource')
    args = parser.parse_args()
    print(args)
    return 'Hello-Parser'



if __name__ == '__main__':
    app.run(debug=True)


###########################################

