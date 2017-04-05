
fuser -k 80/tcp
fuser -k 9090/tcp
uwsgi --ini /etc/uwsgi9090.ini -d /weixin/wechat/uwsgi9090.log & /usr/local/nginx-1.5.6/sbin/nginx
