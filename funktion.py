def help(flag):
    if flag == "help":
        t = "Hlep for random nubers:      bot help random\n" \
            "help for random team:   bot help team"
        return str(t)
    elif flag == "team":
        t = "It's only working in the bot channel\n" \
            "1. Start bot team selection:   bot team\n" \
            "2. Everybody writs something in the bot channel \n" \
            "3. The team selection starts with:     bot team start"
        return str(t)
    elif flag == "random":
        t = "for any nuber:                                      bot random\n" \
            "For heads and tails:                                          bot coin\n" \
            "For an six sided dice:                          bot dice\n" \
            "For an dice with any number of sids:   bot dice 20 / any number you like"
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