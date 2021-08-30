import asyncio
from asyncio.tasks import wait_for
import discord
import requests
import json


BOT_TOKEN = 'ODgxNTg1MzMxODMxNDYzOTk4.YSu-Ug.2AX_0R_KXowT9zR7QaJljb59pTs'
client = discord.Client()


def get_question():
    question = ''
    id = 1
    answer = 0

    response = requests.get("https://tranquil-scrubland-27455.herokuapp.com/api")
    json_data = json.loads(response.text)

    question += "**" + json_data[0]['title'] + "**" + "\n"

    for item in json_data[0]['answer']:
        question += f"**{str(id)}.** {item['answer']} \n"
        if item['is_correct']:
            answer =  id
        id += 1
    
    return(question, answer)

@client.event
async def on_message(message):
    # Checks if the message is from the bot
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Welcome little potato, I\'m Bot-kun')

    if message.content.startswith('$play'):
        question, answer = get_question()
        await message.channel.send(question)

        def check(m):
            return m.author == message.author and m.content.isdigit() 

        try:
            guess = await client.wait_for('message', check=check, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Lazy Potato, you took too long')

        if int(guess.content) == answer:
            await message.channel.send('Smarto Potato')
        else:
            await message.channel.send('Baka Potato')

 
client.run(BOT_TOKEN)
