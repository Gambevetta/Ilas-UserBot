import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "dio1":

        await event.edit(input_str)

        animation_chars = [

           "Porco dio",
			 "Porca Madonna",
			 "Dio cane",
			 "Dio pozzanghera",
			 "Dio Ipad",
			 "Dio frigorifero",
			 "Dio mobile",
			 "Dio termometro", "Dio penna", "Dio matita", "Dio astuccio", "Dio temperino", "Dio matematica", "Dio Italiano", "Dio algebra", "Dio chef", "Dio foto", "Dio video", "Dio spiaggia", "Dio bagnino", "Dio sitcker di maiale", "Dio codino", "Dio pettorali", "Dio dente all'indietro", "Dio nero", "Dio libretto delle istruzioni", "Dio pozzanghera", "Dio fotocamera", "Dio cuscino", "Dio pesce rosso", "Dio canile", "Dio arancia", "Dio arancino", "Dio pezzo di merda", "Dio App Store", "Dio Minecraft", "Dio Sticker di Telegram", "Dio sfondo", "Dio Display", "Dio straniero", "Dio mela", "Dio pera", "Dio egiziano", "Dio anziano", "Dio kebbbaro", "Dio kebab", "Dio cassetto", "Dio compasso", "Dio blu", "Dio auto blu", "Dio rotto", "Dio mano", "Dio Gianni Morandi", "Dio tromba", "Dio fotocamera", "Dio peruviano", "Dio tastiera", "Dio video su Youtube", "Dio vuoto emotivamente", "Dio ask", "Dio indiano", "Dio oscuro", "Dio Rovazzi", "Dio pecora", "Dio ippopotamo", "Dio giraffa", "Dio tumore", "Dio cancro", "Dio corona virus", "Dio vaccino", "Dio desktop", "Dio luminositÃ  al 100%", "Dio bot", "Dio ragazza", "Dio risata", "Dio reginetta del ballo", "Dio canaglia", "Cane dio", " Dio nella vale dei fuochi", "sono tutti dii.... ma di diverse categorie🐖🍌🧱✏️ By CiccioGamer89 con il codice paguro avrai un cazzo in culo porco dio"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])
