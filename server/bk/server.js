const mqtt = require("mqtt")
const brokerURL = 'mqtt.eclipseprojects.io';
const client = mqtt.connect(brokerURL, 1883, 60);
client.on('connect', function () {
    client.subscribe('unitn/compcomp/gps', function (err) {
        if (!err) {
            console.log("Connection to MQTT broker successful!");
        } else {
            console.log("MQTT connection error!");
        }
    })
})

client.on('message', function (topic, message) {
    console.log("Data received: " + message.toString());

    const obj = JSON.parse(message.toString());
    console.log('Application ID:' + obj);
})

app.listen(3000);