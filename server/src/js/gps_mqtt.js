const mqtt = require('mqtt')
const client = mqtt.connect('mqtt://mqtt.eclipseprojects.io')

SUBSCRIBE_TO_TOPIC = 'unitn/compcomp/gps'

client.on('connect', function () {
  client.subscribe(SUBSCRIBE_TO_TOPIC, function (err) {
    if (!err) {
      // client.publish('unitn/compcomp/gps', 'Hello mqtt')
      console.log("Subscribed to " + SUBSCRIBE_TO_TOPIC + " successfully!")
    }
  })
})

client.on('message', function (topic, message) {
  // message is Buffer
  // localStorage.setItem("data", message); //save data

  console.log("Received from topic " + topic)
  console.log(message.toString())
  console.log() // break down
  // client.end()
})


