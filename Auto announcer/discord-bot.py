import discord
import yaml
import friends


def load_yaml(yaml_file):
    with open(yaml_file) as stream:
        data = yaml.safe_load(stream)
    return data


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        for i in announcements:
            channel = client.get_channel(load_yaml(settings_file)['channel_ID'])
            await channel.send(load_yaml(settings_file)['web_link'])
            await channel.send(load_yaml(settings_file)['message'])

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'Live!':
            await message.channel.send(load_yaml(settings_file)['web_link'])
            await message.channel.send(load_yaml(settings_file)['message'])



if '__main__' == __name__:
    settings_file = 'settings.yaml'
    announcements = []
    # friends.get_friends(load_yaml(settings_file)['friends_path'])

    token = load_yaml(settings_file)['token']
    client = MyClient()
    client.run(token)
