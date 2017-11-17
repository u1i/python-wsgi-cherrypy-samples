# Getting started with CherryPy

## 1 - Sample CherryPy app

Files: wsgi.py server.py

Run server: python server.py

Request: curl http://localhost:8080

## 2 - Sample Bottle API app with CherryPy

Files: bottletest.py bottle-server.py

Run server: python bottle-server.py

Request: curl http://localhost:8080/stuff

## 3 - Run app as daemon

Files: app.py srv.ini

Run daemon: cherryd -e production -i app -c srv.ini

Request: curl http://localhost:8080/stuff

### Material:

https://stackoverflow.com/questions/28307981/how-to-launch-a-bottle-application-over-a-cherrypy-standalone-web-server

https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-applications-using-a-cherrypy-web-server-behind-nginx

https://stackoverflow.com/questions/24688032/python-web-server-cherrypy-scaling-concurrent-requests-on-aws
