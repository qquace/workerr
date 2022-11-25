import os
try:
 import keyboard, time, random
 import colorama
 import mouse
 from colorama import Fore, init
 import os
except:
 req = ["keyboard", "time", "random", "colorama", "mouse"]
 for imp in req :
  os.system(f"pip install {imp}")
 print("[!] Я скачал все нужное") 
init()
print(f"""
{Fore.LIGHTRED_EX}                             ▄▄▌ ▐ ▄▌      ▄▄▄  ▄ •▄ ▄▄▄ .▄▄▄  
{Fore.LIGHTRED_EX}                             ██· █▌▐█▪     ▀▄ █·█▌▄▌▪▀▄.▀·▀▄ █·
{Fore.LIGHTRED_EX}                            ██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
{Fore.LIGHTRED_EX}                            ▐█▌██▐█▌▐█▌.▐▌▐█•█▌▐█.█▌▐█▄▄▌▐█•█▌
{Fore.LIGHTRED_EX}                             ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀·▀  ▀ ▀▀▀ .▀  ▀
{Fore.LIGHTRED_EX}                                 tool for mineland.net
{Fore.LIGHTRED_EX}             
{Fore.LIGHTRED_EX}                      FOR LAVA+                       FOR SWEARING                  
{Fore.LIGHTRED_EX}              1 - Lava work spam (Button F8)    8 - Swear generator (Button F8) 
{Fore.LIGHTRED_EX}              2 - Lava work spam (Auto)         9 - Swear auto (chat or suffix)
{Fore.LIGHTRED_EX}              7 - Lava work generation          13 - Mega Swearing (AI)
                                                                  14 - Mega Swearing (But F8)
{Fore.LIGHTRED_EX}            
{Fore.LIGHTRED_EX}                      CHAT FLOOD                        HACKS?
{Fore.LIGHTRED_EX}              3 - Just spam                       10 - Click 10 times in sec (f8)
{Fore.LIGHTRED_EX}              4 = Random spam                     11 - Random walk
{Fore.LIGHTRED_EX}              5 = Set spam (4,6) speed (def 0.5)  12 - IAlina Flood (f8)
{Fore.LIGHTRED_EX}              6 - Invalid symbol spam
{Fore.LIGHTRED_EX}
""")
spamspeed = 0.5

balance = 0
male_s = ['пидорас','хуесос','олигофрен','бомж','раб','выблядок','примат','уебок','кастрат','подсос','хуесос','ебанат','стыд','мусор','абориген','остойник','копрофил','лузер','cцыкун','фаршмак','петух','опарыш','уебан','мусор','клоп','бомжик','жидок','кастрат','долбоеб','хуеглот','жалкий','нищий','лошпед','дегроид','сученышь','червь','глист','хуйлан','опущенец','стыд','клоун','аутист','пиздолиз','аут','еблан','еблоид','лошок','пиздабол','фембой']
male_p = ['контуженый','слабый','немощный','ебаный','cлитый','обосцанный','отсталый','тупой','подпарашный','уебищный','мерзкий','цепной']
male_r = ['твоего батю','деда твоего','батю твоего','твоего деда']
male_n = ['немощного','слабого','беспомощного','нищего','отьебаного','жалкого']

female_s = ['шлюшка','пидораска','дура','хуесоска','ебанатка','рабыня','сучка','падаль','рабыня']
female_p = ['контуженая','слабая','немощная','ебаная','отьебаная','cлитая','обосцанная','нищая','подпарашная','уебищная','цепная','дегроидная']
female_r = ['твою мать','мамку твою','бабку твою','твою бабку','свиноматку твою']
female_n = ['немощную','слабую','беспомощную','нищую','жалкую']

sv = ['бля','нахуй','ору бля','сука']

suffix_p = ['лижи ноги','глотай сперму','соси хуй','лижи яйца','бойся меня','полируй яйца','ноги лижи','терпи','пизди в мой хуй', 'лижи мой хуй']

do = ['обосцал','сжег','выебал','закопал заживо','убил','поебывал','заставил насрать себе на ебло','заставил сосать с заглотом','кислотой облил','ногами запиздил нахуй','вьебал об раму параши','ебал пока челюсть не отпадет','так активно кулаками ебашил что костяшки в кровь стер','сломал нижнюю челюсть и заставил парашу чистить язычком у себя дома','ебашил еблом об стол','заставил сглатывать сперму за каждый визг твой','вьебал хуем по челюхе','заставил шлюхой под забором побираться','отправил в роту рашистов лечить их от спермотоксикоза','сжег бля в индукционной печи','заставил вырвать себе ребра и пожарил на гриле','залил спермой','вьебал об тумбу','ножницами пырнул','вьебал об батарею','ножом выебал','мясом замороженным выебал','сделал эвтаназию','сжег и накончал на пепел','мусоровозом переехал','задушил стекловатой','заставил жрать стекло','заставил пизду себе отрезать','вьебал и вырезал почки и заставил их жрать', 'выебал и в очко просунул лопасть от вертолета', 'выебал и запихал в рот нейролептиков','изнасиловал','расчленил и выебал','сжег на жертвенном костре во имя аллаха','прирезал как свинью и сдал труп на мясокомбинат']

