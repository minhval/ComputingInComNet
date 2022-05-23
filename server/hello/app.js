// var msg = 'Hello World';
// console.log(msg);

const mqtt = require('mqtt')
const client  = mqtt.connect('mqtt://mqtt.eclipseprojects.io')

client.on('connect', function () {
  client.subscribe('unitn/compcomp/gps', function (err) {
    if (!err) {
      // client.publish('unitn/compcomp/gps', 'Hello mqtt')
      console.log("Subscribed!")
    }
  })
})

client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  // client.end()
})
