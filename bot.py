import asyncio
from asyncio.tasks import wait_for
import discord
import requests
import json
import os

BOT_TOKEN = os.getenv('Token')


client = discord.Client()


def update_score(user, points):
    url = "https://discordpotatobot-app.herokuapp.com/api/score/update/"

    new_score = {'name': user, 'points':points}
    response = requests.post(url, data=new_score)
    return

def get_score():
    url = "https://discordpotatobot-app.herokuapp.com/api/score/update/"
    leaderboard = ''
    id = 1

    response = requests.get(url)
    json_data = json.loads(response.text)

    leaderboard += f'**Leaderboard:** \n'
    for item in json_data:
        leaderboard += f"**{id}.** {item['name']} - {item['points']} points \n"
        id += 1

    return leaderboard

def get_question():
    question = ''
    id = 1
    answer = 0

    url = "https://discordpotatobot-app.herokuapp.com/api/random/"
    response = requests.get(url)
    json_data = json.loads(response.text)

    question += "**" + json_data[0]['title'] + "**" + "\n"

    for item in json_data[0]['answer']:
        question += f"**{id}.** {item['answer']} \n"
        if item['is_correct']:
            answer =  id
        id += 1
    
    points = json_data[0]['points']
    return(question, answer, points)

@client.event
async def on_message(message):
    # Checks if the message is from the bot
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Welcome little potato, I\'m Bot-kun')

    if message.content.startswith('$play'):
        question, answer, points = get_question()
        await message.channel.send(question)

        def check(m):
            return m.author == message.author and m.content.isdigit() 

        try:
            guess = await client.wait_for('message', check=check, timeout=7.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Lazy Potato, you took too long')

        user = guess.author
        if int(guess.content) == answer:
            msg = f'Smart potato {user.name}-san 😇, + {points} points!'
            await message.channel.send(msg)
            update_score(user, points)
        else:
            msg = f'Baka potato {user.name}-san 🤬, no points for u!'
            await message.channel.send(msg)
 
    if message.content.startswith('$score'):
        leaderboard = get_score()
        await message.channel.send(leaderboard)

client.run(BOT_TOKEN)
