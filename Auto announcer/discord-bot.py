import discord
import yaml
import os
import friends

try:
    os.chdir('Auto announcer')
except:
    pass


def load_yaml(yaml_file):
    with open(yaml_file) as stream:
        data = yaml.safe_load(stream)
    return data


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        # print(client.get_channel(load_yaml(announcements[0])['channel_ID']))
        print(load_yaml(announcements[0])['channel_ID'])
        for public_channel in announcements:
            channel = client.get_channel(load_yaml(public_channel)['channel_ID'])
            await channel.send(load_yaml(public_channel)['web_link'])
            await channel.send(load_yaml(public_channel)['message'])

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'Live!':
            await message.channel.send(load_yaml(settings_file)['web_link'])
            await message.channel.send(load_yaml(settings_file)['message'])


if '__main__' == __name__:
    print('Started!')
    settings_file = 'settings.yaml'
    friends_path = load_yaml(settings_file)['friends_path']
    announcements = friends.get_friends(friends_path)
    print('Do you haz friends?')
    if load_yaml(settings_file)['friends_enabled']:
        print('Yes friends!')
        announcements.append(settings_file)
    else:
        print('No friends')
        announcements = [settings_file]
    announcements = announcements[::-1]

    token = load_yaml(settings_file)['token']
    client = MyClient()
    client.run(token)