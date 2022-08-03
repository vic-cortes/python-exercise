from flask import Flask

from app.config import Config


app = Flask(Config.APP_NAME)

from app.api import blueprint

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)