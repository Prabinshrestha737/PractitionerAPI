
## Prerequisites

- Python 3+
- Django Framework
- Django Rest Framework
- Postgres Database
- Postman (optional, for testing API endpoints)

## Setup

1. Clone the repository:

https://github.com/Prabinshrestha737/PractitionerAPI




## Environment Variables

Create .env file inside your main project 
and set up accordingly. Generate SECRET_KEY

```
  SECRET_KEY=<your_secret_key>
  DB_NAME=<your_database_name>
  DB_USER=<your_database_user>
  DB_PASSWORD=<your_database_password>
  DB_HOST=<your_database_host>
  DB_PORT=<your_database_port>
```
## Installation

Install required dependencies

```
  pip install -r requirements.txt

```


## Make migrations and migrate


```
  python manage.py makemigrations
  python manage.py migrate
```

## start the server 
Start the server 

```
 python manage.py runserver
```

## API Endpoints

The following API endpoints are available:

- `GET /api/practitioners/`: Retrieve list of all practitioners.
- `POST /api/practitioners/`: Create a new practitioner along with qualifications and communications.
- `GET /api/practitioners/<id>/`: Retrieve details of a specific practitioner.



## API Reference

#### Get all practitioners

```http
  GET /api/practitioners/
```

#### Get practitioners

```http
  GET /api/practitioners/{id}
```

#### Create practitioners

```http
  POST /api/practitioners/
```


## JSON format

```json
Create a new practitioner:

- Method: POST
- URL: `http://localhost:8000/api/practitioners/`
- Headers: Content-Type: application/json

  {
  "active": true,
  "name": "Prabin",
  "telecom": "prabin@gmail.com",
  "address": "Kathmandu",
  "gender": "male",
  "birth_date": "1990-01-01",
  "qualifications": [
    {
      "code": "BACHELOR",
      "period_start": "2016-01-01",
      "period_end": "2020-10-10",
      "issuer": "TU"
    }
  ],
  "communications": [
    {
      "language": "English",
      "preferred": true
    },
    {
      "language": "Chinese",
      "preferred": false
    }
  ]
}

  ```

