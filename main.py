import flask as flask
from src.schema.manage_authentication.features_blueprint import authentication_blueprint

host = '0.0.0.0'
port = 8080
app = flask.Flask(__name__, static_folder='static/')
app.secret_key = 'authentication_server'
app.debug = True

app.register_blueprint(authentication_blueprint)
if __name__ == "__main__":
    print("Authentication server..")
    app.run(host, port)
