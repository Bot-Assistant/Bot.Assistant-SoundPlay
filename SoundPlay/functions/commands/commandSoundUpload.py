import os

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

from addons.SoundPlay.settings.settingAddon import *
import addons.SoundPlay.handlers.handlerSoundsList as handlerSoundsList

from settings.settingColors import *

async def upload(ctx, directory, sound):

    # PERMISSIONS CHECK
    import addons.SoundPlay.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdUploadSound") == False:
        return

    # Folder where the sounds are located
    folder = defaultSoundFolder

    selectedFolder = folder + str(ctx.guild.id) + "/" + directory + "/"

    # If the folder already exists, send a message
    if os.path.exists(selectedFolder) == False:
        embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="This folder doesn't exist", color=red)
        await ctx.respond(embed=embed)
        return

    # Save the sound in the folder
    await sound.save(selectedFolder + sound.filename)

    # Add the sound to the database
    handlerSoundsList.addSound(ctx.guild.id, directory, sound.filename, 0)

    # Create the embed
    embed = discord.Embed(title=f"SOUNDBOARD : {directory}", description="Sound uploaded", color=green)
    await ctx.respond(embed=embed)