DEVICES_LIST_UPDATE_INTERVAL = 1000
let BREAK_DOWN = "</br>"

function updateDevicesList() {
  while (current_gps_data_array.length != 0) {
    gps_element = current_gps_data_array.pop() // get last element
    parsed_gps_element = JSON.parse(gps_element)
    device_id = parsed_gps_element["device_id"]

    if (!(device_id in latest_updated_gps_devices)) {
      latest_updated_gps_devices[device_id] = ""
      console.log(device_id + " not in the list")
    }
    else {
      console.log(device_id + " in the list")
    }
    // update value
    latest_updated_gps_devices[device_id] = parsed_gps_element
  }
}
setInterval(updateDevicesList, DEVICES_LIST_UPDATE_INTERVAL);

function printDevicesList() {
  copied_dev_ls = Object.assign({}, latest_updated_gps_devices); // shallow copy
  document.getElementById("gps_device_array").innerHTML = JSON.stringify(copied_dev_ls);
}
setInterval(printDevicesList, DEVICES_LIST_UPDATE_INTERVAL);

function printParsedDevicesList() {
  copied_dev_ls = Object.assign({}, latest_updated_gps_devices); // shallow copy - dictionary object

  id_list = Object.keys(copied_dev_ls)

  string_to_print = ""

  var canvas = document.querySelector('#my-canvas');
  var context = canvas.getContext('2d');
  context.clearRect(0, 0, canvas.width, canvas.height); // clear the canvas

  function drawPoint(context, x, y, label, color, size) {
    if (color == null) {
      color = '#000';
    }
    if (size == null) {
      size = 5;
    }

    var radius = 0.5 * size;

    // to increase smoothing for numbers with decimal part
    var pointX = Math.round(x - radius);
    var pointY = Math.round(y - radius);

    context.beginPath();
    context.fillStyle = color;
    context.fillRect(pointX, pointY, size, size);
    context.fill();

    if (label) {
      var textX = Math.round(x);
      var textY = Math.round(pointY - 5);

      context.font = 'Italic 14px Arial';
      context.fillStyle = color;
      context.textAlign = 'center';
      context.fillText(label, textX, textY);
    }
  }

  while (id_list.length != 0) {
    id = id_list.pop()
    element = latest_updated_gps_devices[id]

    string_to_print += JSON.stringify(id) + BREAK_DOWN
    string_to_print += element["device_type"] + BREAK_DOWN
    string_to_print += element["datetime"] + BREAK_DOWN
    string_to_print += element["gps_latitude"] + BREAK_DOWN
    string_to_print += element["gps_longitude"] + BREAK_DOWN

    string_to_print += BREAK_DOWN
    // string_to_print = string_to_print + JSON.stringify(element) + BREAK_DOWN + BREAK_DOWN

    // draw a point on canvas
    drawPoint(context, element["gps_latitude"], element["gps_longitude"], id, 'red', 3);
  }
  document.getElementById("gps_device_parsed_array").innerHTML = string_to_print
}
setInterval(printParsedDevicesList, DEVICES_LIST_UPDATE_INTERVAL);