# -*- coding: utf-8 -*-
"""
@file    : main.py
@date    : 2023-04-06
@author  : carey
"""
import discord
import os
import gpt

chat_history_map = {}

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.emojis = True
intents.message_content = True

client = discord.Client(intents=intents, bot=True)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author.id)
    history = chat_history_map.get(message.author.id)
    if history is None:
        chat_history_map[message.author.id] = []
    chat_history_map[message.author.id].append(message.content)
    generated_reply = gpt.generate_reply(message.content, chat_history_map[message.author.id])
    await message.channel.send(generated_reply)


client.run(os.getenv('TOKEN'))
