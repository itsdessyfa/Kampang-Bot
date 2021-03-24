# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """
from datetime import datetime
import time
from time import sleep
from platform import uname
import asyncio
from userbot import CMD_HELP, BOT_VER, ALIVE_NAME
from userbot.events import register

modules = CMD_HELP


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Module Salah KAMPAAAANGGGGG!!**")
            await asyncio.sleep(18)
            await event.delete()
    else:
        await get_readable_time((time.time() - StartTime))
        await event.edit(f"**╭►▻►▻►▻►▻►▻►◄◅◄◅◄◅◄◅◄◅╮**\"
                         f"**\n│ My Master: {ALIVE_NAME}**"
                         f"**\n│ BOT VERSI: {BOT_VER}**"
                         f"**\n│ PING BOT.: `% sms` \n**"
                         f"**\n│ Bantuan Modul[🐨BOT KAMPANG🐨]**"
                         f"**\n╰►▻►▻►▻►▻►▻►◄◅◄◅◄◅◄◅◄◅╯**"
                         f"**\n╭►▻►▻►▻►▻►▻►◄◅◄◅◄◅◄◅◄◅╮
                         f"**\n│   Untuk melihat lengkap Command**"
                         f"* \n│   Contoh: .help < nama module > n│   Modules Aktif: {len(modules)}**"
                         f"**\n╰►▻►▻►▻►▻►▻►◄◅◄◅◄◅◄◅◄◅╯")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t〙◈〘 "
        await event.reply(f"•{string}•"
                          "\nKONTOLLLL....")
        await event.reply(f"\n**Ketik Contoh** `.help afk` **Untuk Informasi Module**")
        await asyncio.sleep(1000)
        await event.delete()
