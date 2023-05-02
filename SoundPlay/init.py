# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-SoundPlay"
version = "1.2.2"

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "soundplay"

# Name of the file containing the cog
cogFile = "cogSoundPlay"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python",
    "PyNaCl"
]

# List of addons required by the addon
addonDependencies = []

# List of permissions required by the addon
addonPermissions = [
    "manage_roles",
    "send_messages",
    "connect",
    "speak",
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild",

    # Permission to play a sound
    "cmdPlay" : "discord.permission.connect",

    # Permission to create a folder
    "cmdCreateFolder" : "discord.permission.manage_messages",

    # Permission to remove a folder
    "cmdRemoveFolder" : "discord.permission.manage_messages",

    # Permission to upload a sound
    "cmdUploadSound" : "discord.permission.manage_messages",

    # Permission to remove a sound
    "cmdDeleteSound" : "discord.permission.manage_messages"
}

