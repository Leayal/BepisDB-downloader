from download import download
import configparser
import os.path

def menu():
    #make cfg file or txt that allows to automaticaly select option
    print("BepisDB Card Downloader - select type of card to download (enter number or use config file):")
    print("1. KK")
    print("2. AA2")
    print("3. HS")
    print("4. PH")
    print("5. AI/HS2")
    print("6. COM3D2")
    print("7. SH")
    print("8. HC")
    print("9. SVS")
    print("10. CONFIG")
    print("11. EXIT")

    selected = input()

    #make cfg file or txt that allows to automaticaly or skit + defaults are just empty- write it into documentation
    #for all of em like KK AA2 for example - kk.txt -> contains setings for that one | AA2.txt -> contains settings for that one / if the row isblank the user inoputs the data here like -> tags = long_hair; name = ; <- will be prompted toinsert name in consoleor click enter to set default
    if selected == "1":
        game = "KK"
        url = "https://db.bepis.moe/koikatsu"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            KK(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "2":
        game = "AA2"
        url = "https://db.bepis.moe/aa2"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            AA2_and_AI_HS2(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "3":
        game = "HS"
        url = "https://db.bepis.moe/honeyselect"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            HS(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "4":
        game = "PH"
        url = "https://db.bepis.moe/playhome"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            PH(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "5":
        game = "AI_HS2"
        url = "https://db.bepis.moe/aishoujo"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            AA2_and_AI_HS2(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "6":
        game = "COM3D2"
        url = "https://db.bepis.moe/com3d2"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            COM3D2(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "7":
        game = "SH"
        url = "https://db.bepis.moe/summerheat"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            SH(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "8":
        game = "HC"
        url = "https://db.bepis.moe/honeycome"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            HC(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "9":
        game = "SVS"
        url = "https://db.bepis.moe/svs"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            mode = "advanced"
            SVS(game, url, mode)
        else:
            mode = "basic"
            basic(game, url, mode)
    elif selected == "10":
        program_config()
    elif selected == "11":
        exit(0)
    else:
        print("Please select one of the correct options (1-11):")
        menu()

def KK(game, url, mode):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    print("Possible Gender: female | male")
    gender = input()
    print("Personality: (number) <Default> = Unspecified")
    print("Possible Personality: 0 = Sexy | 1 = Ojousama | 2 = Snobby | 3 = Kouhai | 4 = Mysterious | 5 = Weirdo | 6 = Yamato Nadeshiko | 7 = Tomboy | 8 = Pure | 9 = Simple | 10 = Delusional | 11 = Motherly | 12 = Big Sisterly | 13 = Gyaru | 14 = Delinquent | 15 = Wild | 16 = Wannabe | 17 = Reluctant | 18 = Jinxed | 19 = Bookish | 20 = Timid | 21 = Typical Schoolgirl | 22 = Trendy | 23 = Otaku | 24 = Yandere | 25 = Lazy | 26 = Quiet | 27 = Stubborn | 28 = Old-Fashioned | 29 = Humble | 30 = Friendly | 31 = Willful | 32 = Honest | 33 = Glamorous | 34 = Returnee | 35 = Slangy | 36 = Sadistic | 37 = Emotionless | 38 = Perfectionist")
    personality = input()
    print("Gametype: (text) <Default> = Unspecified")
    print("Possible Gametype: Base | Steam | Steam 18+ | Emotion Creators | Sunshine")
    game_type = input()
    print("Does not contain modded content: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    modded_content = input()
    print("Order by: (text) <Default> = Date Descending")
    print("You can Order by: popularity | dateasc (Date Ascending)")
    order_by = input()
    print("Show hidden: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_hidden = input()
    print("Show only featured: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_only_featured = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, gender = gender, personality = personality, game_type = game_type, modded_content = modded_content, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured, start_from = start_from)
    if (download_return == 1):
        menu()

def AA2_and_AI_HS2(game, url, mode):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    if(game == "AA2"):
        print("Possible Gender: female | male")
    else:
        print("Possible Gender: Female | Male | Futanari")
    gender = input()
    print("Personality: (number) <Default> = Unspecified")
    if(game == "AA2"):
        print("Possible Personality: 0 = Lively | 1 = Delicate | 2 = Cheerful | 3 = Quiet | 4 = Playful | 5 = Frisky | 6 = Kind | 7 = Joyful | 8 = Ordinary | 9 = Irritated | 10 = Harsh | 11 = Sweet | 12 = Creepy | 13 = Reserved | 14 = Dignified | 15 = Aloof | 16 = Smart | 17 = Genuine | 18 = Mature | 19 = Lazy | 20 = Manly | 21 = Gentle | 22 = Positive | 23 = Otaku | 24 = Savage | 25 = Cadet | 26 = Caring | 27 = Schemer | 28 = Carefree | 29 = Warm | 30 = Cold (Male Aloof) | 31 = AA1 Quiet | 32 = Methodical | 33 = AA1 Empress (HF) | 34 = AA1 Big Sister | 35 = Silent | 36 = AA1 Empress (aa2g) | 37 = AA1 Brave | 38 = AA1 Pure | 40 = Robot | 41 = Sly | 42 = Russian | 43 = Timid | 44 = Whimsical | 45 = Salamanderman | 46 = Callous | 50 = Servent | 51 = OuterSpace | 52 = Apricot | 53 = Wise | 54 = Graceful | 55 = Trendy | 58 = AA1 Ditzy | 59 = AA1 Aloof | 60 = AA1 Affable | 61 = AA1 Calm | 62 = AA1 Tense | 63 = AA1 Rough | 64 = AA1 Sweet | 65 = AA1 Mistress | 66 = AA1 Selfish | 67 = Bekloppt | 68 = AA1 Casual | 69 = Open-eye Joyful | 70 = AA1 Pleasant | 71 = Gynoid (Sweet) | 72 = Open-eye Quiet | 73 = Scholarly | 75 = Cynical | 76 = AA1 Manly | 77 = AA1 Humble | 78 = Succubus (Mature) | 79 = AA1 Violent | 80 = Analytical | 81 = Despair | 82 = Future | 83 = Kuma | 84 = Liar | 85 = Robot (Male) | 90 = Big Brother | 95 = Polite | 96 = Energetic | 97 = Eccentric | 98 = AA1 Cold | 99 = AA1 Soft | 100 = AA1 Eloquent | 101 = AA1 Obscene | 102 = AA1 Faithful | 103 = Professor | 104 = AA1 Handsome | 105 = AA1 Dark | 106 = Twisted | 107 = Cowardly | 108 = Haughty | 110 = Ice | 111 = Hero | 112 = Artsy | 113 = Silent (Male) | 114 = Mute | 115 = Mute+ | 116 = Arrogant | 131 = Bael | 132 = Fumi | 133 = Space Case | 134 = Wild | 135 = Delinquent | 136 = Jinxed | 137 = Chuuni | 138 = Motherly | 139 = Tomboy | 140 = Yandere | 141 = Gyaru | 142 = Bookish | 143 = Archaic | 144 = Enigma | 145 = Kouhai | 146 = Emotionless | 147 = Bashful | 148 = Sadistic | 149 = Geek")
    else:
        print("Possible Personality: 0 = Emotionless | 1 = Friendly | 2 = Confident | 3 = Selfish | 4 = Lazy | 5 = Positive")
    personality = input()
    print("Order by: (text) <Default> = Date Descending")
    print("You can Order by: popularity | dateasc (Date Ascending)")
    order_by = input()
    print("Show hidden: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_hidden = input()
    print("Show only featured: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_only_featured = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, gender = gender, personality = personality, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured, start_from = start_from)
    if (download_return == 1):
        menu()

def HS(game, url, mode):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    print("Possible Gender: female | male")
    gender = input()
    print("Personality: (number) <Default> = Unspecified")
    print("Possible Personality: 0 = Cheerful | 1 = Tsundere | 2 = Gentle | 3 = Withdrawn | 4 = Yandere | 5 = Easygoing | 6 = Strict | 7 = Boyish | 8 = Energetic | 9 = Diligent | 10 = Active | 11 = Sincere | 12 = Bewitching")
    personality = input()
    print("Gametype: (text) <Default> = Unspecified")
    print("Possible Gametype: neo | Classic")
    game_type = input()
    print("Order by: (text) <Default> = Date Descending")
    print("You can Order by: popularity | dateasc (Date Ascending)")
    order_by = input()
    print("Show hidden: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_hidden = input()
    print("Show only featured: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_only_featured = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, gender = gender, personality = personality, game_type = game_type, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured, start_from = start_from)
    if (download_return == 1):
        menu()

def PH(game, url, mode):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Order by: (text) <Default> = Date Descending")
    print("You can Order by: popularity | dateasc (Date Ascending)")
    order_by = input()
    print("Show hidden: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_hidden = input()
    print("Show only featured: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_only_featured = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured, start_from = start_from)
    if (download_return == 1):
        menu()

def COM3D2(game, url, mode):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Preset type: (text) <Default> = Unspecified")
    print("Possible Preset type: outfit | body | all")
    preset_type = input()
    print("Order by: (text) <Default> = Date Descending")
    order_by = input()
    print("Show hidden: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_hidden = input()
    print("Show only featured: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_only_featured = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, preset_type = preset_type, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured, start_from = start_from)
    if (download_return == 1):
        menu()

def SH(game, url, mode):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Order by: (text) <Default> = Date Descending")
    print("You can Order by: popularity | dateasc (Date Ascending)")
    order_by = input()
    print("Show hidden: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_hidden = input()
    print("Show only featured: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_only_featured = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured, start_from = start_from)
    if (download_return == 1):
        menu()

def HC(game, url, mode):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    print("Possible Gender: Female | Male | Futanari")
    gender = input()
    print("Order by: (text) <Default> = Date Descending")
    print("You can Order by: popularity | dateasc (Date Ascending)")
    order_by = input()
    print("Show hidden: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_hidden = input()
    print("Show only featured: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_only_featured = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, gender = gender, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured, start_from = start_from)
    if (download_return == 1):
        menu()

def SVS(game, url, mode):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    print("Possible Gender: Female | Male | Futanari")
    gender = input()
    print("Order by: (text) <Default> = Date Descending")
    print("You can Order by: popularity | dateasc (Date Ascending)")
    order_by = input()
    print("Show hidden: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_hidden = input()
    print("Show only featured: (checkbox) - enter '1' to check - 0 or nothig to leave unchecked <Default>")
    show_only_featured = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, gender = gender, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured, start_from = start_from)
    if (download_return == 1):
        menu()

def basic(game, url, mode):
    mode = mode
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Start from page number: (number) <Default> = blank")
    start_from = input()
    download_return = download(mode = mode, game = game, url = url, name = name, tags = tags, start_from = start_from)
    if (download_return == 1):
        menu()

def create_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'browser_visibility': '1','card_download_interval': '5','website_load_interval': '5','close_browser_after_download': '0','close_program_after_download': '1'}
    config['USER'] = {'browser_visibility': '1','card_download_interval': '5','website_load_interval': '5','close_browser_after_download': '0','close_program_after_download': '1'}
    with open('config.ini', 'w') as conf:
        config.write(conf)

def program_config():
    #loading config
    #...
    config = configparser.ConfigParser()
    config.read("config.ini")
    user_cfg = config["USER"]
    value = None
    print("PROGRAM CONFIGURATION EDITOR (1-5) - Enter for default.")
    print("1. Enable/Disable browser visibility(GUI).")
    print("2. Set card download interval.")
    print("3. Wait for website to load interval.")
    print("4. Close browser after download.")
    print("4. Close program after download.")
    print("6. Display default values.") #displays DEFAULT config
    print("7. Display current values.")
    print("8. Back to main menu.")
    choice = input()
    if(choice == "1"):
        print("Enter [number {1/0} <default: 1>]")
        value = input()
        if(value == None):
            value = 1
        user_cfg['browser_visibility'] = str(value)
        with open('config.ini', 'w') as conf:
            config.write(conf)
        program_config()
    elif(choice == "2"):
        print("Enter [number {integer} <default: 5>]")
        value = input()
        if(value == None):
            value = 5
        user_cfg['card_download_interval'] = str(value)
        with open('config.ini', 'w') as conf:
            config.write(conf)
        program_config()
    elif (choice == "3"):
        print("Enter [number {integer} <default: 5>]")
        value = input()
        if(value == None):
            value = 5
        user_cfg['website_load_interval'] = str(value)
        with open('config.ini', 'w') as conf:
            config.write(conf)
        program_config()
    elif (choice == "4"):
        print("Enter [number {1/0} <default: 1>]")
        print("If browser_visibility is set to 0 and close_browser_after_download is set to 0, the program will not quit! You have to kill the process manually.")
        value = input()
        if(value == None):
            value = 1
        user_cfg['close_browser_after_download'] = str(value)
        with open('config.ini', 'w') as conf:
            config.write(conf)
        program_config()
    elif (choice == "5"):
        print("Enter [number {1/0} <default: 1>]")
        value = input()
        if(value == None):
            value = 1
        user_cfg['close_program_after_download'] = str(value)
        with open('config.ini', 'w') as conf:
            config.write(conf)
        program_config()
    elif (choice == "6"):
        print("Default values form config.ini")
        config.read('config.ini')
        print("browser_visibility: ",config['DEFAULT']['browser_visibility'])
        print("card_download_interval: ",config['DEFAULT']['card_download_interval'])
        print("website_load_interval: ",config['DEFAULT']['website_load_interval'])
        print("close_after_download: ",config['DEFAULT']['close_browser_after_download'])
        print("close_after_download: ",config['DEFAULT']['close_program_after_download'])
        program_config()
    elif (choice == "7"):
        print("Current [USER] values form config.ini")
        config.read('config.ini')
        print("browser_visibility: ", config['USER']['browser_visibility'])
        print("card_download_interval: ", config['USER']['card_download_interval'])
        print("website_load_interval: ", config['USER']['website_load_interval'])
        print("close_after_download: ", config['USER']['close_browser_after_download'])
        print("close_after_download: ", config['USER']['close_program_after_download'])
        program_config()
    elif (choice == "8"):
        menu()
    else:
        print("Please select one of the correct options (1-8):")
        program_config()

def main():
    #check if config exists, if not create one
    config = os.path.exists("config.ini")
    if(config == False):
        create_config()
        print("Config file not found... Generating new one...")
    menu()

if __name__ == "__main__":
    main()
