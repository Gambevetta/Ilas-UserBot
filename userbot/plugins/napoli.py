#@frafol su telegram / Clappo @NotLaudaa a piccone

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.47
    animation_ttl = range(0,117)
    input_str = event.pattern_match.group(1)
    if input_str == "napoli":
        await event.edit(input_str)
        animation_chars = [

            "NAPOLI SIMULATOR🛵",
            "NAPOLI SIMULATOR🛵C",
            "NAPOLI SIMULATO🛵CU",
            "NAPOLI SIMULAT🛵CUR",
            "NAPOLI SIMULA🛵CURR",
            "NAPOLI SIMUL🛵CURRI",
            "NAPOLI SIMU🛵CURRI G",
            "NAPOLI SIM🛵CURRI GE",
            "NAPOLI SI🛵CURRI GEN",
            "NAPOLI S🛵CURRI GENN",
            "NAPOLI 🛵CURRI GENNA",
            "NAPOLI🛵CURRI GENNA'",
            "NAPOL🛵CURRI GENNA'",
            "NAPO🛵CURRI GENNA'",
            "NAP🛵CURRI GENNA'",
            "NA🛵CURRI GENNA'",
            "N🛵CURRI GENNA'",
            "🛵CURRI GENNA'",
            "Sei stato shippato col motorino🛵/Condoglianze da @frafol"

            ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 117])
