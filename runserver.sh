
#!/usr/bin
ps -ef|grep 8000|grep -v grep|awk '{print $2}'|xargs -i kill -9 {}
nohup python manage.py runserver 0.0.0.0:8000 --insecure &
