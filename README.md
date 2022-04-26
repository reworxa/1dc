# What is this ?
Hello! this is my first discord bot engine. Use the "settings.json" file to set up your Discord bot. You even have access to commands!

# How to use ?
Time to use and set up!

### Not a developer? Then be more comfortable with the user version!

For download : https://www.mediafire.com/file/tmturhwhk4mak7w/1dc.rar/file

I will not leave a youtube video as in "mpy". But I will give as detailed examples as in "mpy".

### Let's first lay the foundation of the settings.json file.
```json
{
      "botConfig": {
        "token": "your_bot_token",
        "activity": {
            "activityName": "Bot Activity",
            "activityURL": "",
            "activityType": ""
        },
        "prefix": "!",
        "startBotMessage": true
    }
}
```
The only thing that sticks in your mind here is the "startBotMessage" command. When the bot starts, this command sends a message to the terminal stating the bot's name and starting. If it is false, it will not work and will not send.

### Now let's type the real commands!

(

```json
  {
    "botConfig": {
        "token": "your_bot_token",
        "activity": {
            "activityName": "Bot Activity",
            "activityURL": "",
            "activityType": "playing"
        },
        "prefix": "!",
        "startBotMessage": true
    },
    "commands": {
        "clear": true,
        "avatar": true,
        "ban": false,
        "kick": false,
        "mute": {
            "muteCommand": false,
            "mutedRoleID": "mute-role-id"
        }
    }
}
```
Moderation commands are turned off by default.

To turn on any of these, set the regions that read false to true and enter the conditions if the condition requires it (for example: Role id).

# Here it is done!

Now that you have made your own settings, all is well!

All you have to do is download and run the code!
