import time

from telethon import TelegramClient
from telethon.tl.custom import Message
from telethon.tl.types import Chat, User
from telethon.events import NewMessage, ChatAction
from typing import Dict, Union

from jali.config import ID, API_ID, API_HASH, ADMIN
from jali.utils import get_tags, unindent

TAGS: Dict[str, str] = get_tags()

jali = TelegramClient(ID, API_ID, API_HASH)

# chat_id -> user_id -> name
NEW_USERS: Dict[int, Dict[int, str]] = {}
WELCOME_PER = 10


@jali.on(NewMessage)
async def message(event: NewMessage.Event):
    pass


last_hastag = int(time.time()) - 60


@jali.on(
    NewMessage(forwards=False,
               pattern=r'^!#[a-z]+$',
               func=lambda e: e.is_reply))
async def hastag(event: Union[NewMessage.Event, Message]):
    global last_hastag
    tag: str = event.raw_text[2:]
    user: User = await event.get_sender()
    if tag in TAGS and user.id == ADMIN or int(time.time()) - last_hastag > 60:
        message: Message = await event.get_reply_message()
        await message.reply(TAGS[tag], link_preview=False)
        last_hastag = int(time.time())


@jali.on(ChatAction)
async def chat_action(event: Union[ChatAction.Event, Message]):
    if event.user_joined:
        chat: Chat = await event.get_chat()
        user: User = await event.get_user()
        NS = NEW_USERS.get(chat.id, {})
        if user.id not in NS:
            name = user.first_name
            if user.last_name:
                name += ' ' + user.last_name
            NS[user.id] = name
        if len(NS) >= WELCOME_PER:
            chat: Chat = await event.get_chat()
            text = 'Selamat datang di group'
            for id_, name in NS.items():
                text += f", [{name}](tg://user?id={id_})"
            text += '''. 😃\n
            **Feel free to sharing seputar UT, No SARA, No SPAM, No Iklan.**
            [Kumpulan Akses Bahan Ajar](https://t.me/UniversitasTerbuka/37415)
            [FAQ](https://t.me/UnivTerbukaID/11)
            Bahan ajar juga bisa dibaca di @UniversitasTerbukaBot
            '''
            await jali.send_message(
                chat.id,
                unindent(text),
                link_preview=False,
            )
            NS.clear()
        NEW_USERS[chat.id] = NS
