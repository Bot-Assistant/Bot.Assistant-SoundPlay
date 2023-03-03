import os

import addons.soundplay.settings.settingAddon as settingAddon

def onGuildRemove(guild):
    if os.path.exists(settingAddon.defaultSoundFolder + str(guild.id)):
            
            # Remove all folders and files
            for root, dirs, files in os.walk(settingAddon.defaultSoundFolder + str(guild.id), topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))

            os.rmdir(settingAddon.defaultSoundFolder + str(guild.id))