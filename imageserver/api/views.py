from django.http import HttpResponse, JsonResponse
from django.views.generic import View
import requests
from controllers import onedrive, cognitive
from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR # Comment this out when running executable w/o application

'''
Tests that GET and POST requests are working successfully on the server
'''
class test(View):

    def get(self, request):
        return HttpResponse("API Endpoint Successfully Hit")

    def post(self, request):
        return HttpResponse("API Endpoint Successfully Hit")

'''
Basic display text for the home page.
'''
class home(View):
    def get(self, request):
        return HttpResponse("Welcome to Jigar's Digital Fabrication Final Project. Make a post to /api/test and /api/upload to try out the server. Please don't abuse uploads because it adds a file to my OneDrive account :)")


'''
Description: 
	API call in order to upload an image to a user's account
Request Parameters: 
	{image : [File Stream]}
Response Object:
	{"Response" : "File Successfully Uploaded", "Status" : 200, "Data" : Image Name}
'''
class uploadImage(View):

	def post(self, request):
		imageFile = request.FILES.get('image')
		data = imageFile.read()
		name = cognitive.getImageName(data)
		f = open(os.path.join(BASE_DIR, 'api/controllers/tmp/image'), 'w')
		f.write(data)
		f.close()
		onedrive.uploadFile('Pictures', name, os.path.join(BASE_DIR, 'api/controllers/tmp/image'))
		return JsonResponse({"Response" : "File Successfully Uploaded", "Status" : "200", "Data" : name})


'''
Executable to test uploading a photo to the web server. Make sure to comment BASE_DIR first, and 
ensure that files that the server is running is separate from the one running the script.
'''
if __name__ == '__main__':
	f = open('./controllers/tmp/trial.jpg')
	requests.get('localhost:8000/api/upload/', files={'image' : f})


