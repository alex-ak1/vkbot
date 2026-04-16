import json
import sys
import vk_api
from pathlib import Path

class VKBot:
    def __init__(self):
        self.settings = settings = json.load(open( str(Path(__file__).parent) + "/settings.json"))
        if (self.settings.get('vk', '') == ''):
            print( "No VK settings" )
            exit(1)
        if (self.settings['vk'].get('token', '') == ''):
            print( "No bot token specified" )
            exit(1)

        vk_session = vk_api.VkApi(token=self.settings['vk']['token'])
        self.vk = vk_session.get_api()

    def  sendMsg(self, msg):
        self.vk.messages.send(peer_id=self.settings['vk'].get('peer', ''),
                     message=msg, random_id=0)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print( "usage: python3 bot.py \"some message to user\"" )
        exit(1)

    bot = VKBot()

    msg = sys.argv[1]

    print( f" Send {msg}" )
    bot.sendMsg(msg)