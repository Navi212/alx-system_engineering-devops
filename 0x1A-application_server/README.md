# configure Nginx to serve your page from the route /airbnb-onepage/

server {
        listen  80;
        listen  [::]:80 default_server;

        # Adds customer header for X-Served-By
        # web-01 id
        add_header X-Served-By 208571-web-01;
        root    /var/www/html;
        index   index.html index.htm;

        # Adds location to proxy-request to WSGI gunicorn
        # application server running on localhost port 5000
        location = /airbnb-onepage/ {
                proxy_pass http://127.0.0.1:5000/airbnb-onepage/;
        }

        location /redirect_me {
                return 301 http://www.google.com;
        }

        error_page 404 /404.html;
        location /404.html {
                root /var/www/html;
                internal;
        }
}