tebya = ['тебя', 'тя']
ya = ['я']
dot = ['отпиздил','вьебал','вьебашил', 'запиздил']

thing = ['камнями','кирпичами','арматурой','ногами','кнутом','бутылкой','своим хуем','ножом','калашом','шуруповертом','дилдаком','молотком']

popo = ['по']

potom = ['а потом']

po = ['черепушке','башке']

terp = ['ты стерпела','ты терпишь'] 
first = ["сученышь тупой вьебашил тебя шуруповертом по черепушке а потом сделал эвтаназию ", "Скули в хуй ", "Полируй яйца ртом ", "Ты в своей коммуналке зажился ", "Твоя мамаша за алкашу сосет, а ее сынок голодает и стыдиться жить, " , "Запиздил своим хуем по черепушке батю твоего, а его сынишка ", "Ты без хуя", "Ты пьешь мою сперму,", "Я харкаю тебе в рот", "Ты по жизни хуи глотаешь", "Ты спишь на полу", "Твой отец жалкий куколд который живет за счет женщины и лижет ей пизду а ты", "Убейся об стенку", "Вынеси мусор", "Слизывай", "Cосешь мой член", "Ты", "Я тя в рот епу ", "Лижи мои ноги", "Я ебу твои уши", "Ты вербально", "Я твоему отцу уретру порвал", "Из твоего рта хуями воняет", "Ты просто ","Ты играешься моим членом во рту", "Соси покорно", "У тебя хуй во рту", "Я из волос твоей матери табак сделал", "Поплачь", "Я тебе в рот сру", "Я ору", "Твоя мать тонет, не бездействуй,", "Я твою мать топлю", "Я тя захуярил, ", "Я тя в рот епу", "Лижи мои ноги", "Чисти мою обувь", "Слушай мои команды,", "Твоей матери на лицо по кд кончаю", "Твоя мать шлюха", "Лол ты блять овца ебаная", "Ору тебя только мужики потные ебут,", "Соси член смирно ебик", "Ты немощь, я твою мать ебал", "Я ебу твою мать опущеный", "Сосешь мой член нервно", "Я тебя ногами хуярю", "Ты бомжиха", "Ты с моего течешь", "Член сосешь", "Твоя батя мусорник", "В рот тя ебу", "Я твою семью сжег"]
second = ["хуерван)", "вонючий и ничтожный клоп", "свинота бля)", "скудоумная свиномразь", "чмоня", "слабый" , "жалкий раб", "глист", "терпила", "жирный пидор", "задрот ебаный", "подстилка", "спермоед", "нищая дура", "псинка", "хуесоска", "кукла ебаная", "рабынька", "соска ебаная", "куколд", "мусор", "лесбиянка слитая", "ты от плетки раком встаешь, немощь", "глотаешь мою сперму, еблан", "скулишь в хуй", "пастерша ебаная", "плеткой бью тя", "прошмандовка сцука", "ебаная хуйня", "дура ебаная", "хуйланка", "шакал", "резвая сучка", "сучка сцаная", "пидор", ", погавкай", ", гавкни сука пидор", "мой фанатик ржачный, гавкай","гондон подсосочный", "псина ебаная", "немощный раб", "сынишка проститутки", "дочка урода", "твой батек инвалид", "проститутка", "телка ебаная", "житель мусорки"]

texts = ["осамый уникальний игрокь (:", "очень крютой (:", "самий особенный игрок (:", "имеит большюю особеннасть (:", "ни злой и не обманщикь (:", "лусшчий!", "топовий (:", "самий особенний", "молодец (:", "о с о б е н н ы й", "не пляхой (:", "лусше воды (:", "всем нужин", 'афигеный (:', 'то п ч и к', 'особенный', 'лучший', 'хароший', 'топ', 'особенный', 'особенный', 'топчик', 'уникальный', 'не плохой (:', '&aу&bн&cи&5к&6а&7л&8ь&eн&4ы&2й', 'отличаеяться', 'лусший', 'топ топ', 'йыннебосо', "важный", "имеет 12 импиров (:", "кляссний игрок", 'не обманивает (:', "топчикь", "лучший", "отличаеться с 12 импирами (:"]
lavas = ['Лява', 'лявочка', 'лявка', "Лава"]

