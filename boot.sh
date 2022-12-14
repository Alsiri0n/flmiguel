#!/bin/bash
exec ./venv/bin/rq worker -u $REDIS_URL microblog-tasks &
source venv/bin/activate
# flask db upgrade
flask translate compile
exec gunicorn -b :$flask_port --access-logfile - --error-logfile - run:app
