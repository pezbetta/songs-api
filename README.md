#Readme

## TODOs
- Dockerize django service
- Use PostgreSql with docker compose
- 

### Requirements

For running this project it is recommend to use Docker and Docker Compose

### Start the app

## API endpoints docs

### Music
#### Public
- GET music/artist/ returns a list of all artist in DB.

#### Need Authentication
- GET music/artist/[artist_id] returns a list of albums by artist_id.
- GET music/album return a list of album with nested list of songs.
- GET music/album/[album_id] returns album  list of songs.
- GET album/[album_id]/detail returns album list of songs with artist info, total
lenght of album, longest and shortest track.

### Passphrase

#### Public
The next endpoints required some RAW body to be send with the POST request

- POST passphrase/basic 
- POST passphrase/advance