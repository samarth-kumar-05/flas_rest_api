# flask_rest_api

This is CRUD API build using Flask and MongoDb as database

First install all the requiremnts from requirements.txt files :

    1)  cd to the directory where requirements.txt is located
    2)  activate your virtualenv
    3)  run: pip install -r requirements.txt in your shell
    
   Now start the API using :  python app.py
   
   The application have the following REST API endpoints:
     1) GET /users - Returns a list of all users.
     2) GET /users/<id> - Returns the user with the specified ID.
     3) POST /users - Creates a new user with the specified data.
     4) PUT /users/<id> - Updates the user with the specified ID with the new data.
     5) DELETE /users/<id> - Deletes the user with the specified ID.


The postman testing screenshots have been added in this repo in the screenshots folder
