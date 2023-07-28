#!/usr/bin/env bash
# sets up your web servers for the deployment

echo -e "Updating and doing some checks...\n"

# install nginx if not present
if [ ! -x /usr/sbin/nginx ]; then 
	sudo apt-get update -y -qq && \
		sudo apt-get install -y nginx
fi

echo -e "\nSetting up some minor stuff.\n"

# creating directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

# creating index.html for sample text
echo "<h1>Welcome to kouts.tech website <\h1>" | sudo dd status=none of=/data/web_static/releases/test/index.html

# creating a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# giving user ownership to directory
sudo chown -R ubuntu:ubuntu /data/

# backup default server configuration file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

# Set-up the content of /data/web_static/current/ to redirect
# to domain.tech/hbnb_static
sudo sed -i '37i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart

echo -e "Completed"
