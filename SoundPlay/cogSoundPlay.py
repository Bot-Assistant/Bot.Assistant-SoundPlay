# Author: Ted.
# Co-Author: Mr.Se6un

# External imports
import os

# BOTASSISTANT IMPORTS
from services.serviceLogger import Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
from settings.settingBot import debug
import services.serviceBot as serviceBot
# Settings
from settings.settingBot import debug

# Discord
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()


# 𝗔𝗗𝗗𝗢𝗡
# Init file
import addons.SoundPlay.init as init
# Database
import addons.SoundPlay.handlers.handlerDatabaseInit as handlerDatabaseInit
# Settings
import addons.SoundPlay.settings.settingAddon as settingAddon
# Functions
import addons.SoundPlay.functions.commands.commandRequirements as commandRequirements
import addons.SoundPlay.functions.commands.commandPlay as commandPlay
import addons.SoundPlay.functions.commands.commandFolderCreate as commandFolderCreate
import addons.SoundPlay.functions.commands.commandFolderDelete as commandFolderDelete
import addons.SoundPlay.functions.commands.commandSoundUpload as commandSoundUpload
import addons.SoundPlay.functions.commands.commandSoundDelete as commandSoundDelete
# Events
import addons.SoundPlay.functions.events.eventOnReady as eventOnReady
import addons.SoundPlay.functions.events.eventOnGuildJoin as eventOnGuildJoin
import addons.SoundPlay.functions.events.eventOnGuildRemove as eventOnGuildRemove
import addons.SoundPlay.functions.events.eventOnVoiceStateUpdate as eventOnVoiceStateUpdate


class PlaySound(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # INIT SOUNDS FOLDERS
    @commands.Cog.listener()
    async def on_ready(self):
        eventOnReady.onReady()

    # Create the sound folder with guild ID if it doesn't exist
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        eventOnGuildJoin.onGuildJoin(guild)

    # Remove the sound folder with guild ID if it exists
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        eventOnGuildRemove.onGuildRemove(guild)
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        await eventOnVoiceStateUpdate.onVoiceStateUpdate(member, before, after)



    # AUTOCOMPLETE
    async def getSoundsFolders(ctx: discord.AutocompleteContext):
        return os.listdir(settingAddon.defaultSoundFolder + str(ctx.interaction.guild_id) + "/")

    async def getSounds(ctx: discord.AutocompleteContext):
        directory = ctx.options["directory"]
        return os.listdir(settingAddon.defaultSoundFolder + str(ctx.interaction.guild_id) + "/" + directory + "/")


    # INIT GROUP COMMAND
    groupSoundPlay = discordCommands.SlashCommandGroup(init.cogName, "🔶 Group of commands to manage the SoundPlay addon")
    groupDeleteElement = groupSoundPlay.create_subgroup("delete", "🔶 Group of commands to delete elements")
    groupCreateElement = groupSoundPlay.create_subgroup("create", "🔶 Group of commands to create elements")

    # Verify if the bot has the prerequisites permissions
    @groupSoundPlay.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx) 

    
    # PLAY A SOUND
    # Play a sound from the sound folder
    @groupSoundPlay.command(name="play", description="Play a sound from the sound folder")
    async def cmdPlay(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSoundsFolders), description="Folder where the sound is located")
        ):
        await commandPlay.play(ctx, directory)


    # UPLOAD A SOUND
    # Upload a sound in a specific folder
    @groupSoundPlay.command(name="upload", description="Upload a sound in a specific folder")
    async def cmdSFXUpload(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSoundsFolders), description="Folder where the sound is located", required=True),
        sound: discord.Option(discord.Attachment, description="Sound to upload", required=True)
        ):
        await commandSoundUpload.upload(ctx, directory, sound)


    # DELETE A ELEMENT
    # Create a new sound folder in the sound folder
    @groupCreateElement.command(name="folder", description="Create a new sound folder in the sound folder")
    async def cmdSFXFolderCreate(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, description="Folder where the sound is located")
        ):
        await commandFolderCreate.folderCreate(ctx, directory)

    # Delete a sound folder in the sound folder
    @groupDeleteElement.command(name="folder", description="Delete a sound folder in the sound folder")
    async def commandSFXFolderDelete(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSoundsFolders), description="Folder where the sound is located")
        ):
        await commandFolderDelete.folderDelete(ctx, directory)

    # Delete a sound in a specific folder
    @groupDeleteElement.command(name="sound", description="Delete a sound in a specific folder")
    async def cmdSFXDelete(
        self,
        ctx: commands.Context,
        directory: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSoundsFolders), description="Folder where the sound is located", required=True),
        sound: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(getSounds), description="Sound to delete", required=True)
        ):
        await commandSoundDelete.soundDelete(ctx, directory, sound)


# INIT COG
def setup(bot):
    Logger.debug("[COG][SOUNDPLAY]Sound play cog init")
    handlerDatabaseInit.databaseInit()
    bot.add_cog(PlaySound(bot))


