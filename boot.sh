#!/bin/bash
source venv/bin/activate
# flask db upgrade
flask translate compile
exec gunicorn -b :5050 --access-logfile - --error-logfile - run:app
exec venv/bin/rq worker -u $REDIS_URL microblog-tasks