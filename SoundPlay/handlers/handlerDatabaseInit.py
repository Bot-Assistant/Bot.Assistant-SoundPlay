import services.serviceDatabase as serviceDatabase
import settings.settingBot as settingBot

def databaseInit():
    if settingBot.databaseType == "MariaDB":
        tableName = "addon_soundPlay_settings"
        columns = [
            ["serverID", "BIGINT NOT NULL"],
            ["userID", "BIGINT NOT NULL"],
            ["volume", "FLOAT NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        tableName = "addon_soundPlay_soundsList"
        columns = [
            ["serverID", "BIGINT NOT NULL"],
            ["folderName", "VARCHAR(255) NOT NULL"],
            ["soundName", "VARCHAR(255) NOT NULL"],
            ["soundPlayCount", "INT DEFAULT 0"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)


    elif settingBot.databaseType == "SQLite":
        tableName = "addon_soundPlay_settings"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["userID", "integer NOT NULL"],
            ["volume", "float NOT NULL"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)

        tableName = "addon_soundPlay_soundsList"
        columns = [
            ["serverID", "integer NOT NULL"],
            ["folderName", "text NOT NULL"],
            ["soundName", "text NOT NULL"],
            ["soundPlayCount", "integer DEFAULT 0"]
        ]
        serviceDatabase.databaseCreation(tableName, columns)