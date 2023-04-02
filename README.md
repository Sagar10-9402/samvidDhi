
## Installation


Clone the repository:
```bash
  https://github.com/Sagar10-9402/samvidDhi.git  
```
  
Install the dependencies:

```
  pip install -r requirements.txt
```

### Set up the MySQL database:

Create a new MySQL database (e.g., ta_db).
Create a new table in the database called TA with the following columns:

```SQL 
  id              INT(11) NOT NULL AUTO_INCREMENT
  native_english_speaker BOOLEAN NOT NULL
  course_instructor VARCHAR(255) NOT NULL
  course          VARCHAR(255) NOT NULL
  semester        BOOLEAN NOT NULL
  class_size      INT(11) NOT NULL
  class_attribute VARCHAR(255) NOT NULL
  PRIMARY KEY     (id)

```

### Set the environment variables:

```JWT_SECRET_KEY: the secret key for JWT token generation and verification
MYSQL_HOST: the host name of the MySQL server
MYSQL_USER: the MySQL username
MYSQL_PASSWORD: the MySQL password
MYSQL_DATABASE: the MySQL database name 
```


## Usage

Start the Flask server:

``` 
  python api.py
```


### Use a tool like curl or Postman to send requests to the API endpoints:

POST /ta:
 create a new TA record

GET /ta/:id: retrieve a TA record by ID

PUT /ta/:id: update a TA record by ID

DELETE /ta/:id: delete a TA record by ID



