# 0x1A. Application server

Task is to add application server to infrastructure, plug into Nginx, and serve Airbnb Clone projecct.

# Background Context


Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

Resources

+ Application server vs web server
+ How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
Running Gunicorn
+ Be careful with the way Flask manages slash in route - strict_slashes
+ Upstart documentation

## Requirements
General
+ A README.md file, at the root of the folder of the project, is mandatory
+ Everything Python-related must be done using python3
+ All config files must have comments

## Bash Scripts
+ All your files will be interpreted on Ubuntu 16.04 LTS
+ All your files should end with a new line
+ All your Bash script files must be executable
+ Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
+ The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
+ The second line of all your Bash scripts should be a comment explaining what is the script doing


Example:

Window 1:
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
Window 2:
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
