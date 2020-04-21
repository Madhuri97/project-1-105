TASK-1: Authenticate user and show user home

1. Added login button in Registration.html
2. Written login page as login.html
3. Added routes for authentication, login, and home
4. Validated the page with different error messages 
Time: 5hrs
Problems: 
1. First when i have run my program i got an error like internal server error due to wrong variable name
Fixed:
1. By checking my code and changed the variable name 

TASK-2: Allow authenticated user to home and logout

1. Created a session variable for authenticatio page 
2. Inserted a logout button in login.html
3. Redirected to the login page if the user is authenticated by bypassing the home page
4. By clicking logout the session will be closed and comes to registration page.
Time: 20min
Problems: nothing

TASK-3: Imported Books from csv to database

1. In this i have not used flask python
2. Creadted books_db.py file for the database creation. in this file i have written a constructor for the books database
3. I have created books.py, in this file i have written the code for reading the csv file and updating them into the table. this code is written using sqlalchemy. 
4. Now after executing i have checcked my datbase for the records of books by logging into the Adminer. i found the 5000 records in that table.
Time: 40min
Problems: nothing
