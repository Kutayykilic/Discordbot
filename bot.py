import discord
import responses
import config
import upload_google_oauth_2
import tracemalloc
config_file=config.AppConfig
async def send_message(message,user_message,is_private):
    try:
        response=responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN=config_file.token
    print(TOKEN)
    intents = discord.Intents.default()
    intents.message_content = True
    client=discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f"{client.user} is running!")
    @client.event
    async def on_message(message):
        print(message)
        tracemalloc.start()
        user_message=str(message.content)
        print(user_message)
        user_message=str.split(user_message," ")
        command=user_message[1]
        char_name=user_message[2]
        print(user_message,char_name)
        if command=="!upload" and message.attachments:
            save_name=str(char_name+".jpeg")
            print("here")
            attachment = message.attachments[0]
            await attachment.save(save_name)
            await upload_google_oauth_2.upload_to_folder("1x0c4Os6Yy4ETdOCGubC_mUSuibUVtNHd")

        elif message.content.startswith("!upload"):
             print("yok burada")
             print( "You didn't send an image can you try again?")
        else:
            print("wtf man?")
            return "The message you have sent was completly useless"

       # if message.author == client.user:
        #    return
        #username=str(message.author)
        #user_message=str(message.content)
        #channel=str(message.channel)
        #print(f"{username,user_message,channel}")
        #await send_message("message","selam",is_private=False)
        #user_message=str.split(user_message," ")
        #user_message=user_message[1]
        #if user_message[0]=="!":
         #   user_message=user_message[1:]
           # await send_message(message,user_message,is_private=True)
        #else:
         #   await send_message(message,user_message,is_private=False)




    client.run(TOKEN)