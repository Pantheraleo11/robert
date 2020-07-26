def readSetting(settingsfile, setting):
    file = open(settingsfile, "r")
    for line in file:
        if setting in line:
            content = line.split("==")
            return content[1]
    return "!!!FAIL!!!"

def readSetting(setting):
    file = open("settings.txt", "r")
    for line in file:
        if setting in line:
            content = line.split("==")
            return content[1]
    return "!!!FAIL!!!"
