FROM python:3

WORKDIR /home/vuanhminhle/Desktop/comp in comm net/source/ComputingInComNet/clients/websocket_client/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "publisher_cars.py" ]
