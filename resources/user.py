from flask import request
from database.db import mongo
from flask_restful import Resource,reqparse

import json
from bson import json_util
from bson.objectid import ObjectId

user_post_parse = reqparse.RequestParser()
user_post_parse.add_argument("name",type=str,required=True,help="enter user name")
user_post_parse.add_argument("email",type=str,required=True,help="enter user email")
user_post_parse.add_argument("password",type=str,required=True,help="enter user password")

user_put_parse = reqparse.RequestParser()
user_put_parse.add_argument("name",type=str,required=True,help="enter user name")
user_put_parse.add_argument("email",type=str,required=True,help="enter user email")
user_put_parse.add_argument("password",type=str,required=True,help="enter user password")


class UsersApi(Resource):
    def get(self):
        users = mongo.db.Users.find()

        details_dicts = [userr for userr in users]
        details_json_string = json.dumps(details_dicts,default=json_util.default)
        return json.loads(details_json_string)


    def post(self):
        args = user_post_parse.parse_args()

        _name = args['name']
        _email = args['email']
        _password = args['password']

        if _name and _password and _email and request.method == 'POST':

            id = mongo.db.Users.insert_one({'name':_name,'email':_email,'password':_password})
            return "User added successfully",200


class UserApi(Resource):
    def get(self,id):
        user = mongo.db.Users.find_one({"_id":ObjectId(id)})
        user_json_string = json.dumps(user,default=json_util.default)
        return json.loads(user_json_string)
        

    def put(self, id):
        _id = id
        args = user_put_parse.parse_args()
        _name = args['name']
        _email = args['email']
        _password = args['password']
 
        if _name and _email and _password and _id and request.method == "PUT":

            mongo.db.Users.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set':{'name':_name,'email':_email,'password:':_password}})
 
            return "User updated successfully",200
 
        else:
 
            return "User not found"

    def delete(self, id):
        mongo.db.Users.delete_one({'_id':ObjectId(id)})
        return 'User deleted Successfully', 200
