import os
from app import app


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)