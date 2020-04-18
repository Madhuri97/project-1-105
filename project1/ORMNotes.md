Task-1: Create a database table
1. Added email field to registration.html file
2. Written Schema.py created class schema for the creation of database 
3. Initiated basic constructor for the variables name, email and password
4. Assigned primary keys for the variable which should be unique like name, emailid and password is nullable because there sholud be enter something.
5. Fixed environment for database using getnv, created configuration session and set up the database
6. By setting heroku URI to database i executed
7. opened heroku and checked whether the table is created or not and went to data clips by writing query i got the display of data entered into the form.
Time: 5hrs
Reference:https://hackersandslackers.com/flask-sqlalchemy-database-models/
Problems: connecting application.py to Schema.py
fixed: by giving proper names and cheacked the sequence of lines.

Task-2:  Insert records

1. Added Alerts implementation in the Registration.html for proper creation of user 
2. In application.py i have added two messages for the proper creation and an error message if the user already exists or user entered any wrong message
3. I have created objects in registration form and assigned in application.py for the messages 
Time: 30min
Problems: the wrong symbol over alert is not worked 
Fixed: added scripts to the registration file.