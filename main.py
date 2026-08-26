from email import message
from fileinput import filename

import discord
import time
import sys, datetime, os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("TOKEN")
async def dm(usr, msg):
	user = client.get_user(usr)  # Replace user_id with the actual user's ID
	await user.send(msg)

try:
    setmessage = sys.argv[1]
    print("Message recieved from sys")
except:
    setmessage = "`Uh oh there is not a set message yet`"
    print("No message recieved from sys, using default message.")


#setmessage = "`Uh oh there is not a set message yet`"
def log(messg, filename):
    now = datetime.datetime.now()
    logmsg = f"{now} - {messg}\n"
    try:
        # Open the file in append mode
        with open(filename, 'a') as file:
            # Write the log message to the file
            file.write(logmsg)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating new file...")
        # Open the file for the first time
        with open(filename, 'w') as file:
            file.write(logmsg)
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        log(f"{message.author}: {message.content}", "log.txt")
        print(f"{message.author}: {message.content}")
        #for i in range(5):
            #    await message.channel.send(f"@everyone Uh oh someone said cracker! {i}")
        if message.content == ";larp":
            await message.channel.send(" https://klipy.com/gifs/theres-no-limit-to-the-larp-flight")
        if message.content == ";dbgg":
            await message.channel.send("https://klipy.com/gifs/du-bist-gut-genug-2")
        if message.content == ";tenna":
            await message.channel.send("https://tenor.com/iO0cg9xyYGF.gif")
        if message.content == ';spam-brick-wait=1':
            for i in range(100):
                 await message.channel.send('<@1138621441345065060>'); print("spamming w level 1")
                 time.sleep(1)
        elif message.content == ';spam-whatever':
            for i in range(100):
                await message.channel.send('https://tenor.com/view/ai-slop-ai-67-meme-laser-eyes-gif-15578141754060597010'); print("Spamming w level 2")
                time.sleep(0.01)
        if message.content == ";stop":
           await message.channel.send('Okay fine i stop now'); print("stopping bot")
           exit()
        if message.content == ";send-current-set-message":
           await message.channel.send(setmessage); print("set message sent")
        if message.content == ";did-mason-kick-me":
           await message.channel.send("No, mason did not kick me"); print("it appears that i have not been kicked by mason!!!")
        if message.content == ";yttl":
           await message.channel.send("https://tenor.com/view/youre-taking-too-long-jackenstein-deltarune-chapter-4-gif-9089560851254498960"); print("Your taking too long!!")
        if message.content == ";ls":
          await message.channel.send("""=====All Garry text commands=====")
          await message.channel.send(";1984"); - sends the 1984 gif 
          await message.channel.send(";ping"); - pings the bot
         # await message.channel.send(";spam-brick-wait=1"); --purged cmd--
         # await message.channel.send(";spam-whatever");     --purged cmd--
          await message.channel.send(";stop"); - disables the bot
          await message.channel.send(";stfu"); - sends the stfu gif
          await message.channel.send(";did-mason-kick-me"); - sends a message saying mason did not kick the bot
          await message.channel.send(";yttl"); - sends a gif of jackenstein saying "your taking too long" 
          await message.channel.send(";ls") - lists all commands
          await message.channel.send(";dbgg") - sends a gif of du bist gut genug
          await message.channel.send(";send-current-set-message) - sends the current set message
          ===Moderation commands===
          ;log-secret - sends the log file to the user in a dm
          ;log-public - sends the log file to the channel
          ;clean [num messages to delete] - deletes the specified number of messages from the channel
         # ;warn [member] [reason] - sends a DM message to the specified member with a reason --ignore, use sapphire--
          """)
          await message.channel.send("=================================")
        if message.content == ";1984":
           print("literally 1984")
           await message.channel.send("https://tenor.com/view/1984-literally-1984-gif-15073437220075643382")
        if message.content == ";stfu":
           print("stfu")
           await message.channel.send("https://tenor.com/view/stfu-shut-up-shut-the-hell-up-sybau-deltarune-gif-8176397554908480927")
        if message.content == ";ping":
           await message.channel.send("recievedeth"); print("ping")
        if message.content == ";log-public":
            await message.channel.send(file=discord.File("log.txt"))
            await message.channel.send("abc")
        if message.content == ";log-secret":
            #await message.channel.send("abc")
            await message.author.send(file=discord.File("log.txt"))
            await message.author.send("Here is the log file")
            await message.delete()
        if message.content.split()[0] == ";clean":
            try:
                num_messages = int(message.content.split()[1])
                deleted_messages = await message.channel.purge(limit=num_messages)
                #await message.channel.send(f"Deleted {len(deleted_messages)} messages", delete_after=5)
            except (IndexError, ValueError):
                await message.channel.send("Please specify a valid number of messages to delete.", delete_after=5)
            print(f"Deleted {len(deleted_messages)} messages")
        if message.content.split()[0].lower() == ";warn":
            try:
                warned_user = str(message.content.split()[1])
                warning_reason = " ".join(message.content.split()[2:])
            
            
                if not warned_user or not warning_reason:
                    await message.channel.send("Usage: ;warn [user] [reason]", delete_after=3)
                    return
                dm(warned_user,warning_reason)
        
            
                await message.author.send(f"Done! {warned_user} has been warned for: {warning_reason}")
            
                print(f"{warned_user} has been warned for: {warning_reason}")
    
            except (IndexError, ValueError):
                await message.channel.send("Usage: ;warn [user] [reason]", delete_after=3)
"""        if message.content.split()[0] == ";warn":
            try:
                user = str(message.content.split()[1])
                reason = " ".join(message.content.split()[2:])
                await user.send(f"{user}, you have been warned!")
                await user.send(f"You have been warned for: {reason}")
                await message.author.send(f"Done! {user} has been warned for: {reason}")
                print(f"{user} has been warned for: {reason}")
            except (IndexError, ValueError):
                await message.channel.send("Please specify a valid user and reason.", delete_after=5)
"""

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
