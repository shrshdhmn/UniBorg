import os
from telethon import events
from telethon.tl import functions
from uniborg.util import admin_cmd


@borg.on(events.NewMessage(pattern=r".Sbio ?(.*)", chats=-1001230772704))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            about=bio
        ))
    except Exception as e:  # pylint:disable=C0103,W0703
        return