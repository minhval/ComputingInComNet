DEVICES_LIST_UPDATE_INTERVAL = 2000
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
  }
  document.getElementById("gps_device_parsed_array").innerHTML = string_to_print
}
setInterval(printParsedDevicesList, DEVICES_LIST_UPDATE_INTERVAL);