ialina = ["мужыки", "мужчинкы", "му*ыки", "муж*ки"]
antiman = ["не ну*ный пол", "не нуж*ы", "бесполезн*й пол", "не нуж*ны, женщины великий пол", "ущемл*ються в чате"]


reklama = [' vk.com/banml (смешные баны игроков (: )' ,' /ad splav (:', "", ' /ad speeds (:', "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
color = ['&e', '&b', "&a", "&e", "&c", "&6", "&d"]
chat = ['/dc', '/cc', '/cc', '/cc', '/cc', '/cc', '/cc', '/cc', '/cc', '/cc', '/cc', '/cc']
while True:
 select = input("")
 if select == "1":
  print("[!] Yout started working.")
  while True: 
    if keyboard.is_pressed('F8'):
        keyboard.send("t")
        time.sleep(0.3)
        keyboard.write(random.choice(chat) + " " + random.choice(color) + random.choice(lavas) + " " + random.choice(texts) + random.choice(reklama))
        time.sleep(0.3)
        keyboard.send("enter")
        print("Отправлено!")
        balance += 0.1
        os.system(f"title Worker / Balance: {balance}")
        print(f"{Fore.LIGHTGREEN_EX}] Ваш баланс теперь: {Fore.LIGHTGREEN_EX}{balance} руб")
        
 if select == "2":
  while True:
        keyboard.send("t")
        time.sleep(0.3)
        keyboard.write(random.choice(chat) + " " + random.choice(color) + random.choice(lavas) + " " + random.choice(texts) + random.choice(reklama))
        time.sleep(0.3)
        print("Отправлено!")
        keyboard.send("enter")
        time.sleep(random.randint(7,50))
        balance += 0.1
        os.system(f"title Worker / Balance: {balance}")
        print(f"{Fore.LIGHTGREEN_EX}] Ваш баланс теперь: {Fore.LIGHTGREEN_EX}{balance} руб")
 if select == "3":
  text = input(f"{Fore.LIGHTRED_EX}Text {Fore.LIGHTWHITE_EX}")
  time.sleep(4)
  while True:
   keyboard.send("t")
   time.sleep(0.3)
   keyboard.write(text + " " + str(random.randint(99999,999999)))
   time.sleep(0.3)
   print("Отправлено!")
   keyboard.send("enter")
   time.sleep(spamspeed)
 if select == "5":
  number = float(input("Number (In S, can use float): "))
  spamspeed = number
 if select == "4":
  while True:
   keyboard.send("t")
   time.sleep(0.3)
   keyboard.write(str(random.randint(0,999999999999)) + str(random.randint(0,999999999999)) + str(random.randint(0,999999999999))+ str(random.randint(0,999999999999)) + str(random.randint(0,999999999999)) + str(random.randint(0,999999999999)) + str(random.randint(0,999999999999)) + str(random.randint(0,999999999999)) + str(random.randint(0,999999999999))+ str(random.randint(0,999999999999)) * 10)
   time.sleep(0.3)
   print("Отправлено!")
   keyboard.send("enter")
   time.sleep(spamspeed)
 if select == "6":
  while True:
   keyboard.send("t")
   time.sleep(0.3)
   keyboard.write("🔰🔰🔰🔰🔰🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🔰🔰🔰🔰🔰🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🔰💠💠💠💠💠💠🌐🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🌐🌐🌐🌐❎❎❎☢〽❔❔‼‼⁉🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🔆⏪⏬⏬⏬⏬⏬⏬⏬®®®🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨")
   time.sleep(0.3)
   print("Отправлено!")
   keyboard.send("enter")
   time.sleep(spamspeed)
 if select == "7":
  print("[!] Yout started working.")
  while True: 
    if keyboard.is_pressed('F8'):
        keyboard.send("t")
        time.sleep(0.3)
        keyboard.write(random.choice(color) + random.choice(lavas) + " " + random.choice(texts) + random.choice(reklama))
        time.sleep(0.3)
        keyboard.send("enter")
        print("Отправлено!")
        balance += 0.1
        os.system(f"title Worker / Balance: {balance}")
        print(f"     {Fore.LIGHTGREEN_EX}] Ваш баланс теперь: {Fore.LIGHTGREEN_EX}{balance} руб")
 if select == "8":
  suffix = input("[!] Suffix:")
  print("[!] Yout started srach.")
  while True: 
    if keyboard.is_pressed('F8'):
        keyboard.send("t")
        time.sleep(0.3)
        keyboard.write(suffix + random.choice(first) + " " + random.choice(second))
        time.sleep(0.3)
        keyboard.send("enter")
        print("Отправлено!")
        time.sleep(spamspeed)
 if select == "9":
  suffix = input("[!] Suffix:")
  print("[!] Yout started srach.")
  while True:
        keyboard.send("t")
        time.sleep(0.3)
        keyboard.write(suffix + random.choice(first) + " " + random.choice(second))
        time.sleep(0.3)
        keyboard.send("enter")
        print("Отправлено!")
        time.sleep(spamspeed)
 if select == "10":
  number = int(input("     Введите сколько раз нажать за 1 секунду (НЕ БОЛЬШЕ 30, ИНАЧЕ ПИЗДА РУЛЯМ): "))
  rol = input("R or L: ")
  if number < 30:
    if rol == "L":
     while True:
      if keyboard.is_pressed('F8'):
         for i in range(10):
          mouse.click(button='left')
          print("нажато 10 раз")
    if rol == "R":
     while True:
        if keyboard.is_pressed('F8'):
         for i in range(10):
          mouse.click(button='right')
          print("нажато 10 раз")
  else:
   print("чел твоему пк пизда если больше 30")
 if select == "11":
  buttons = ["w", "a", "s", "d", "space"]
  number = int(input("     Введите количество шагов: "))
  put = number * 1.2
  time.sleep(3)
  for i in range(number):
    button = random.choice(buttons)
    print(f"     [!] Pressing {button}")
    time.sleep(1)
    keyboard.press(button)
    time.sleep(1)
    keyboard.release(button)
    time.sleep(0.5)
  print(f"     [!] Путь пройден в ~{put} блоков")
 if select == "13":
  number = int(input("Введите колво повторений: "))
  zad = float(input("Введите заддержжку: "))
  suffix = str(input("Введите суффикс: "))
  rand = random.randint(1,12)
  x = 0
  g = ""
  ranger = number
  for i in range(number):
   time.sleep(zad)
				#Жертва 2 слова
   if rand == 12:
					global result
					result = random.choice(male_p) + " " + random.choice(male_s) + " " + random.choice(ya) + " " + random.choice(tebya) + " " + random.choice(do) + " " + random.choice(terp)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
						
						
   if rand == 11:
					result = random.choice(male_p) + " " + random.choice(male_s) + " " + random.choice(suffix_p) + " " + random.choice(sv)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
						
						
   if rand == 10:
					result = random.choice(suffix_p) + " " + random.choice(female_s) + " " + random.choice(sv)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
						
						
   if rand == 9:
					result = random.choice(dot) + " " + random.choice(thing) + " " + random.choice(popo) + " " + random.choice(po) + " " + random.choice(male_r) + " " + random.choice(male_n) + " " + random.choice(terp)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
					
   if rand == 8:
					result = random.choice(female_s) + " " + random.choice(suffix_p) + " " + random.choice(female_p) + " " + random.choice(sv)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
					
   if rand == 7:
					result = random.choice(thing) + " " + random.choice(dot) + " " + random.choice(female_r) + " " + random.choice(female_n) + " " + random.choice(terp)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
					
   if rand == 6:
					result = random.choice(female_s) + " " + random.choice(female_p) + " " + random.choice(suffix_p)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
					
   if rand == 5:
					result = random.choice(male_s) + " " + random.choice(male_p) + " " + random.choice(sv)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
					
				#Родня
   if rand == 4:
					result = random.choice(male_s) + " " + random.choice(male_p) + " " + random.choice(male_r) + " " + random.choice(do) + " " + random.choice(sv)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
					
   if rand == 3:
					result = random.choice(female_s) + " " + random.choice(female_p) + " " + random.choice(female_r) + " " + random.choice(do) + " " + random.choice(sv)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
					
				#Жертве пизда
   if rand == 2:
					result = random.choice(female_s) + " " + random.choice(female_p) + " " + random.choice(dot) + " " + random.choice(tebya) + " " + random.choice(thing) + " " + random.choice(popo) + " " + random.choice(po) + " " + random.choice(potom) + " " + random.choice(do) + " " + random.choice(suffix_p) + " " + random.choice(female_s) + " " + random.choice(sv)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
					
   if rand == 1:
					result = random.choice(male_s) + " " + random.choice(male_p) + " " + random.choice(dot) + " " + random.choice(tebya) + " " + random.choice(thing) + " " + random.choice(popo) + " " + random.choice(po) + " " + random.choice(potom) + " " + random.choice(do) + " " + random.choice(suffix_p) + " " + random.choice(female_s) + " " + random.choice(sv)
					keyboard.write(suffix + result)
					x = x + 1
					keyboard.press_and_release('enter')
					print(g+' [+] Сообщение успешно отправлено! (',x,'/',ranger,')')
 if select == "12":
  suffix = input("Введите суффикс: ")
  while True: 
     if keyboard.is_pressed('F8'):
        keyboard.send("t")
        time.sleep(0.3)
        keyboard.write(suffix + random.choice(color) + random.choice(ialina) + " " + random.choice(antiman))
        time.sleep(0.3)
        keyboard.send("enter")
        print("Отправлено!")