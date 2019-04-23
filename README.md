# The Night King's Itinerary

## A UF SEC Flask Example

### Dependencies
```
pip install pipenv
```

### Flask Migrate Setup
```
# Initialize Flask Migrate
pipenv run /bin/bash -c 'FLASK_APP=sec_app flask db init'

# Create a migration
pipenv run /bin/bash -c 'FLASK_APP=sec_app/ flask db migrate'
```

### Running
```
pipenv install # to update the Python packages
pipenv run run.sh
```

The API will be available at `localhost:8000/api/v1/`, and the Swagger docs will be available at `localhost:8000/api/v1/apidocs`


### Run Tests
```
pipenv run launch_tests.sh
```
