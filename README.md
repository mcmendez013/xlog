# xlog
X log allows you to privately keep track of personal notes, or whatever X maybe. A web based log to access your mind wherever you can find an internet connection.

This project is only tested on an Arch Linux base operating system and runs on a django framework.
This project is setup under a virtual enviornement called, "env1".

Creating a virtual enviornment
terminal:$ pip install --user virtualenv
terminal:$ virtualenv env1 

Virtual Enviornment is now created.

Download files and save to a newly created xlog directory in home folder
From the terminal go into the xlog directory you just created that has the files downloaded in directory.
terminal:$ cd /home/'computers_home_name'/xlog

Now that you are in the  correct terminal with the required files downloaded, we can access the virtual enviornment.
terminal:$ source env1/bin/activate

You are now in a virtual enviornment and are safe to run xlog.
terminal:$ python manage.py runserver

Then type in localhost:8000 into your webrowser and xlog will be up and running.



