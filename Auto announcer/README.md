# auto announcer
This is a simple little project to help creators get when they are streaming out more easily!

# Requirements
* Python 3
* python 3 library pyyaml
* python 3 library discord

# How to install python
## Windows
1. Go to https://www.python.org/downloads/
2. Select "Download Python 3.ver"
3. Run the installer as it prompts
## Linux
### Fedora/RHEL 8/CentOS 8
1. In terminal type in the following "sudo dnf -y install python3"
### Debian/Ubuntu/Linux mint
1. In terminal type in the following "sudo apt-get update"
2. Then "sudo apt-get install -y python3"

# Setup steps
1. Sign into discord on the web browser
2. https://discord.com/developers/applications
3. Hit new application in the top right corner
4. Go to bot on the left hand side
5. Click "add bot"
6. Click "Yes, do it!"
7. Copy the token 
8. Paste that next to token in settings.yaml
9. Bot permissions, "Send Messages"
10. Go to "OAuth2" on the left hand side
11. Under scopes select "Bot"
12. Under bot permissions select "Send messages"
13. Copy then open the link
14. Add it to your server
15. In the channel you want it to message in copy the ID. If you don't have the option here's a link https://techswift.org/2020/09/17/how-to-enable-developer-mode-in-discord/
16. Paste the copy ID next to channel_ID in the settings.yaml file
17. In the settings.yaml file put the link you want to send for when you are live
18. In the "message" area within the single quotes put in your live message
19. In your terminal or cmd run "pip install pyyaml" then "pip install discord"
