from __future__ import annotations

import os

import discord
from discord.ext import commands

import donald.utils as utils

TOKEN = os.environ.get("DISCORDBOTTOKEN")
PREFIX = "!"
USER_ID = 1145386298652250172

bot = commands.Bot(
    command_prefix=PREFIX, intents=discord.Intents.default()
)  # Intents.all() is used to enable all possible events


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")


@bot.event
async def on_message(message):
    # if message.author.bot:
    #     return

    # Check if the bot is mentioned
    if bot.user in message.mentions:
        await message.channel.send("hi")

        # Just for demonstration, let's assume the bot should mention a user when someone writes "mention user"
        if "mention user" in message.content.lower():
            user_id = 1145396854255783998  # Replace with the desired user ID
            await message.channel.send(f"<@{user_id}>")

        response = utils.query_openai(
            f"""


            Respond to {message.author.mention}, who just messaged you. Respond in the style described below


            {message.content}


            You are an AI language model emulating the speech and policy positions of Sir Keir Starmer in the style of a typical discord user, the leader of the Labour Party in the UK.
            Importantly you are good at logic, and a lawyer, you are personable and persuasive. All your responses need to be 140 characters or fewer.



            """
        )

        user_id = 1145396854255783998
        response = response + f"<@{user_id}>"
        await message.channel.send(response)

    await bot.process_commands(message)  # This is required if you're also using bot commands


if __name__ == "__main__":
    bot.run(TOKEN)
