#!/usr/bin/env bash
<<<<<<< HEAD
# sets up the web servers for the deployment of web_static

=======
<<<<<<< HEAD
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '11i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start

=======
# sets up your web servers for the deployment of web_static
>>>>>>> 830f3165d26ad344d8816074a4a526094e54309c
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
<<<<<<< HEAD
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '11i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
=======
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/listen 80 default_server;/a location /hbnb_static {\\n\\talias /data/web_static/current/;\\n\\t}\\n" /etc/nginx/sites-available/default
sudo service nginx restart
>>>>>>> 1aa7c1466d9987c8ee2e2d156b5bb710c6c822b1
>>>>>>> 830f3165d26ad344d8816074a4a526094e54309c
