sudo docker build -t unitn_mqtt_server .

sudo docker run -it --rm -d -p 8080:80 --name web unitn_mqtt_server

on webbrowser access: http://localhost:8080/

to stop web docker: sudo docker stop web

to push to docker hub:
sudo docker tag TAG_ID minhval0307/unitn_mqtt_server
sudo docker push minhval0307/unitn_mqtt_server

------------------------------------------------------------------------------
sudo docker run -it --rm -d -p 8080:80 --name web minhval0307/unitn_gpstracking_server

on webbrowser access: http://localhost:8080/

sudo docker stop web
