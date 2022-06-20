import asyncio
import itertools
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest

from config import api_id, api_hash


async def main():
    client = TelegramClient('Telethon Try Invite', api_id, api_hash)
    await client.start()

    print("trying invites...")

    options = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "-",
        "_",
    ]

    attempts = 0

    for guess in itertools.product(options, repeat=16):
        attempts += 1
        guess = ''.join(guess)
      #  await asyncio.sleep(0.03)
      #  print(attempts, guess)
        try:
            chat_invite = await client(ImportChatInviteRequest(guess))
            print(attempts, guess)
            print(chat_invite)
        except:
            pass

    print("done.")


asyncio.run(main())
