import io
from googleapiclient.http import MediaIoBaseDownload
from apiclient import discovery
from apiclient import discovery
from httplib2 import Http
import oauth2client
from oauth2client import file, client, tools

obj = lambda: None
lmao = {"auth_host_name":'localhost', 'noauth_local_webserver':'store_true', 'auth_host_port':[8080, 8090], 'logging_level':'ERROR'}
for k, v in lmao.items():
    setattr(obj, k, v)
    
# authorization boilerplate code
SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
store = file.Storage('token.json')
creds = store.get()
# The following will give you a link if token.json does not exist, the link allows the user to give this app permission
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
    creds = tools.run_flow(flow, store, obj)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))


# listOfFiles = []
# page_token = None
# q = "mimeType='image/jpeg'"

#Get list of jpg files in Drive of authenticated user
# while True:
	# response = DRIVE.files().list(q=q, spaces = "drive", fields = "nextPageToken, files(id, name)", pageToken = page_token, driveId='1DrKx_pWOHKi8QzmqAB8HVZiKsQSosCwl', corpora='drive', includeItemsFromAllDrives=True, supportsAllDrives=True).execute()
	# for file in response.get('files', []):
		# listOfFiles.append(file)

	# print(listOfFiles)
	# page_token = response.get('nextPageToken', None)

	# if page_token is None:
		# break

# while True:
    # response = DRIVE.files().list(q="mimeType='image/jpeg'",
                                          # spaces='drive',
                                          # fields='nextPageToken, files(id, name, folder)',
                                          # pageToken=page_token).execute()
    # for file in response.get('files', []):
        # # Process change
        # print('Found file: %s (%s)' % (file.get('name'), file.get('folder')))
    # page_token = response.get('nextPageToken', None)
    # if page_token is None:
        # break
			
			
# for fileID in listOfFiles:
    # response = service.files().get_media(fileId=fileID['id'])
    # fh = io.FileIO(fileID['name'], 'wb')
    # downloader = MediaIoBaseDownload(fh, response)
    # done = False
# while done is False:
	# status, done = downloader.next_chunk()
	# print("Downloading..." + str(fileID['name']))

# if you get the shareable link, the link contains this id, replace the file_id below
file_id = '0B3e0FtdZKP8vMG9OQlFZOS14c2c'
request = DRIVE.files().get_media(fileId=file_id)
# replace the filename and extension in the first field below
fh = io.FileIO('stage.dat', mode='w')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))
	

	
	