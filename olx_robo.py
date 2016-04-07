#olx_robo

				#1. Connect to gDrive spreadsheets 
""" I was installing pip and PyDrive.
Right now add from pypi.python.org/pypi/PyDrive
1st step - adding OAuth..."""
#!/usr/bin/python

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow


# Copy your credentials from the APIs Console
CLIENT_ID = '599191305513-idtd9kffcn4tncli9rpnag306auej7sf.apps.googleusercontent.com'
CLIENT_SECRET = 'HeqlYjHowwf0DjOgw5yxicxr'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Path to the file to upload
FILENAME = 'document.txt'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE)
authorize_url = flow.step1_get_authorize_url()
print ('Go to the following link in your browser: ' + authorize_url)
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
 'title': 'My document',
 'description': 'A test document',
 'mimeType': 'text/plain'
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)


#RedGreenLight Test
# test = 1 #this var is RedGreenLight

# def RGtest(test):
# 	if test >= 0:
# 		return "Green"
# 	elif test == True:
# 		return "Green"
# 	else:
# 		return Red
# print ("You have %s light" % (RGtest(test)))
#RedGreenLight Test

				#2. Understand which raws I should listen and check; 

				#3. Detect new items 

				#4. If I find new item, I should check am I adding this one in past? 

				#5. If I see this item is brand new, I'm grabbing this data... 

				#6. ... and I go to my canvac (my workspace) and ask it "Hey there. Can I come in?" (log in gDrive for OLX) 

				#7. After successful login I'm creating new product... 

				#8. ... and adding new title inside it... 

				#9. ... and adding new descr... 

				#10. ... and adding new thumbnail... 

				#11. ... and adding new photos... 

				#12. ... and adding new categories or just adding existing category 

				#13. ... and I say:"Yeah, please publish it, love" 

				#14. If all is okey, I start from to-do #1