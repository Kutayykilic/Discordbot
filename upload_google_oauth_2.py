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
#folder_metadata = {'name': 'Bleach_Characters', 'mimeType': 'application/vnd.google-apps.folder'}
#folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
#print(F'Folder ID: {folder.get("id")}')
file_metadata = {'name': 'image.jpeg', 'mimeType': 'image/jpeg',"parents":"1x0c4Os6Yy4ETdOCGubC_mUSuibUVtNHd"}
media = MediaFileUpload('adultnels2.jpg', mimetype='image/jpeg')
file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
print(F'File ID: {file.get("id")}')
def upload_to_folder(folder_id):
    # Get OAuth 2.0 credentials
    image_path="image.jpeg"
    creds = Credentials.from_authorized_user_file("token.json", scopes=["https://www.googleapis.com/auth/drive"])

    # Build the Drive API client
    service = build("drive", "v3", credentials=creds)

    # Upload the image to the folder
    file_metadata = {
        "name": image_path,
        "parents": [folder_id],
        "mimeType": "image/jpeg"
    }
    media = MediaFileUpload(image_path, mimetype="image/jpeg", resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    print(f"Uploaded image to folder with ID: {file.get('id')}")

if __name__ == "__main__":
    image_path = "adultnels2.jpg"
    folder_id = "your_folder_id"
    upload_to_folder("adultnels2.jpg", "1x0c4Os6Yy4ETdOCGubC_mUSuibUVtNHd")


