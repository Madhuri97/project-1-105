# project-1-105
Task-1: Created registration page using html,css
1. Created a registration form with name, password
2. Used bootstrap properties
3. Applied color to the name section
Time: 15min
Problems: none

Task-2: Added the registration page to flask app
1. Firstly created index.py file to set the FLASK application and added my html page into the templates folder
2. Then added basic route for testing
3. Then added route for my registration page
4. I had set the FLASKAPP "set FLASK_APP=index.py"
5. "set FLASK_DEBUG=1"
6. Now i had run the flask "py -m flask run" it launches a server 
7. Copied the path and tested then i got my registration page.
Time: 40min
Problems: I typed wrong file name after the path.
Fixed: Searched for the name and loaded the page again.

Task-3: Handeled server side requests with flask
1. I added GET,POST methods to my route using requests library
2. Then i had linked the server link the form action
3. I had created a html page for showing the data of the registration form
4. I linked them in a method called result in index.py file 
Reference: https://www.tutorialspoint.com/flask/flask_sending_form_data_to_template.htm
Time:1 hr
Problems: I faced problem in linking the pages.
I typed wrong in the result.html as a Username instead name which i had given in registration
I got an error called template not found because of name of folder template instead templates
Fixed: By typing again after fixing above problems
Searched similar code in the reference link
By giving correct name in method 
