sudo docker build -t unitn_mqtt_server .

docker run -it --rm -d -p 8080:80 --name web unitn_mqtt_server

on webbrowser access: http://localhost:8080/

to stop web docker: sudo docker stop web
