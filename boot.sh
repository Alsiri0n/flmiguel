#!/bin/bash
source venv/bin/activate
# flask db upgrade
flask translate compile
exec gunicorn -b :$flask_port --access-logfile - --error-logfile - run:app
# exec rq worker -u $REDIS_URL/5 microblog-tasks