# Security for a bank storage

You can check who is inside of storage now, who has access and information about each visit of each person. 

### How to install

* Check that you have Python 3  
* Install requirements:  
```sh
$ pip install -r requirements.txt
```
* How to start security service
```sh
python manage.py runserver
```
After that you can go by link 127.0.0.1:8000, and you will see service in your browser.

### Environment variables  
Some part of settings is from environment variables. You should make file `.env` near `manage.py` and write there: `VARIABLE=value`.  
Variables:  
- `DEBUG` - debug-mode. Put `True` to see debug information in error case. Turn off with value `False`.  
- `SECRET_KEY` - secret key of project. For example: `blablabla`.  
- `USER` - write your login.  
- `PASSWORD` - write your password.  

### Purpose

Code was writing for learning purpose as a part of course for web-developers [dvmn.org](https://dvmn.org/).