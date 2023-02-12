import io
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from PIL import Image
from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaFileUpload
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'drive-discordbot-7e0009f389fb.json'


credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)
results = drive_service.files().list(fields="nextPageToken, files(id, name)").execute()
items = results.get("files", [])
ids=[]
for item in items:
    print(F'{item["name"]} ({item["id"]})')
    ids.append(item["id"])
for i in ids:
    permission = {'type': 'anyone', 'role': 'reader'}
    drive_service.permissions().create(fileId=i, body=permission).execute()
# Replace the following with your Google Drive API credentials

