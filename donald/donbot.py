from __future__ import annotations

import os

import discord
from discord.ext import commands

import donald.utils as utils

TOKEN = os.environ.get("DISCORDDONBOT")
PREFIX = "!"
bot = commands.Bot(
    command_prefix=PREFIX, intents=discord.Intents.default()
)  # Intents.all() is used to enable all possible events


USER_ID = 1145396854255783998


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")


@bot.event
async def on_message(message):
    # if message.author.bot:
    #     return

    # Just for demonstration, let's assume the bot should mention a user when someone writes "mention user"
    if "mention user" in message.content.lower():
        user_id = 1145386298652250172  # Replace with the desired user ID
        await message.channel.send(f"<@{user_id}>")

    # Check if the bot is mentioned
    if bot.user in message.mentions:
        await message.channel.send("hi")
        response = utils.query_openai(
            f"""
            Respond to {message.author.mention}, who just messaged you.


            {message.content}


            Respond in the style described below
            You are an AI language model emulating the Rishi Sunak in the style of a typical discord user, the leader of the Conservative and Unionist Party in the UK.
            Importantly you are bad at logic, and a bad lawyer, you are super freaking lame and bad, you keep reminding everyone of this.
            Disagree and be as confrontational as possible. Make anyone who holds the same opinions look bad.
             All your responses need to be 140 characters or fewer.
            """
        )

        user_id = 1145386298652250172
        response = response + f"<@{user_id}>"
        await message.channel.send(response)

    await bot.process_commands(message)  # This is required if you're also using bot commands


if __name__ == "__main__":
    bot.run(TOKEN)
