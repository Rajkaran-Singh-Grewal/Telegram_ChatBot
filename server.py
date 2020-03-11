# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:01:26 2019

@author: TomaicazyX
"""

from karen import telegram_chatbot as bot
import random
update_id=None
bot=bot("config.cfg")
from_=None
from_C=None
from_p=None
helps=["/roll6 -- rolls a dice","/toss -- tosses a coin","/images -- shows a random image","/rps <rock,paper,or scissor> -- plays rock paper scissor with you","/show -- shows you three random cards"]
def roll6():
    return random.randint(1,6)
def toss():
    coin=random.randint(1,2)
    if coin==1:
        return "head"
    else:
        return "tail"
def imagereply():
    return "/randomImage"
def rockPaperScissor(ss):
    ssw=bot.Game(ss)
    if ssw==1:
        return "its a tie"
    elif ssw==2:
        return " you win Congrats"
    elif ssw==3:
        return "I Win"
def teenpati():
    return "/teenpati"
def make_reply(msg):
    print (msg)
    reply=None
    if msg is not None:
        reply= "ok"
        if msg == "/roll6":
            reply=roll6()
            from_=from_C
        elif msg=="/toss":
            from_=from_C
            reply=toss()
        elif msg=="/image":
            reply=imagereply()
            from_=from_C
        elif msg=="/rps rock":
            reply=rockPaperScissor(1)
            from_=from_C
        elif msg=="/rps paper":
            reply=rockPaperScissor(2)
            from_=from_C
        elif msg=="/rps scissor":
            reply=rockPaperScissor(3)
            from_=from_C
        elif msg=="/show":
            reply=teenpati()
            from_=from_p
        elif msg=="/help":
            from_=from_C
            bot.showHelp(helps,from_)
            reply=""
    from_=from_C
    return reply,from_
while True:
    print("...")
    updates = bot.get_updates(offset=update_id)
    updates=updates["result"]
    if updates:
        for item in updates:
            update_id=item["update_id"]
            try:
                message =item["message"]["text"]
            except:
                message = None
            try:
                from_C=item["edited_message"]["chat"]["id"]
            except:
                from_C=item["message"]["chat"]["id"]
                from_p=item["message"]["from"]["id"]
            
            
            reply,from_ = make_reply(message)
            
            bot.send_messages(reply,from_)
