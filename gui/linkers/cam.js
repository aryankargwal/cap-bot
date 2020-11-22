let {PythonShell} = require('python-shell')
var path = require("path")


function get_frames() {
  
  document.getElementById("session").value

  let pyshell = new PythonShell('cam.py');


  pyshell.on('message', function(message) {
    swal(message);
  })
  document.getElementById("city").value = "";
}