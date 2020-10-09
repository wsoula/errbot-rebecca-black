from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import random

class Rebeccablack(BotPlugin):
    """Returns Rebecca Black gif"""
    def callback_message(self, mess):
        """Runs on every message"""
        if mess.body.find('rebeccablacktesterino') != -1:
            self.send_card(
                in_reply_to=mess,
                image=self.gif()
            )

    def gif(self):
        gifs = [
            "https://media1.giphy.com/media/yvaMWkRQpwhCU/giphy.gif?cid=6104955e9679ed759124a6a79072bff201bc96c7f78af6de&rid=giphy.gif" # noqa
            "https://media2.giphy.com/media/1X7vgDeISiInjAJQK7/giphy.gif?cid=6104955e4ba1bfb17640875b27cdc2637511bd111b3968de&rid=giphy.gif" # noqa
        ]
        return random.choice(gifs)
