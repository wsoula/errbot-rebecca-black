""" Return rebecca black gifs if rebecca black is mentioned """
import os
import random
from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd


class Rebeccablack(BotPlugin):
    """Returns Rebecca Black gif"""
    def callback_message(self, mess):
        """Runs on every message"""
        if mess.body.upper().replace(' ', '').find('REBECCABLACK') != -1 and os.getenv('BOT_PREFIX', '!') == os.getenv('PROD_BOT_PREFIX', '!'):
            self.send_card(
                in_reply_to=mess,
                color='white',
                image=self.gif()
            )

    def gif(self):
        gifs = [
            "https://media1.giphy.com/media/yvaMWkRQpwhCU/giphy.gif?cid=6104955e9679ed759124a6a79072bff201bc96c7f78af6de&rid=giphy.gif", # noqa
            "https://media2.giphy.com/media/1X7vgDeISiInjAJQK7/giphy.gif?cid=6104955e4ba1bfb17640875b27cdc2637511bd111b3968de&rid=giphy.gif", # noqa
            "https://media3.giphy.com/media/z1CksDrnttZMA/giphy.gif?cid=6104955e61405a1ea1f1f1678b5468d97eb744350eed3e7c&rid=giphy.gif", # noqa
            "https://media4.giphy.com/media/dq9mX9hEbSfx6/giphy.gif?cid=6104955e3f7953fc02c36578c8b527f6fe4ec4888f3ec493&rid=giphy.gif", # noqa
            "https://media3.giphy.com/media/8SS0MSoBHa8la/giphy.gif?cid=6104955ea23136dba6daa7e736954533a653ff80b273acd7&rid=giphy.gif", # noqa
            "https://media1.giphy.com/media/ZLD94N65BOEGk/giphy.gif?cid=6104955e00471a13f95bf4e59a6adc1b3489d728a75a792f&rid=giphy.gif", # noqa
            "https://media1.giphy.com/media/wuUnCnoMdmPLO/giphy.gif?cid=6104955e8afa9a6cb6f757d7ca8e12f9606af13046b0677f&rid=giphy.gif", # noqa
            "https://media1.giphy.com/media/LqzgIzNWDiyFG/giphy.gif?cid=6104955e9bb19786966124f0446e2b7c9c4a4a22254dad2a&rid=giphy.gif", # noqa
            "https://media0.giphy.com/media/XdesnSMy28JzO/giphy.gif?cid=6104955e1878d01a8156134a8785d3f1624507d37616eab7&rid=giphy.gif" # noqa
        ]
        return random.choice(gifs)
