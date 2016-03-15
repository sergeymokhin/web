# Nginx
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#Gunicorn
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test.conf
#sudo /etc/init.d/gunicorn restart