# README

##### Requirements & Installation:

 * Mysql
 * Python 2.7 or higher
 * Run `pip install -r requirements.txt`
 * Change the mysql user and password in `settings.py`

##### How to Run:
 * Create database `artifacia` and run `python manage.py migrate`
 * Import the mysql dump imto your local mysql db. 
 * Run `python manage.py sync_algolia`.
 * Run `python manage.py runserver`
 * You can test it now on `http://localhost:8000/search/`

If something doesn't work as expected then please feel free to contact me.