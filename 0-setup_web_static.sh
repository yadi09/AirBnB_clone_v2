#!/usr/bin/env bash

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx
    service nginx start
fi

mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
sudo chmod u+w /data/web_static/releases/test/
echo "<h1>simple content, to test Nginx configuration</h1>" > /data/web_static/releases/test/index.html

ln -sf data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sed -i '/server_name _;/a\
\    location /hbnb_static/ {\
\    \    alias /data/web_static/current/;\
\    \	  try_files \$uri \$uri/ =404;\
\    }' /etc/nginx/sites-available/default

if [ "$(pgrep -c nginx)" -le 0 ]; then
    sudo service nginx start
else
    sudo service nginx restart
fi
