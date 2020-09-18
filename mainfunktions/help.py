def help(message):

    try:
        m = message.content.split(" ")
        flag = int(m[1])
    except:
        flag = ""

    if flag == "":
        out = "Hilfe für Zufallszahlen:      bot help random\n" \
            "Hilfe für Zufälligesteam:   bot help team"
        return out
    elif flag == "team":
        out = "Es funktionirt nur im Bot chat\n" \
            "1. Um die Teamauswahl zu starten:   bot team\n" \
            "2. Dann schreibt jeder der mitmachen möchte\n" \
            "    etwas in den Bot chat\n" \
            "3. Es geht los mit:     bot team start"
        return out
    elif flag == "random":
        out = "Für eine beliebige Zahl:                                      bot random\n" \
            "Für einen Münzwurf:                                          bot coin\n" \
            "Für einen Würfel mit 6 Seiten:                          bot dice\n" \
            "Für einen Würfel mit belibig vielen Steiten:   bot dice 20 / belibige zahl"
        return out
