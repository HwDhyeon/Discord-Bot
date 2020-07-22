import asyncio
import discord
import json
import os
from typing import NoReturn
from discord.ext import commands
from utils import colored_print


def read_token_file() -> str:
    path = os.path.dirname(os.path.abspath(__file__)) + '/data/token.json'
    with open(file=path, mode='r', encoding='utf-8') as f:
        data = json.load(f)
    return data['token']


def init_bot_informations():
    return commands.Bot(
        command_prefix='-',    
        status=discord.Status.online,
        activity=discord.Game('-help')    
    )


# Bot Settings
bot = init_bot_informations()


# Start Bot
@bot.event
async def on_ready() -> NoReturn:
    colored_print('Bot is running...', 'yellow')


@bot.event
async def on_member_join(member):
    await member.send('Hi~✨')


@bot.event
async def on_message(message):
    bad_words = [
        'fuck',
    ]
    for bad_word in bad_words:
        if bad_word in message.content:
            colored_print('\nBad word detection!', 'red')
            colored_print(f'Content: [{message.content}]')
            await message.channel.send('Let\'s use good and fine words.')
            await message.delete()
            break
    await bot.process_commands(message)


@bot.command()
async def commands(ctx):
    await ctx.send('How can I help you?')


@bot.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


if __name__ == "__main__":
    bot.run(read_token_file())
