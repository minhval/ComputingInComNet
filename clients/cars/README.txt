sudo docker build -t publisher_cars .

sudo docker run -it --rm --name cars publisher_cars

docker pull minhval0307/publisher_cars:latest
