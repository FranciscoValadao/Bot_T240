from pyrogram import Client, filters
from pyrogram.types import Chat
from dotenv import load_dotenv
from os import getenv
from asyncio import run
from classes import Usuario
import json
import shutil
import tempfile


load_dotenv()

app = Client('T240_bot',
             api_id=getenv('TELEGRAM_API_ID'),
             api_hash=getenv('TELEGRAM_API_HASH'),
             bot_token=getenv('TELEGRAM_BOT_TOKEN')
             )

@app.on_message(filters.command('hojeteve'))
async def messages(client, message):
    #Verifica quem mandou a mensagem
    if message.from_user.first_name == 'Francisco':
        Usuario.set_treino(vala)
        data["xico"] = Usuario.get_treino(vala)
    elif message.from_user.first_name == 'João Pedro':
        Usuario.set_treino(joao)
        data["joao"] = Usuario.get_treino(joao)
    elif message.from_user.first_name == 'Miguel':
        Usuario.set_treino(scat)
        data["scat"] = Usuario.get_treino(scat)
    elif message.from_user.first_name == 'Yago':
        Usuario.set_treino(yago)
        data["yago"] = Usuario.get_treino(yago)
    #Transforma as informações num compilado
    var = ("""
    {}
{}
{}
{}
    """ .format(
    Usuario.get_msg(vala),
    Usuario.get_msg(joao),
    Usuario.get_msg(scat),
    Usuario.get_msg(yago)
                         ))
    #Envia o ranking no app
    print(var)
    print(message.from_user.first_name)
    await message.reply('{}'.format(var))
    #Atualiza o arquivo json
    att_json(data)






@app.on_message(filters.command('tevenada'))
async def messages(client, message):
    if message.from_user.first_name == 'Francisco':
        Usuario.set_desfaz(vala)
        data["xico"] = Usuario.get_treino(vala)
    elif message.from_user.first_name == 'João Pedro':
        Usuario.set_desfaz(joao)
        data["joao"] = Usuario.get_treino(joao)
    elif message.from_user.first_name == 'Miguel':
        Usuario.set_desfaz(scat)
        data["scat"] = Usuario.get_treino(scat)
    elif message.from_user.first_name == 'Yago':
        Usuario.set_desfaz(yago)
        data["yago"] = Usuario.get_treino(yago)

    var = ("""
    {}
{}
{}
{}
    """ .format(
    Usuario.get_msg(vala),
    Usuario.get_msg(joao),
    Usuario.get_msg(scat),
    Usuario.get_msg(yago)
                         ))
    print(var)
    print(message.from_user.first_name)
    await message.reply('{}'.format(var))
    #Atualiza o arquivo json
    att_json(data)


@app.on_message(filters.command('ranking'))
async def messages(client, message):
    var = ("""
    {}
{}
{}
{}
    """ .format(
    Usuario.get_msg(vala),
    Usuario.get_msg(joao),
    Usuario.get_msg(scat),
    Usuario.get_msg(yago)
                         ))
    print(var)
    print(message.from_user.first_name)
    await message.reply('{}'.format(var))

def att_json(dados):
    with open('data.json', 'r', encoding='utf-8') as arq, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
    # escreve o objeto atualizado no arquivo temporário
        json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))
    # se tudo deu certo, renomeia o arquivo temporário
    shutil.move(out.name, 'data.json')


my_json = open("data.json")
data = json.load(my_json)

print(data)

yago = Usuario('Yago', data["yago"])
joao = Usuario('João', data["joao"])
vala = Usuario('Vala', data["xico"])
scat = Usuario('Scat', data["scat"])

app.run()