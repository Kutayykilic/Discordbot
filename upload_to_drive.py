import io
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from PIL import Image
from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaFileUpload
# Replace the path with the path to your image file
image_path = 'adultnels2.jpg'

# Load the image using the Pillow library
image = Image.open(image_path)

# Convert the image to a BytesIO object
image_bytes = io.BytesIO()
image.save(image_bytes, format='JPEG')
image_bytes.seek(0)

# Replace the following with your Google Drive API credentials
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'drive-discordbot-7e0009f389fb.json'


credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# Build the Google Drive API client
service = build('drive', 'v3', credentials=credentials)

try:
    # Create the metadata for the file
    file_metadata = {'name': 'image.jpg',"parents":"17B4MAjyZMPT65ep-VYC1JhBKyqRp98ds"}
    media = MediaFileUpload('adultnels2.jpg',
                            mimetype='image/jpeg')
    folder_metadata = {'name': 'Bleach_characters', 'mimeType': 'application/vnd.google-apps.folder'}
    folder = service.files().create(body=folder_metadata, fields='id').execute()
    results = service.files().list(fields="nextPageToken, files(id, name)").execute()
    file_id = '1jtdfnjRJWyq2mwINx23_TgtLvWM0WLqC'
    file = service.files().get(fileId=file_id, fields='webContentLink').execute()
    url = file.get('webContentLink')
    print(F'File URL: {url}')
    permission = {'type': 'anyone', 'role': 'reader'}
    service.permissions().create(fileId=file_id, body=permission).execute()
    items = results.get("files", [])
    for item in items:
        print(F'{item["name"]} ({item["id"]})')
    print(F'Folder ID: {folder.get("id")}')

    # Upload the file to Google Drive
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'File ID: {file.get("id")}')

except HttpError as error:
    print(f'An error occurred: {error}')
