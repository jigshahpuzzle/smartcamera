import os
import onedrivesdk
from django.conf import settings

BASE_DIR = settings.BASE_DIR # Comment this line out when creating authentication without app running.

'''
Configurations for the Microsoft One Drive API. API tokens are provided for convenient 
recreation of the web server. Please don't abuse the limits on the API. 
'''
redirect_uri = 'https://localhost:8080/'
client_secret = 'MICROSOFT_ONE_DRIVE_CLIENT_SECRET'
client_id='MICROSOFT_ONE_DRIVE_CLIENT_ID'
api_base_url='https://api.onedrive.com/v1.0/'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

http_provider = onedrivesdk.HttpProvider()
auth_provider = onedrivesdk.AuthProvider(
    http_provider=http_provider,
    client_id=client_id,
    scopes=scopes)

'''
Upload a file onto the one drive sdk, loading a user's information  
'''
def uploadFile(directory, filename, local_path):
	client = load_authenticated_session()
	root_folder = client.item(drive='me', id='root').children.get()
	for item in root_folder:
		if item.name == directory:
			fileobj = client.item(drive='me', id=item.id).children[filename]
			returned_item = fileobj.upload(local_path)

'''
Load the pickled credentials for a Microsoft One Drive Account from the application's folder
'''
def load_authenticated_session():
	client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
	client.auth_provider.load_session(path=os.path.join(BASE_DIR, "api/controllers/tmp/onedrive_session.pickle"))
	client.auth_provider.refresh_token()
	return client

'''
Create and pickle credentials for a Microsoft One Drive account. Implements the Oauth2 protocol in a command 
line interface, and saves the refresh token, so no need to reauthenticate the application.
'''
def create_authenticated_session():	
	client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
	auth_url = client.auth_provider.get_auth_url(redirect_uri)
	# Ask for the code
	print('Paste this URL into your browser, approve the app\'s access.')
	print('Copy everything in the address bar after "code=", and paste it below. Put code in quotations.')
	print(auth_url)
	code = input('Paste code here: ')

	client.auth_provider.authenticate(code, redirect_uri, client_secret)
	client.auth_provider.save_session(path='./tmp/onedrive_session.pickle')

'''
Run this executable to generate a credentials file for the application to use. Comment out BASE_DIR 
when running this script.
'''
if __name__ == "__main__": 
	create_authenticated_session()

