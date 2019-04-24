pipenv run /bin/bash -c 'export FLASK_APP=sec_app; flask db upgrade'
pipenv run gunicorn sec_app:app
