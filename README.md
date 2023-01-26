# Mountain_Peak
This project is a simple web service for storing and retrieving mountain peaks. 
It uses the following technologies: SQLAlchemy, SQLModel, Postgres, Alembic and Docker.

The features include:
  - Creating models/database tables for storing peak information such as lat, lon, altitude, and name
  - REST API endpoints for:
    - Creating, reading, updating, and deleting a peak
    

## How to use this project?

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

Get all peaks: 
```sh
$ curl --location --request GET "http://localhost:8004/peaks"
```

Add a peak:

```sh
$ curl -d "{\"lat\": 34.567890, \"lon\": 76.543210, \"altitude\": 3456.7, \"name\": \"Kangchenjunga\"}" -H "Content-Type: application/json" -X POST http://localhost:8004/peak
```

Update a peak:

```sh
$ curl -d "{\"lat\": 45.227173, \"lon\": 121.839455, \"altitude\": 543.2, \"name\": \"Mt. Hood\"}" -H "Content-Type: application/json" -X PUT http://localhost:8004/peak/1
```


Delete a peak:

```sh
$ curl -X DELETE http://localhost:8004/peak/3
```
