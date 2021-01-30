import requests
import xml.etree.ElementTree as et
import json


def twitch_is_live(url):
    return twitch_api(url.split('/')[-1])
    twitch = requests.get(url)
    twitch = twitch.text
    twitch = twitch.split('LIVE')
    print(len(twitch))
    # twitch = twitch.index('Live')
    return twitch
    tree = et.fromstring(twitch)
    # tree.findall('/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/a/div/div/div/div[2]/div/div/div/p')
    return twitch

def twitch_api(user):
    url = 'https://api.twitch.tv/kraken/streams/' + user + '?client_id=' + 'wbmytr93xzw8zbg0p1izqyzzc5mbiz'
    twitch = requests.get(url)
    return twitch.text


twitch1 = 'https://www.twitch.tv/sheridanelektra'
twitch2 = 'https://www.twitch.tv/iwkerley'
twitch3 = 'https://www.twitch.tv/actualjake'




if __name__ == '__main__':
    print(twitch_is_live(twitch1))
    print(twitch_is_live(twitch2))
    print(twitch_is_live(twitch3))

