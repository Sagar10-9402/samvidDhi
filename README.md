
#  TA API

## Installation


Clone the repository:
```bash
  git clone https://github.com/Sagar10-9402/samvidDhi.git  
```
  
Install the dependencies:

```
  pip install -r requirements.txt

```

### Set up the MySQL database:

Create a new MySQL database (ta_db).
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
#### we have a multiple endpoints to working api requirements : 

POST / signup : we need the api access so for this access you have to signup first 
```
{
    "username" : "user",
    "password" : "password"
}
```

POST /  login : login in the app and get generated the token
Use the json body for the login 
```
{
    "username" : "user",
    "password" : "password"
}
```

POST /ta: create a new TA record
```
{        
    "native_english_speaker": false,
    "course_instructor": "Rohan",
    "course": "Introduction to Java",
    "semester": 1,
    "class_size": 45,
    "class_attribute": 2
}

```

GET /ta/:id: retrieve a TA record by ID

PUT /ta/:id: update a TA record by ID

DELETE /ta/:id: delete a TA record by ID




#### ** Unittest of the API Development  i attached in the files **

name of the file :
#### Test Endpoints and Test logins 

``` 
  test_routes.py 
  test_logins.py 
```  






