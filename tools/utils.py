from pyrogram import Client, filters
from pyrogram.types import Chat
from dotenv import load_dotenv
from os import getenv
from asyncio import run
from classes import Usuario
import json
import shutil
import tempfile
import chardet

def get_users_list(data):
    users_list =[]
    for username, n_workouts in data.items():
        app_user = Usuario(username, n_workouts)
        users_list.append(app_user)
    return users_list

def att_json(dados):
    with open('data.json', 'r', encoding='utf-8') as arq, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
    # escreve o objeto atualizado no arquivo temporário
        json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))
    # se tudo deu certo, renomeia o arquivo temporário
    shutil.move(out.name, 'data.json')

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
    result = chardet.detect(rawdata)
    return result['encoding']