#!/bin/bash
source venv/bin/activate
# flask db upgrade
flask translate compile
exec gunicorn -b ":{$FLASKPORT}" --access-logfile - --error-logfile - run:app
exec rq worker -u $REDIS_URL microblog-tasks