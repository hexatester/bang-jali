from telethon import TelegramClient
from telethon.tl.custom import Message
from telethon.tl.types import Chat, User
from telethon.events import NewMessage, ChatAction
from typing import Dict, List, Union

from jali import ID, API_ID, API_HASH
from jali.utils import get_tags, unindent

TAGS: Dict[str, str] = get_tags()

jali = TelegramClient(ID, API_ID, API_HASH)

NEW_USERS: List[User] = []
WELCOME_PER = 10


@jali.on(NewMessage)
async def message(event: NewMessage.Event):
    pass


@jali.on(
    NewMessage(forwards=False, pattern=r'^#[a-z]+$',
               func=lambda e: e.is_reply))
async def katalog(event: Union[NewMessage.Event, Message]):
    tag: str = event.raw_text[1:]
    if tag in TAGS:
        message: Message = await event.get_reply_message()
        await message.reply(TAGS[tag])


@jali.on(ChatAction)
async def chat_action(event: Union[ChatAction.Event, Message]):
    if event.user_joined:
        user: User = await event.get_user()
        if user not in NEW_USERS:
            NEW_USERS.append(user)
        if len(NEW_USERS) >= WELCOME_PER:
            chat: Chat = await event.get_chat()
            text = 'Selamat datang di group'
            for user in NEW_USERS:
                name = user.first_name
                if user.last_name:
                    name += ' ' + user.last_name
                text += f", [{name}](tg://user?id={user.id})"
            text += '''. 😃\n
            - Feel free to sharing seputar UT
            - No SARA
            - No SPAM
            - No Iklan
            '''
            await jali.send_message(chat.id, unindent(text))
