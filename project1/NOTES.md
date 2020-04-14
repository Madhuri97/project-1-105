TASK-1: Postgresql

1. Visited heroku website and created free account 
2. Now clicked "Create app" gave name as "wp-project1-105"
3. Then opened overview, clicked on "Configure Add-ons" 
4. In Addons searched for "heroku Postgres" after loading clikc over "Provision".
5. Now i had click on heroku Postgres link -- settings -- view credentials 
6. open Adminer link: paste the heroku credentials in this site and don.

TASK-2: Python and FLASK

1. I already had python in my laptop and also had pip installed 
2. Downloaded the project1 zip file to new repo named project-1-105 and branch named starter-code
3. Opened terminal at project1 file location "py -m pip install -r requirements.txt" packages are installed 
4. Set environment by "set FLASK_APP=application.py" -- "set FLASK_DEBUG=1" -- "DATABASE_URL= pasted my postegres uri"
5. Checked for version of Werkzeug if it is 1.0.1 we need to uninstall and reinstall 0.16.0 version according our system. 
6. "py -m pip install Werkzeug==0.16.0"
7. Now "flask run" and copy http link and test over internet