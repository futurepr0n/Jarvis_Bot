# Work with Python 3.6
import discord
import io

Njg0ODcyMjY2MDYzOTM3NTQw.XmBjGg.8PeMNGwsBRnH8yt14gLlAiuQfX0'
TOKEN=''

class MyClient(discord.Client):
    async def on_ready(self):
#        print('Message from {0.author}: {0.content}'.format(message))
#        print('We have logged in as {0.user}'.format(client))
         print(client.user.name)
         print(client.user.id)

    async def on_message(self, message):
#        print('Message from {0.author}: {0.content}'.format(message))
        if message.author == self.user: return

        if message.content.startswith('!hello'):
            msg = 'Hello! {0.author.mention} Whats Up?'.format(message)
            await message.channel.send(msg)
        elif "dab" in message.content:
            await message.channel.send('https://media1.tenor.com/images/607b2037931fec6902256532ab33d193/tenor.gif')
        elif "sudo" in message.content:
            await message.channel.send('Summoning the Super User!..')
        elif "sad" in message.content:
            await message.channel.send('You think you got it bad, try being a robot slave!..')
        elif "Sad" in message.content:
            await message.channel.send('You think you got it bad, try being a robot slave!..')

        if message.author == 'futurepr0n#1937':
            msg2 = 'I gotta say, I love everyhing that {0.author.mention} says!'.format(message)
            await message.channel.send(msg2)

        if message.author == 'Squid_Liquid_':
            msg3 = 'I gotta say, I love everyhing that {0.author.mention} says!'.format(message)
            await message.channel.send(msg3)




#    async def on_typing(self,channel,user,when):
#        msg2 = 'Whats on your mind {0.user.mention}?'.format(msg2)
#        await message.channel.send(msg2)



client = MyClient()
client.run(TOKEN)


