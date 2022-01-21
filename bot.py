from dis import disco
import discord
from discord.ext import tasks
import datetime
from dotenv import load_dotenv
from teehee import *
import os

client = discord.Client()   
load_dotenv()

def findTimeDif(endTime):
    now = datetime.datetime.now()
    print(now)
    timeLeft = endTime - now
    days = timeLeft.days
    hours = timeLeft.seconds // 3600
    minutes = (timeLeft.seconds // 60) % 60
    return(str(days) + ' days, ' + str(hours) + ' hours, ' + str(minutes) + ' minutes')

def composeEmbed(titleCon, urlCon, dueDate, timeLeft, handoutLink, gearupLink):
    embeded = discord.Embed(title=titleCon, url=urlCon, description=dueDate + '\n' + timeLeft, color=discord.Color.green())
    embeded.add_field(name='__**Resources**__', value='[Handout](' + handoutLink + ')\n[GearUp](' + gearupLink + ')\n')
    return(embeded)

@client.event
async def on_ready():
    print('Discord Bot On as {0.user}'.format(client))
    test.start()

@tasks.loop(minutes=5)
async def test():
    thisChannel = client.get_channel(933599507504058409)
    ourmessage = await thisChannel.fetch_message(933600016696750121)
    eventsList = next5EventsFormatted()
    eventsList = '\n'.join(eventsList)
    embeded = discord.Embed(title='Hours', url="https://calendar.google.com/calendar/u/1?cid=Y19lcTA1MXNrbjZlZ3UxMDZwMXZxaDZsbjM4b0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t",
    description=eventsList + "\n\n" + tillNextHours(),
    color=discord.Color.purple())  
    embeded.add_field(name='__**Resources**__', value='[Google Calendar](https://calendar.google.com/calendar/u/1?cid=Y19lcTA1MXNrbjZlZ3UxMDZwMXZxaDZsbjM4b0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t)\n[SignMeUp](https://signmeup.cs.brown.edu/)\n')
    await ourmessage.edit(embed=embeded)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.guild is None and not message.author.bot:
        if message.content.startswith('!anon'):
            thisChannel = client.get_channel(933421821355757640)
            embeded = discord.Embed(description='*"' + message.content[5:] + '"*', color=discord.Color.dark_blue(), timestamp=datetime.datetime.utcnow())
            await message.add_reaction("👍")
            await thisChannel.send(embed=embeded)
            return
    user_message = str(message.content)
    channel = str(message.channel.name)
    if user_message.startswith('!'):
        if user_message == '!chain':
            due_date = datetime.datetime(2022, 2, 14, 23, 59, 59)
            timeLeft = findTimeDif(due_date)
            await message.delete()
            embeded = composeEmbed('Project 1 : Chain', 'https://csci1951l-spring2022.vercel.app/', 'This project is due on February 14, 2022 at 11:59pm EST.', 
                "Time left until due date : " + timeLeft, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            await message.channel.send(embed=embeded)
        elif user_message == '!coin':
            due_date = datetime.datetime(2022, 3, 6, 23, 59, 59)
            timeLeft = findTimeDif(due_date)
            await message.delete()
            embeded = composeEmbed('Project 2 : Coin', 'https://csci1951l-spring2022.vercel.app/', 'This project is due on March 6, 2022 at 11:59pm EST.',
                "Time left until due date : " + timeLeft, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            await message.channel.send(embed=embeded)
        elif user_message == '!lightning':
            due_date = datetime.datetime(2022, 4, 17, 23, 59, 59)
            timeLeft = findTimeDif(due_date)
            await message.delete()
            embeded = composeEmbed('Project 3 : Lightning', 'https://csci1951l-spring2022.vercel.app/', 'This project is due on April 17, 2022 at 11:59pm EST.',
                "Time left until due date : " + timeLeft, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            await message.channel.send(embed=embeded)
        elif user_message == '!auction':
            await message.delete()
            due_date = datetime.datetime(2022, 5, 1, 23, 59, 59)
            timeLeft = findTimeDif(due_date)
            embeded = composeEmbed('Project 4 : Auction', 'https://csci1951l-spring2022.vercel.app/', 'This project is due on May 1, 2022 at 11:59pm EST.',
                "Time left until due date : " + timeLeft, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            await message.channel.send(embed=embeded)
        elif user_message == '!commands'or user_message == '!help':
            embeded = discord.Embed(title='Commands', description=
                '**!<project name>** = To get the project details.\n' +
                '**!hours** = To get information about upcoming hours.\n' +
                '**!help** = To get this message again.\n' + 
                'You can also PM the bot **"!anon <message>"** to post a question anonymously!', color=discord.Color.red())
            await message.delete()
            await message.channel.send(embed=embeded)
        elif user_message == '!hours':
            eventsList = next5EventsFormatted()
            eventsList = '\n'.join(eventsList)
            embeded = discord.Embed(title='Hours', url="https://calendar.google.com/calendar/u/1?cid=Y19lcTA1MXNrbjZlZ3UxMDZwMXZxaDZsbjM4b0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t",
            description=eventsList + "\n\n" + tillNextHours(),
            color=discord.Color.purple())  
            embeded.add_field(name='__**Resources**__', value='[Google Calendar](https://calendar.google.com/calendar/u/1?cid=Y19lcTA1MXNrbjZlZ3UxMDZwMXZxaDZsbjM4b0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t)\n[SignMeUp](https://signmeup.cs.brown.edu/)\n')
            await message.delete()
            await message.channel.send(embed=embeded)
        # elif user_message == "!welcome":
        #     embeded = discord.Embed(title='Welcome!', description='The Discord is still **under construction**, but will be fully up and running by the start of shopping period!\n', color=discord.Color.red())
        #     await message.delete()
        #     await message.channel.send(embed=embeded)
        # elif user_message == "!rules":
        #     embeded = discord.Embed(title="Rules", description='**1.** No spamming.\n' + 
        #     '**2.** Do your best to keep discussion relevant to the channel you are in.\n' +
        #     "**3.** Don't break the [Collaboration Policy](https://csci1951l-spring2022.vercel.app/) as outlined on the course website.\n" +
        #     "**4.** Be respectful to the TAs and other students.\n", color=discord.Color.teal())
        #     await message.delete()
        #     await message.channel.send(embed=embeded)

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    if reaction.message.channel.id == 933617908251246645:
        if reaction.emoji == '👍':
            role = discord.utils.get(user.guild.roles, name='Student')
            await user.add_roles(role)
            
client.run(os.getenv('TOKEN'))
