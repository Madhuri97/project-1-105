TASK-1: Postgresql

1. Visited heroku website https://www.heroku.com/ and created free account 
2. Now clicked "Create app" gave name as "wp-project1-105"
3. Then opened overview, clicked on "Configure Add-ons" 
4. In Addons searched for "heroku Postgres" after loading clikc over "Provision".
5. Now i had click on heroku Postgres link -- settings -- view credentials 
6. open Adminer link: paste the heroku credentials in this site and don.
7. time: 10min

TASK-2: Python and FLASK

1. I already had python in my laptop and also had pip installed 
2. Downloaded the project1 zip file to new repo named project-1-105 and branch named starter-code
3. Opened terminal at project1 file location "py -m pip install -r requirements.txt" packages are installed 
4. Set environment by "set FLASK_APP=application.py" -- "set FLASK_DEBUG=1" -- "DATABASE_URL= pasted my postegres uri"
5. Checked for version of Werkzeug if it is 1.0.1 we need to uninstall and reinstall 0.16.0 version according our system. 
6. "py -m pip install Werkzeug==0.16.0"
7. Now "flask run" and copy http link and test over internet
8. time: 30min
9.  problems faced: i had a problem using the command: "pip install -r requirements.txt". 
    I also faced problem with Werckaeug installation of another version whereas i had got 1.0.1 version instead 0.16.0 
    Direct pip install command is not recognized in my command prompt
10. fixed: 
    The 9th problem is fixed by adding "py -m" to the command then it got installed, 
    I had uninstalled old werckzeug version installed the required version 

TASK-3: Goodreads API
1. Visited link and created my account using google account
2. Navigated through apply for API link filled the name of app "wp-project1-105" and got key
3. Copied the code given in doc and pasted in project1 goodr.py and pasted that key in the place of KEY in the py file
4. I need to install requests first to run this "py -m pip install requests"
5. Now executed goodr.py file "py goodr.py" and got some books
6. time: 15min
7. problems faced: i had problem in running the goodr.py file because we did not installed requests module for accepting key
8. fixed: by installing requests module i had sucessfully executed my file using given api key.