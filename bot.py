#! python

import discord
import requests
import json
import random
import asyncio

from discord import Client
from dotenv import load_dotenv#! python

import discord
import requests
import json
import random
import asyncio

from discord import Client
from dotenv import load_dotenv
import os

os.eviron()
load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

sysmsg_channel = client.get_channel(843676544316735528)
welcome_channel = client.get_channel(845398906577879060)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


sad_words = {"sad", 'depressed', "unhappy", "angry", "miserable", "tired", 'ticked', 'pissed'}

encouragements = [
    'Cheer up!', 'Don\'t give up.', 'Keep a stiff upper lip.',
    'Hang in there.', 'You know your on the right path when things stop being easy.',
    'You are a great person / bot!', 'Patience is power.', 'Stay hungry.',
    'It can\'t rain all the time.', 'Don\'t say \"Why me?\" Say \"Try me!\"',
    'No worries.', 'Fierce. Focused. Force of nature. Unlimited. Unleashed.       Understood?',
    'Stop looking back, you’re not going that way.', 'Smile. It makes people wonder what your up to.'
]


# ######## functions ###############

def get_title(name):
    # makes a list of role names
    role_names = [role.name for role in name.roles]
    length = len(role_names)  # checks number of roles
    title = ""
    if length > 1:  # ignore @everyone role
        list_item = 1
        while length > 1:
            title += "{0} ".format(role_names[list_item])
            length -= 1
            list_item += 1

        return title
    else:
        return False


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Do not close window')


#   ****** When new member joins / leaves
@client.event
async def on_member_join(member):
    embedVar = embed = discord.Embed(
        title="Welcome " + member.name + ' to the ' + member.guild.name,
        description=f"You are member # {member.guild.member_count}",
        color=discord.Color.red(),
        inline=False)
    embedVar.set_thumbnail(url=member.avatar_url)

    await welcome_channel.send(embed=embedVar)
    await sysmsg_channel.send(member.name + ' joined.')


@client.event
async def on_member_remove(member):
    await sysmsg_channel.send(member.name + ' has left.')


# ********* responses to various messages from members
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # ************* sends message to member of his/her roles
    if message.content.startswith('$whoami'):
        await message.delete()  # removes message
        member_title = (get_title(message.author))
        if member_title:
            await message.author.send(member_title + " " + message.author.nick)
        else:
            await message.author.send('You have no Hell association.')

    # ************ respond to greeting, then removes post
    if message.content.startswith('Hail!'):
        member = message.author
        greetings = [
            'Are you my mudder?', 'Master ' + member.nick + ' has returned!'
        ]
        botmsg = await message.channel.send(random.choice(greetings))
    #    await asyncio.sleep(15)
    #    await botmsg.delete()  # removes message

    # ****** give inspiring quote when requested
    if message.content.startswith('$inspire'):
        await message.delete()  # removes message
        quote = get_quote()
        await message.channel.send(quote)

    # *********** checks if anyone says "sad words", Stygee will respond
    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(encouragements))

    # ************ list out help commands, then removes post -
    if message.content.startswith('$help'):
        await message.delete()  # removes message
        botmsg = await message.channel.send('These are available commands:\n' +
                                            '$inspire - random inspiring quotes\n' +
                                            '$whoami - Returns your roles on the discord server\n')
        await asyncio.sleep(15)
        await botmsg.delete()  # removes message

    # *********** Embed test **************
    if message.content.startswith('$hello'):
        member = message.author
        embedVar = embed = discord.Embed(
            title='Welcome ' + member.name + " to the " + member.guild.name,
            description=f'You are member # {member.guild.member_count}',
            color=discord.Color.red(),
            inline=False)
        embedVar.set_thumbnail(url=member.avatar_url)

        await welcome_channel.send(embed=embedVar)

client.run(DISCORD_TOKEN)
import os

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

sysmsg_channel = client.get_channel(843676544316735528)
welcome_channel = client.get_channel(845398906577879060)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


sad_words = {"sad", 'depressed', "unhappy", "angry", "miserable", "tired", 'ticked', 'pissed'}

encouragements = [
    'Cheer up!', 'Don\'t give up.', 'Keep a stiff upper lip.',
    'Hang in there.', 'You know your on the right path when things stop being easy.',
    'You are a great person / bot!', 'Patience is power.', 'Stay hungry.',
    'It can\'t rain all the time.', 'Don\'t say \"Why me?\" Say \"Try me!\"',
    'No worries.', 'Fierce. Focused. Force of nature. Unlimited. Unleashed.       Understood?',
    'Stop looking back, you’re not going that way.', 'Smile. It makes people wonder what your up to.'
]


# ######## functions ###############

def get_title(name):
    # makes a list of role names
    role_names = [role.name for role in name.roles]
    length = len(role_names)  # checks number of roles
    title = ""
    if length > 1:  # ignore @everyone role
        list_item = 1
        while length > 1:
            title += "{0} ".format(role_names[list_item])
            length -= 1
            list_item += 1

        return title
    else:
        return False


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Do not close window')


#   ****** When new member joins / leaves
@client.event
async def on_member_join(member):
    embedVar = embed = discord.Embed(
        title="Welcome " + member.name + ' to the ' + member.guild.name,
        description=f"You are member # {member.guild.member_count}",
        color=discord.Color.red(),
        inline=False)
    embedVar.set_thumbnail(url=member.avatar_url)

    await welcome_channel.send(embed=embedVar)
    await sysmsg_channel.send(member.name + ' joined.')


@client.event
async def on_member_remove(member):
    await sysmsg_channel.send(member.name + ' has left.')


# ********* responses to various messages from members
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # ************* sends message to member of his/her roles
    if message.content.startswith('$whoami'):
        await message.delete()  # removes message
        member_title = (get_title(message.author))
        if member_title:
            await message.author.send(member_title + " " + message.author.nick)
        else:
            await message.author.send('You have no Hell association.')

    # ************ respond to greeting, then removes post
    if message.content.startswith('Hail!'):
        member = message.author
        greetings = [
            'Are you my mudder?', 'Master ' + member.nick + ' has returned!'
        ]
        botmsg = await message.channel.send(random.choice(greetings))
    #    await asyncio.sleep(15)
    #    await botmsg.delete()  # removes message

    # ****** give inspiring quote when requested
    if message.content.startswith('$inspire'):
        await message.delete()  # removes message
        quote = get_quote()
        await message.channel.send(quote)

    # *********** checks if anyone says "sad words", Stygee will respond
    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(encouragements))

    # ************ list out help commands, then removes post -
    if message.content.startswith('$help'):
        await message.delete()  # removes message
        botmsg = await message.channel.send('These are available commands:\n' +
                                            '$inspire - random inspiring quotes\n' +
                                            '$whoami - Returns your roles on the discord server\n')
        await asyncio.sleep(15)
        await botmsg.delete()  # removes message

    # *********** Embed test **************
    if message.content.startswith('$hello'):
        member = message.author
        embedVar = embed = discord.Embed(
            title='Welcome ' + member.name + " to the " + member.guild.name,
            description=f'You are member # {member.guild.member_count}',
            color=discord.Color.red(),
            inline=False)
        embedVar.set_thumbnail(url=member.avatar_url)

        await welcome_channel.send(embed=embedVar)

client.run(DISCORD_TOKEN)
