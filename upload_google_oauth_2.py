from google.oauth2.credentials import Credentials
import io
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from PIL import Image
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
import json
with open("token.json", "r") as f:
    user_info = json.load(f)
creds = Credentials.from_authorized_user_info(info=user_info, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=creds)


def upload_image():
    file_metadata = {'name': 'image.jpeg', 'mimeType': 'image/jpeg'}
    media = MediaFileUpload('adultnels2.jpg', mimetype='image/jpeg')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(F'File ID: {file.get("id")}')


if __name=="main"