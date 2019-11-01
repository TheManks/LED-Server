import PyCmdMessenger
import random as rand
import subprocess
from pathlib import Path


from flask import Flask, render_template, request
app = Flask(__name__)

port = '/dev/ttyACM'
for i in range(0,5):
    file = Path(port+str(i))
    if file.exists():
        port = port + str(i)
        print("Found open serial port: {}".format(port))
        break

ard = PyCmdMessenger.ArduinoBoard(port, baud_rate=115200)
commands = [["setLed","i"]]
c = PyCmdMessenger.CmdMessenger(ard, commands)

@app.route("/asd")
def hello():
    return "Hello world"
   

@app.route("/")
def json():
    return render_template('json.html')
    
@app.route("/upload_are_we")
def upload_are_we():
    subprocess.run("sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/Development/view-house-lights/are_we", shell=True)
    return "done"

@app.route("/upload_basic_tests")
def upload_basic_tests():
    subprocess.run("sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/Development/view-house-lights/basic_tests", shell=True)
    return "done"

@app.route("/upload_color_tests")
def upload_color_tests():
    subprocess.run("sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/Development/view-house-lights/color_tests", shell=True)
    return "done"

@app.route("/upload_bouncing")
def upload_bouncing():
    subprocess.run("sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/Development/view-house-lights/bouncing", shell=True)
    return "done"

@app.route("/upload_pulsating")
def upload_pulsating():
    subprocess.run("sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/Development/view-house-lights/pulsating", shell=True)
    return "done"

@app.route("/upload_color_pulse")
def upload_color_pulse():
    subprocess.run("sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/Development/view-house-lights/color_pulse", shell=True)
    return "done"

@app.route("/setBrightness")
def setBrightness():
    level = request.args.get("level", rand.randint(0,255))
    c.send("setLed", level)
    return "done"
   
if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8080, debug=True)
