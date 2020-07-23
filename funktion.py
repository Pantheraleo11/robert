def help(flag):
    if flag == "help":
        t = "Hilfe für Zufallszahlen:      bot help random\n" \
            "Hilfe für Zufälligesteam:   bot help team"
        return str(t)
    elif flag == "team":
        t = "Es funktionirt nur im Bot chat\n" \
            "1. Um die Teamauswahl zu starten:   bot team\n" \
            "2. Dann schreibt jeder der mitmachen möchte\n" \
            "    etwas in den Bot chat\n" \
            "3. Es geht los mit:     bot team start"
        return str(t)
    elif flag == "random":
        t = "Für eine beliebige Zahl:                                      bot random\n" \
            "Für einen Münzwurf:                                          bot coin\n" \
            "Für einen Würfel mit 6 Seiten:                          bot dice\n" \
            "Für einen Würfel mit belibig vielen Steiten:   bot dice 20 / belibige zahl"
        return t

def flag_sero(state):
    flag_team(state)
    flag_random(state)
    return

def flag_team(state):
    global f
    if state == 1:
        f = 1
        return f
    if state == 0:
        f = 0
        return f
    if state == 2:
        return f

def flag_random(state):
    global f1
    if state == 1:
        f1 = 1
        return f1
    if state == 0:
        f1 = 0
        return f1
    if state == 2:
        return f1
    if state == 3:
        f1 = 3
        return f1

def clear_user():
    user = open("user.txt", "w")
    user.close()

def add_user(name,text):
    user = open("user.txt", "r")
    user = user.read()
    if str(name) in user and str(text) in user:
        print("test")
        return
    user = open("user.txt", "a")
    user.write(str(name)+" "+str(text)+"\n")
    print("test2")
    user.close()
    return