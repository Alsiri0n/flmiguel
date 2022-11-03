import os
from app import app
from config import Config

app.config.from_object(Config)


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)