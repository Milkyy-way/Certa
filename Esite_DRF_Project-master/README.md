# Esite_DRF_Project

Follow below steps to start the project
1)Run below command to run the virtual server 
venv\Script\activate.bat
2)to install all the dependency run below command
pip install -r backend/requirements.txt
3)To login you need to create superuser, go to backend dir. User below command (if you don’t want to create then skip this step and go to step 4)
python manage.py createsuperuser
give username, skip email address, give password.
4)go to backend dir and run below command to start server
python manage.py runserver
5)Go to Browser and hit http://localhost:8000/admin/ (if you did not created superuser then use below credentials otherwise use your credentials)
Username: first
Password: abc123!@#
