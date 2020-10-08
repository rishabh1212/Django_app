# MoviesAnalyticsApi

## Target

1. Implement API endpoints for below requirements
	- getting a list of movies filterable by a query and
	- details for a specific movie.
	- favorite a specific movie.
	- get a list of favorited movies.

2. APIs to access movies information should be implemented based on API keys

3. APIs related to users movie preferences should be implemented based on user id and password

4. Repeated authentication should be avoided for conveninence

## How To Run

1. Docker compose is used to start a standalone api system with postgresql and django

	- ``docker-compose build && docker-compose up -d``

2. There is admin user, test user and api key created by `populate.sh` for testing
	- ``docker logs movies_app_movies_api_1 | grep admin===>``
	- ``docker logs movies_app_movies_api_1 | grep key===>``
	- ``docker logs movies_app_movies_api_1 | grep testuser===>``

3. It is possible to create new api keys by going to `localhost:8000/admin` and logging in using `admin user`

4. Running the API endpoints

### To access APIs which require ApiKey

#### /movies?search={search}

Get the API_KEY using ``docker logs movies_app_movies_api_1 | grep key===>``

RUN `curl -H "X-API-KEY: API_KEY" localhost:8000/movies_app/movies?search=jurassic`

#### /movie/:id

Get the API_KEY using ``docker logs movies_app_movies_api_1 | grep key===>``
RUN `curl -H "X-API-KEY: hbFnSrd7.tzm08395Gw88AYJYojmhJyNcc2vxXk1e" localhost:8000/movies_app/movie/tt0369610`

### To access APIs which require Login

	1. Set up the login session for the test user

	2. Get test user using `docker logs movies_app_movies_api_1 | grep testuser===>`

	3. To login Run
		- `curl -c cookie.txt localhost:8000/movies_app/login > /dev/null` [This gets the initial csrf token]
		- export csrftoken=$(cat cookie.txt | tail -1 | awk '{print $NF}') [This is used to login using testuser]
		- curl -X POST -c cookie.txt -b cookie.txt -d "username=ris&password=pas&csrfmiddlewaretoken=${csrftoken}" -H "X-CSRFToken:${csrftoken}" localhost:8000/movies_app/login [Post requires CSRF token both in form and header]
		- export csrftoken=$(cat cookie.txt | tail -1 | awk '{print $NF}') [The final logged in csrf]

#### /favorites

This will get present favorties of test user
``curl -c cookie.txt -b cookie.txt localhost:8000/movies_app/favorites``

#### /favorite/:id

This will add Jurrasic movie to favorites
``curl -X POST -c cookie.txt -b cookie.txt -d "csrfmiddlewaretoken=${csrftoken}" -H "X-CSRFToken:${csrftoken}" localhost:8000/movies_app/favorite/tt0369610``

#### Again run /favorites
Check if the favorties list is updated by running 
``curl -c cookie.txt -b cookie.txt localhost:8000/movies_app/favorites``

## Architecture

1. Postgres DB is used to store data, essentially 3 tables of interest - `User`, `movie`, `userfavorites`

2. Django MVC framework is used
	- Views are split into two parts, one containing apis requireing API key and other require user logged in session
	- Filtered IMDB data set is used to populate movies db and two users are created
	- API Key authorization is checked in simple way by validating if header key is actually created and stored in DB [using HasAPIKey class]
	- It is possible to create and invalidate other API keys by logging in admin console at `localhost:8000/admin`
	- Postgresql is prefered over Mysql in case of Django due to less support
	- `movies_api/movies_api` is like wrapper project for the main app `movies_api/movies_app` which contains all api endpoints
	- Blueprint of tables of interest are created in `models.py` with many-many relationship between `User`, `movie`
