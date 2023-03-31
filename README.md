TA API Development 

This is an API for managing TA (Teaching Assistant) data, implemented using Flask and MySQL. It supports the following CRUD operations:

Create a TA record
Retrieve a TA record by ID
Update a TA record by ID
Delete a TA record by ID


Clone the repository:
```https://github.com/Sagar10-9402/samvidDhi.git```

Install the dependencies:
`pip install -r requirements.txt'

Set up the MySQL database:
Create a new MySQL database (e.g., ta_db).
Create a new table in the database called TA with the following columns:

'id              INT(11) NOT NULL AUTO_INCREMENT
native_english_speaker BOOLEAN NOT NULL
course_instructor VARCHAR(255) NOT NULL
course          VARCHAR(255) NOT NULL
semester        BOOLEAN NOT NULL
class_size      INT(11) NOT NULL
class_attribute VARCHAR(255) NOT NULL
PRIMARY KEY     (id)'

