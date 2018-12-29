#!/usr/bin/env python3
import subprocess
import time
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    #return "Hello World!"
    return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route("/api/tv/")
def tv():
    return "TV!"


@app.route("/api/tv/power")
def power():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_POWER'])
    return "Power!"


@app.route("/api/tv/volumeup")
def volumeup():
    for index in range(5):
        time.sleep(0.5)
        subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_VOLUMEUP'])
    #subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_VOLUMEUP','KEY_VOLUMEUP','KEY_VOLUMEUP','KEY_VOLUMEUP','KEY_VOLUMEUP'])
    return "volumeup!"


@app.route("/api/tv/volumedown")
def volumedown():
    for index in range(5):
        time.sleep(0.5)
        subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_VOLUMEDOWN'])
    #subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_VOLUMEDOWN','KEY_VOLUMEDOWN','KEY_VOLUMEDOWN','KEY_VOLUMEDOWN','KEY_VOLUMEDOWN'])
    return "volumedown!"


@app.route("/api/tv/mute")
def mute():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_MUTE'])
    return "mute!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')