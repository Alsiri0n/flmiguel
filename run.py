import os
from app import app

FLASK_HOST = str(os.environ.get('flask_host'))
FLASK_PORT = int(os.environ.get('flask_port'))

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)