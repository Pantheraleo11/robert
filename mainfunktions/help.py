def help(message):

    try:
        m = message.content.split(" ")
        flag = int(m[1])
    except:
        flag = ""

    if flag == "":
        out = "Helppage for random numbers:      /help random\n" \
            "Helppage for random teambuilding:   /help team"
        return out
    elif flag == "team":
        out = "Es funktionirt nur im Bot chat\n" \
            "1. Um die Teamauswahl zu starten:   bot team\n" \
            "2. Dann schreibt jeder der mitmachen möchte\n" \
            "    etwas in den Bot chat\n" \
            "3. Es geht los mit:     bot team start"
        return out
    elif flag == "random":
        out = "For random number:                                      /random\n" \
            "For coin:                                                /coin\n" \
            "For dice:                                                /dice"
        return out
