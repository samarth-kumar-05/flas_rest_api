

from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/users"

initialize_db(app)
initialize_routes(api)


app.run(host="0.0.0.0")
