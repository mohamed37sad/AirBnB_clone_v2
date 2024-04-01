#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

fake_html="
<html>
  <head>
  </head>
  <body>
   <h1>Hello world!</h1>
   <h2> This is a test</h2>
  </body>
</html>
"


# Install Nginx if it not already installed 
apt-get -y update
apt-get -y upgrade
apt-get -y install nginx
service nginx start

# # Create the folder /data/web_static/releases/test if it doesn’t already exist
mkdir -p /data/web_static/releases/test/

# Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
printf "%s" "$fake_html" >> /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static 
sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

# Restart Nginx after updating the configuration
service nginx restart
