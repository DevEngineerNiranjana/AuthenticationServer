# AuthenticationServer
IDE used: Pycharm

python version: 3.8

The host and port is set as local in main.py

Use mongo DB as database: In src/common/constants.py the mongo client is initialized please change the client connection to yours if necessary.

Use Postman to hit the APIs and see the output

There are 3 APIS :

    /generate_token : to generate a JWT token with payloads username, password and first_name
   
    /login : to login, Verifies the username and password. both username and email id can be used to login.
    
    /register : to register a new user, checks whether the user already exists, checks the password strength, username, email and password are mandatory fields.

First run the main.py file to up the server.

Run the mongodb if using local.

From postman first register a user then generate the token and login using the token.



