"""Commands:
.catturaibambini"""

import asyncio
import datetime
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import asyncio
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "UserBot"
# ============================================


@bot.on(dev_cmd(pattern=r"catturaibambini"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("[**Comando Creato Da Uno 05**]\nScusate il ritardo ma mi ci sono volute ore per ritrovare la mia collezione di bambini e posso assicurarvi che non è un lavore facile")