# QuizBuddy
Live project
https://quizzbuddyy.herokuapp.com/

## For local setup run:-
```sh
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## Run tests:-
```sh
python manage.py test
```

## Environment variables:-
* Database
  * DATABASE_URL
* Google authentication
  * GOOGLE_CLIENT_ID
  * GOOGLE_CLIENT_SECRET
* Caching
  * REDIS_URL
## Run in Docker
Follow these instructions to build an image and run a container.
```sh
# Build Docker image
docker-compose build

# Run Docker container in port 8000
docker-compose up
```
