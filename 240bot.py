from pyrogram import Client, filters
from pyrogram.types import Chat
from dotenv import load_dotenv
from os import getenv
from asyncio import run
from classes import Usuario
import json
import shutil
import tempfile
import tools.utils as uti


load_dotenv()

app = Client('T240_bot',
             api_id=getenv('TELEGRAM_API_ID'),
             api_hash=getenv('TELEGRAM_API_HASH'),
             bot_token=getenv('TELEGRAM_BOT_TOKEN')
             )

@app.on_message(filters.command('hojeteve'))
async def messages(client, message):
    with open("data.json", 'r', encoding='utf-8') as my_json:
        data = json.load(my_json)
    users_list = uti.get_users_list(data)
    user = message.from_user.first_name
    ranking = ''
    if user in data.keys():
        for app_user in users_list:
            if app_user.name == user:
                Usuario.set_workout(app_user)
                data[user] = Usuario.get_workout(app_user)
                uti.att_json(data)
            workouts = Usuario.get_msg(app_user)
            ranking +=f'\n{workouts}'
        await message.reply('{}'.format(ranking))
    else:
        await message.reply(f'Usuário {user} não registrado')


@app.on_message(filters.command('tevenada'))
async def messages(client, message):
    with open("data.json", 'r', encoding='utf-8') as my_json:
        data = json.load(my_json)
    users_list = uti.get_users_list(data)
    user = message.from_user.first_name
    ranking = ''
    if user in data.keys():
        for app_user in users_list:
            if app_user.name == user:
                Usuario.undo_workout(app_user)
                data[user] = Usuario.get_workout(app_user)
                uti.att_json(data)
            workouts = Usuario.get_msg(app_user)
            ranking +=f'\n{workouts}'
        await message.reply('{}'.format(ranking))
    else:
        await message.reply(f'Usuário {user} não registrado')


@app.on_message(filters.command('ranking'))
async def messages(client, message):
    with open("data.json", 'r', encoding='utf-8') as my_json:
        data = json.load(my_json)
    users_list = uti.get_users_list(data)
    user = message.from_user.first_name
    ranking = ''
    if user in data.keys():
        for app_user in users_list:
            workouts = Usuario.get_msg(app_user)
            ranking +=f'\n{workouts}'
        await message.reply('{}'.format(ranking))


if __name__ == '__main__':
    print("running")
    app.run()
