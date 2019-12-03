# Songs-api
This project has been made with Django, Django-restframework and Docker. 
It allows client to get information about artists and albums.  

Using a separated container which runs a scrapy process as an API, Django app can recover artist pictures 
from Internet. The pictures are download and path to pictures are added to Django app DB.

**This setup is intended for showcasing and development, you should not use similar configuration on a production enviroment.**

#### TODOs
- <s>Dockerize Django app</s>
- Include more test for music app
- Pagination on listing endpoints
- Recover artist pictures from AllSongs.com
  - <s>Get pictures based on artist name</s>
  - <s>Command to ask django to download pictures and populate DB with artist pictures</s>
  - <s>Add pictures to artist endpoint</s>
  - Check artists results albums againt artist's albums in DB
  - Install async tasks system in order to run this task in background

### Requirements
In order to run this project it is recommend to use Docker and Docker Compose

### Start the app
Start by cloning this repository  and create the necessary images:
```shell script
docker-compose build
```

We are now ready to run our app!
It will start on **localhost:8000**:
```shell script
docker-compose up
```

Ok, app is running at this point. Now, to comunicate with it we could use CURL or [httpie](https://httpie.org/).
```shell script
curl http://localhost:8000/music/artist
```
```shell script
http get http://localhost:8000/music/artist
```

This will return the complete list of artist in DB. This is a open endpoint, 
but how can we comunicate with endpoints that need authentication? We need to create a user beforehand.
Django allows us to create user from the admin app. We can access this part using the next link: http://localhost:8000/admin
In order to access admin console, we will need a superuser, these can be creates using:
```shell script
docker-compose run --rm web ./manage.py createsuperuser
```
After creating a user we can comunicate with private endpoints:
```shell script
http get -a user:password http://localhost:8000/music/artist/1
```

### DB
This repo include DB with data fetched from [here](https://www.sqlitetutorial.net/sqlite-sample-database/).
This way DB is already populated with artists, albums and tracks.

#### How to populate DB with artist pictures
There is a django command to download pictures for all artist from DB:
```shell script
docker-compose run --rm web ./manage.py fetchartistimages --all
> Successfully fetch image for artist 1 > /app/images/AC%20DC.jpg
> Successfully fetch image for artist 2 > /app/images/Accept.jpg
> Successfully fetch image for artist 3 > /app/images/Aerosmith.jpg
> Successfully fetch image for artist 4 > /app/images/Alanis%20Morissette.jpg
> Successfully fetch image for artist 5 > /app/images/Alice%20In%20Chains.jpg
[...]
```

In case we just want to search the pictures for some artist:
```shell script
docker-compose run --rm web ./manage.py fetchartistimages 100
> Successfully fetch image for artist 100 > /app/images/Lenny%20Kravitz.jpg
```

### Test
We can run test by using:
```shell script
docker-compose run --rm web ./manage.py test
```

## API endpoints docs

### Music
#### Public
- GET music/artist: returns a list of all artist in DB.

#### Need Authentication
- GET music/artist/*[artist_id]*: returns a list of albums by artist_id.
- GET music/album: return a list of album with nested list of songs.
- GET music/album/*[album_id]*: returns album  list of songs.
- GET album/*[album_id]*/detail: returns album list of songs with artist info, total
lenght of album and longest and shortest track.

### Passphrase

#### Public
The next endpoints required some RAW body to be send with the POST request

- POST passphrase/basic: return number of passphrases that not contains duplicated words.
- POST passphrase/advance: return number of passphrases that not contains anagrams.

```shell script
cat | http POST http://localhost:8000/passphrase/basic Content-Type:text/plain
> bar foo
> bar foo fooo
> foo foo ko
> joo ojo 
```