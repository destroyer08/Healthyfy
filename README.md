
Installation:
1. Install all python packages listed in requirement.txt
2. Install node.js and npm for Announce.js (socket.io)
3. Install django-announce client:
  - npm install announce.js
  - node node_modules/announce.js/server.js (server will start on port 6600)
4. Run django server - python manage.py runserver (I have added database file as well so no need to migrate)
5. Add following cron job in unix crontab
*/1 * * * * source /path/to/project/env/bin/activate && python /path/to/project/Healthyfy/Healthyfy/manage.py runcrons 

Usage:
1. To add notification login to /admin/ and in notification model fill the details. (default superuser pratik with paswd pratik)
2. Goto url / and login with user. (default demo with paswd demo) to see notification dashboard.

Documentation:
I have used django-cron for writting a cron class in views.py, everytime we fire manage.py runcrons it runs do function in cron 
class where I am querying notification table for only new notifications by comparing current time.
If I get some notification I execute raw sql query and collect all users and then with help of django-announce client I emit notification_payload.
In dashboard.html with the help of announce.js data is received and I add it to notification div by prepend method.
In dashboard.html {% load announcetags %} and {% announce_js %} take care of notification.

Reference Links:


https://docs.djangoproject.com/en/1.10/ref/validators/
https://github.com/ozkatz/announce.js/blob/master/README.md
https://github.com/ozkatz/django-announce
http://django-cron.readthedocs.io/en/latest/installation.html
Some stackoverflows

