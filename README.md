# README

##### Requirements & Installation:

 * Mysql
 * Python 2.7 or higher
 * Run `pip install -r requirements.txt`
 * Change the mysql user and password in `settings.py`

##### How to Run:
 * Create database `artifacia` and run `python manage.py migrate`
 * Import the mysql dump imto your local mysql db. 
 * The data is already synced but has the mysql id as per my local system. If you wish to sync them according to your local db then run `python manage.py sync_algolia`. It will still work if you don't do this step. Beacuse I have the data on a free server it has limited storage, I request you to tell me once before you do this step so that I can clear the data on the server once. 
 * Run `python manage.py runserver`
 * You can test it now on `http://localhost:8000/search/`

If something doesn't work as expected then please feel free to contact me.