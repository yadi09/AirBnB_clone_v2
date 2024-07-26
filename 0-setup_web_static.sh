#!/usr/bin/env bash
# Installs configures and starts the web server

if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

echo "<h1>simple content, to test Nginx configuration</h1>" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
    rm -rf /data/web_static/current
fi

ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/server_name _;/a\
\    location /hbnb_static/ {\
\    \    alias /data/web_static/current/;\
\    \	  try_files \$uri \$uri/ =404;\
\    }" /etc/nginx/sites-available/default

if [ "$(pgrep -c nginx)" -le 0 ]; then
    sudo service nginx start
else
    sudo service nginx restart
fi
