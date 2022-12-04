import json
from pathlib import Path

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=['help']))
async def send_help(message: Message):
    with open(Path(Path.cwd(), 'data/commands.json')) as f:
        commands_dict = json.load(f)
    commands = ''
    for key, value in commands_dict.items():
        commands += f'{key} - {value}\n'
    await message.reply(commands)
