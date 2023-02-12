import upload_google_oauth_2
def handle_response(message):

    if message.attachments:
        attachment=message.attachments[0]
        attachment.save("discord_deneme.jpg")
        #upload_google_oauth_2.upload_to_folder(attachment,"1x0c4Os6Yy4ETdOCGubC_mUSuibUVtNHd")
    else:
        return "Yeah I can't understand it"

