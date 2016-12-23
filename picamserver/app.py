from flask import Flask
from picamera import PiCamera
import requests

'''
This web server is to be run on a Raspberry Pi. To run the server, ssh into your Raspberry Pi module,
install Apache, and start an Apache Web Server running an instance of the Flask Application. 
'''
app = Flask(__name__)

'''
Home page for the PiCamera Webserver
'''
@app.route('/')
def main():
	return "Welcome. Your PiCam Server is working. Try /api/capture in order to take a picture"

'''
Uses the PiCamera to capture a picture of what it is currently pointed at, and uploads the picture to 
the digfabserver for processing. 
'''
@app.route('/api/capture')
def capture(): 
	camera = PiCamera()
	camera.start_preview()
	camera.capture('/home/pi/Desktop/image.jpg')
	camera.stop_preview()
	f = open('/home/pi/Desktop/image.jpg')
	requests.post('___imageserver_url___/api/upload/', files={'image' : f})
	f.close()
	return "Image Successfully Captured"


if __name__ == "__main__":
	app.run()
