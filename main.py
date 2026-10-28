import os
import time
import webbrowser
from tkinter import messagebox
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
import asyncio
import random
import threading
from rich.prompt import Prompt
import msvcrt
import json
import sys
import pygame

console = Console()

plakats = """###########################################################################################################
###########################################################################################################
#############Gtii1f0######1ii1##########1iit8iiiiif#######8iii8tiiiii@#######1ii1#iiiiiiiiiiiiiiiiiG#######
#########              ;##   .##########   .G      .######G   C.      f######.   @                 t#######
#######C   :########@.   #   .##########   ,G   i    #####G   C.       :#####.   @   i0000000000000@#######
#######G   ,##############   .##########   ,G   G#    f###0   C.   #t    ####.   @   :fffffffffC###########
###########8CLLG8.. .;0###   .##########   ,G   G##:    ##0   C.   ###    G##.   #             .###########
#####################,   #    ##########   ,G   G###C    8G   C.   ####,   :#.   #   :LLLLLLLLLC###########
#######G    ########8    #;     0###@G     tG   G#####    .   C.   #####t        @   .i;;;;;;;;i;;iC#######
#########i             f###1.            .f#G   G######,      C.   ######8       @                 t#######
##############0CLC8##########Gt;:,..,:;t0###@LLL@#######0LLLLL@CLLL########LLLLLC#LLLLLLLLLLLLLLLLL8#######
###########################################################################################################
###########################################################################################################"""
plakats2 = """
###########################################################################################################
################################################ ПОДДЕРЖКА ################################################
#############Gtii1f0######1ii1##########1iit8iiiiif#######8iii8tiiiii@#######1ii1#iiiiiiiiiiiiiiiiiG#######
#########              ;##   .##########   .G      .######G   C.      f######.   @                 t#######
#######C   :########@.   #   .##########   ,G   i    #####G   C.       :#####.   @   i0000000000000@#######
#######G   ,##############   .##########   ,G   G#    f###0   C.   #t    ####.   @   :fffffffffC###########
###########8CLLG8.. .;0###   .##########   ,G   G##:    ##0   C.   ###    G##.   #             .###########
#####################,   #    ##########   ,G   G###C    8G   C.   ####,   :#.   #   :LLLLLLLLLC###########
#######G    ########8    #;     0###@G     tG   G#####    .   C.   #####t        @   .i;;;;;;;;i;;iC#######
#########i             f###1.            .f#G   G######,      C.   ######8       @                 t#######
##############0CLC8##########Gt;:,..,:;t0###@LLL@#######0LLLLL@CLLL########LLLLLC#LLLLLLLLLLLLLLLLL8#######
###########################################################################################################
###########################################################################################################
"""

def plakat():
    print(plakats)

def save_game():
    save_data = {
        "ochko": ochko,
        "pomit": pomit,
        "pomitp": pomitp,
        "musor": musor,
        "dro": dro,
        "igr": igr,
        "drc": drc,
        "dss": dss,
        "rib": rib,
        "rrib": rrib,
        "opencr": opencr,
        "gamecorp": gamecorp,
        "day": day,
        "posilka": posilka,
        "data_base": data_base,
        "chh": chh,
        "dayav": dayav,
        "dayav2": dayav2,
        "ddv": ddv,
        "mmv": mmv,
        "mmv2": mmv2,
        "imya": imya,
        "gvozd": gvozd,
        "police": police,
        "tolea_sdan": tolea_sdan,
        "psiholog": psiholog,
        "paranoya_day": paranoya_day,
        "paranoya_shown": paranoya_shown,
        "koncovka_active": koncovka_active,
        "mearephone": mearephone,
        "tolya_dialog": tolya_dialog,
        "path_tolya": path_tolya,
        "path_police": path_police,
        "dike": dike,
        "juing": juing,
        "daytolya": daytolya,
        "gamecorpscam": gamecorpscam
    }
    with open("save.json", "w") as f:
        json.dump(save_data, f)

def load_game():
    global ochko, pomit, pomitp, daytolya, musor, gamecorpscam, dro, igr, drc, dss, rib, juing, rrib, opencr, gamecorp, dike, day, posilka, data_base, chh, dayav, ddv, mmv, dayav2, mmv2, imya, gvozd, police, tolea_sdan, psiholog, paranoya_day, paranoya_shown, koncovka_active, mearephone, tolya_dialog, path_tolya, path_police
    try:
        with open("save.json", "r") as f:
            save_data = json.load(f)
            ochko = save_data.get("ochko", 0)
            pomit = save_data.get("pomit", 1)
            pomitp = save_data.get("pomitp", 1)
            musor = save_data.get("musor", 1)
            dro = save_data.get("dro", 0)
            igr = save_data.get("igr", 1)
            drc = save_data.get("drc", 0)
            dss = save_data.get("dss", 0)
            rib = save_data.get("rib", 0)
            rrib = save_data.get("rrib", 0)
            opencr = save_data.get("opencr", 0)
            gamecorp = save_data.get("gamecorp", 0)
            day = save_data.get("day", 0)
            posilka = save_data.get("posilka", 0)
            data_base = save_data.get("data_base", 0)
            chh = save_data.get("chh", 0)
            dayav = save_data.get("dayav", 0)
            dayav2 = save_data.get("dayav2", 0)
            ddv = save_data.get("ddv", 0)
            mmv = save_data.get("mmv", 0)
            mmv2 = save_data.get("mmv2", 0)
            imya = save_data.get("imya", 0)
            gvozd = save_data.get("gvozd", 0)
            police = save_data.get("police", 0)
            tolea_sdan = save_data.get("tolea_sdan", 0)
            psiholog = save_data.get("psiholog", 0)
            paranoya_day = save_data.get("paranoya_day", 0)
            paranoya_shown = save_data.get("paranoya_shown", 0)
            koncovka_active = save_data.get("koncovka_active", 0)
            mearephone = save_data.get("mearephone", 0)
            tolya_dialog = save_data.get("tolya_dialog", 0)
            path_tolya = save_data.get("path_tolya", 0)
            path_police = save_data.get("path_police", 0)
            dike = save_data.get("dike", 0)
            juing = save_data.get("juing", 0)
            daytolya = save_data.get("daytolya", 0)
            gamecorpscam = save_data.get("gamecorpscam", 0)
            return True
    except FileNotFoundError:
        return False

nazvanie = "Youhe Bain 1: Others' Circumstances"

for i in range(6):
    os.system('cls' if os.name == 'nt' else 'clear')
    if i % 2 == 0:
        print("Starting..")
    elif i % 3 == 0:
        print("Starting...")
    else:
        print("Starting.")
    time.sleep(0.1)

answer = messagebox.askyesno("Поддержка", "Вы хотите поддержать разработчиков? (вам начислится ваш донат умноженный на 200 рублей на карту после доната)")

def opensite():
    webbrowser.open("https://vexikoff.xyz/fatdesign/")
    time.sleep(1.5)
    webbrowser.open("https://vexikoff.xyz/")
    time.sleep(1.5)
    webbrowser.open("https://calcux.vexikoff.xyz/")
    time.sleep(1.5)
    webbrowser.open("https://avle.vexikoff.xyz/")
    time.sleep(1.5)
    webbrowser.open("https://www.youtube.com/@rgglidemusic")
    time.sleep(1.5)
    webbrowser.open("https://www.donationalerts.com/r/vexikoff")
    time.sleep(1.5)

if answer:
    opensite()
    print("ЭСЛИ ТЫ НИЧЕГО НЕ ЗАДОНАТИШЬ ТО ТЫ ГЕЙ!")
else:
    print("ЖЛОБ ТУПОЙ! ИДИ ИГРАЙ В СВОЕ ГОВНО ТЕБЕ ЖАЛКО РАЗРАБА ДАЖЕ ПОДДЕРЖАТЬ")

pomit = 1
pomitp = 1
musor = 1
dro = 0
ochko = 0
imya = 0
gvozd = 0
in_action = False

igr = 1
drc = 0
dss = 0
zvonok = 0
rib = 0
rrib = 0
zvv = False
opencr = 0
gamecorp = 0
day = 0
posilka = 0
data_base = 0
chh = 0
dayav2 = 0
dayav = 0
ddv = 0
mmv = 0
mmv2 = 0
police = 0
tolea_sdan = 0
psiholog = 0
paranoya_day = 0
paranoya_shown = 0
koncovka_active = 0
mearephone = 0
tolya_dialog = 0
path_tolya = 0
path_police = 0
dike = 0
juing = 0
daytolya = 0
domtolya = 0
gamecorpscam = 0
cooldowns = {
    "pomit": 0,
    "pomitp": 0,
    "musor": 0,
    "dro": 0,
    "igr": 0,
    "rib": 0,
    "dayav": 0,
    "dayav2": 25,
}

load_game()

def titry():
    global plakats2
    console.print(nazvanie)
    time.sleep(2.5)
    for bukva in plakats2:
        print(bukva, end='', flush=True)
        time.sleep(0.003)
    time.sleep(2.5)
    console.print("Создатели:")
    time.sleep(2.5)
    console.print("[link=https://github.com/vexikoff]vexikoff[/]")
    time.sleep(2.5)
    console.print("[link=https://github.com/vexikoff]Maxim304[/]")
    time.sleep(2.5)
    console.print("[link=https://qwen.ai/]Qwen[/]")
    time.sleep(2.5)
    console.print("")
    time.sleep(2.5)
    console.print("Идеи:")
    time.sleep(2.5)
    console.print("[link=https://github.com/vexikoff]vexikoff[/]")
    time.sleep(2.5)
    console.print("[link=https://github.com/vexikoff]Maxim304[/]")
    time.sleep(2.5)
    console.print("[link=https://qwen.ai/]Qwen[/]")
    time.sleep(2.5)
    console.print("[link=https://gemini.google.com/]Gemini[/]")
    time.sleep(2.5)
    console.print("[link=https://mistral.ai/]Mistral[/]")
    time.sleep(2.5)
    console.print("MaxGPT")
    time.sleep(2.5)
    console.print("")
    time.sleep(2.5)
    console.print("Музыка:")
    time.sleep(2.5)
    console.print("[link=https://github.com/vexikoff]vexikoff[/]")
    time.sleep(2.5)
    console.print("")
    time.sleep(10)
    pygame.mixer.music.stop()

def koncovka_neutral():
    global koncovka_active, tolea_sdan, day, ochko, zvv
    zvv = 1
    koncovka_active = 2
    save_game()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    console.print(f"[green]День {day}.[/]")
    time.sleep(3)
    console.print(f"[green]День {day + 1}.[/]")
    time.sleep(2.5)
    console.print(f"[green]День {day + 2}.[/]")
    time.sleep(2)
    console.print(f"[green]День {day + 3}.[/]")
    time.sleep(1.5)
    console.print(f"[green]День {day + 4}.[/]")
    time.sleep(1)
    console.print(f"[green]День {day + 5}.[/]")
    time.sleep(0.5)
    console.print(f"[green]День {day + 6}.[/]")
    time.sleep(2)
    console.print("[yellow]Вы поняли, что жизнь наладилась и все всегда будет прежним. Изменить мир нету шанса.[/]")
    time.sleep(2)
    console.print("Вы пытаетесь изменить мир. Не получается.")
    time.sleep(2.5)
    console.print("[yellow]Все отвечают как обычно, толю не найти.[/]")
    time.sleep(2.5)
    console.print("Нигде. Никого. Все. Отвечают. По. Работе.")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    pygame.mixer.init()
    pygame.mixer.music.load('3.wav')
    pygame.mixer.music.play(-1)
    console.print("")
    console.print("[white]КОНЦОВКА 3 ИЗ 5: Нейтрал[/]")
    console.print("")
    time.sleep(3)
    console.print("[white]Вы выбрали сторону закона.[/]")
    time.sleep(2.5)
    console.print("[white]Но в этом мире закон не защищает.[/]")
    time.sleep(2.5)
    console.print("[white]Он добрый.[/]")
    time.sleep(2.5)
    console.print("[white]Он не хотел убивать. Он хотел работать.[/]")
    time.sleep(3)
    console.print("")
    console.print("[yellow]Статистика:[/]")
    console.print(f"[yellow]Прожито дней: {day + 6}[/]")
    console.print(f"[yellow]Заработано очков: {ochko}[/]")
    console.print(f'[yellow]Куплено "очень крутых и полезных" унитазов: {juing}[/]')
    time.sleep(5)
    console.print("")
    console.print("[white]Нажмите Enter чтобы выйти...[/]")
    input()
    titry()
    os._exit(0)

def koncovka_predatel(name):
    global koncovka_active, tolea_sdan, day, ochko, zvv
    zvv = 1
    koncovka_active = 1
    save_game()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    console.print(f"[red]День {day}. 2:47 ночи.[/]")
    time.sleep(3)
    console.print("Вы просыпаетесь от странного звука.")
    time.sleep(2.5)
    console.print("Кто-то скребётся в дверь. Тихо. Потом громче.")
    time.sleep(2.5)
    console.print("[yellow]Скрип... Скрип... Скрип...[/]")
    time.sleep(2)
    console.print("Вы пытаетесь встать. Ноги не слушаются.")
    time.sleep(2.5)
    console.print("[yellow]Звук металла по замку.[/]")
    time.sleep(2.5)
    console.print("Холодный пот течёт по спине.")
    time.sleep(2.5)
    console.print("[yellow]Щёлк.[/]")
    time.sleep(3)
    console.print("Дверь медленно открывается.")
    time.sleep(3)
    console.print("В проёме силуэт. Тёмный. Неподвижный.")
    time.sleep(3)
    console.print("Вы узнаёте это лицо.")
    time.sleep(3)
    console.print(f"[red]{name}[/]")
    time.sleep(3)
    console.print("В его руке блеск лезвия.")
    time.sleep(2.5)
    console.print("Он делает шаг вперёд.")
    time.sleep(2.5)
    console.print("Вы пытаетесь крикнуть.")
    time.sleep(2.5)
    console.print("Звук не идёт из горла.")
    time.sleep(3)
    console.print("[red]Вспышка боли.[/]")
    time.sleep(2)
    console.print("[red]Холод.[/]")
    time.sleep(2)
    console.print("[red]Темнота.[/]")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    pygame.mixer.init()
    pygame.mixer.music.load('1.wav')
    pygame.mixer.music.play(-1)
    console.print("")
    console.print("[white]КОНЦОВКА 1 ИЗ 5: ПРЕДАТЕЛЬ[/]")
    console.print("")
    time.sleep(3)
    console.print("[white]Вы выбрали сторону закона.[/]")
    time.sleep(2.5)
    console.print("[white]Но в этом мире закон не защищает.[/]")
    time.sleep(2.5)
    console.print("[white]Он помнил ваше лицо.[/]")
    time.sleep(2.5)
    console.print("[white]Он помнил ваш адрес.[/]")
    time.sleep(3)
    console.print("")
    console.print("[yellow]Статистика:[/]")
    console.print(f"[yellow]Прожито дней: {day}[/]")
    console.print(f"[yellow]Заработано очков: {ochko}[/]")
    console.print(f'[yellow]Куплено "очень крутых и полезных" унитазов: {juing}[/]')
    time.sleep(5)
    console.print("")
    console.print("[white]Нажмите Enter чтобы выйти...[/]")
    input()
    titry()
    os._exit(0)

def koncovka_police():
    global koncovka_active, tolea_sdan, day, ochko, zvv
    zvv = 1
    koncovka_active = 3
    save_game()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    console.print(f"[red]День {day}. 12:47.[/]")
    time.sleep(3)
    console.print("Вы просыпаетесь от странного звука.")
    time.sleep(2.5)
    console.print("Кто-то скребётся в дверь. Тихо. Потом громче.")
    time.sleep(2.5)
    console.print("[yellow]Скрип... Скрип... Скрип...[/]")
    time.sleep(2)
    console.print("[red]Полиция[/]")
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    pygame.mixer.init()
    pygame.mixer.music.load('5.wav')
    pygame.mixer.music.play(-1)
    console.print("")
    console.print("[white]КОНЦОВКА 5 ИЗ 5: СКАМ ДОМА[/]")
    console.print("")
    time.sleep(3)
    console.print("")
    console.print("[yellow]Статистика:[/]")
    console.print(f"[yellow]Прожито дней: {day}[/]")
    console.print(f"[yellow]Заработано очков: {ochko}[/]")
    console.print(f'[yellow]Куплено "очень крутых и полезных" унитазов: {juing}[/]')
    time.sleep(5)
    console.print("")
    console.print("[white]Нажмите Enter чтобы выйти...[/]")
    input()
    titry()
    os._exit(0)

def koncovka_data():
    global koncovka_active, tolea_sdan, day, ochko, zvv
    zvv = 1
    koncovka_active = 4
    save_game()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    pygame.mixer.init()
    pygame.mixer.music.load('4.wav')
    pygame.mixer.music.play(-1)
    console.print("")
    console.print("[white]КОНЦОВКА 2 ИЗ 5: СКАМ ДАТА БАЗОЙ[/]")
    console.print("")
    time.sleep(3)
    console.print("")
    console.print("[yellow]Статистика:[/]")
    console.print(f"[yellow]Прожито дней: {day}[/]")
    console.print(f"[yellow]Заработано очков: {ochko}[/]")
    console.print(f'[yellow]Куплено "очень крутых и полезных" унитазов: {juing}[/]')
    time.sleep(5)
    console.print("")
    console.print("[white]Нажмите Enter чтобы выйти...[/]")
    input()
    titry()
    os._exit(0)

def koncovka_notdata():
    global koncovka_active, tolea_sdan, day, ochko, zvv
    zvv = 1
    koncovka_active = 5
    save_game()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    pygame.mixer.init()
    pygame.mixer.music.load('6.wav')
    pygame.mixer.music.play(-1)
    console.print("")
    console.print("[white]КОНЦОВКА 4 ИЗ 5: СКАМ УГРОЗОЙ[/]")
    console.print("")
    time.sleep(3)
    console.print("")
    console.print("[yellow]Статистика:[/]")
    console.print(f"[yellow]Прожито дней: {day}[/]")
    console.print(f"[yellow]Заработано очков: {ochko}[/]")
    console.print(f'[yellow]Куплено "очень крутых и полезных" унитазов: {juing}[/]')
    time.sleep(5)
    console.print("")
    console.print("[white]Нажмите Enter чтобы выйти...[/]")
    input()
    titry()
    os._exit(0)

async def main():
    global pomit, pomitp, dike, musor, dro, igr, dss, drc, ochko, zvonok, zvv, rib, rrib, opencr, gamecorp, day, posilka, data_base, chh, dayav, dayav2, mmv, mmv2, imya, ddv, gvozd, in_action, tolea_sdan, psiholog, paranoya_day, paranoya_shown, koncovka_active, mearephone, tolya_dialog, path_tolya, path_police, police
    
    global cooldowns
    cooldowns["call"] = time.time() + random.uniform(15.0, 40.0)

    current_time = time.time()
    
    if pomit == 0:
        cooldowns["pomit"] = current_time + random.uniform(10.0, 50.0)
    if pomitp == 0:
        cooldowns["pomitp"] = current_time + random.uniform(10.0, 100.0)
    if musor == 0:
        cooldowns["musor"] = current_time + random.uniform(10.0, 200.0)
    if dro == 0:
        cooldowns["dro"] = current_time + random.uniform(20.0, 60.0)
    if igr == 0:
        cooldowns["igr"] = current_time + random.uniform(100.0, 240.0)
    if rib == 0 and rrib == 1:
        cooldowns["rib"] = current_time + random.uniform(60.0, 200.0)
    if dayav == 0 and dss == 1 and day <= 3:
        cooldowns["dayav"] = current_time + random.uniform(10.0, 60.0)
    if day > 4 and dayav2 == 0 and ddv == 1 and mmv2 >= 1:
        cooldowns["dayav2"] = current_time + random.uniform(10.0, 50.0)
    
    cooldowns["call"] = current_time + random.uniform(15.0, 40.0)
    
    while True:
        current_time = time.time()
        
        if pomit == 0 and current_time >= cooldowns["pomit"]:
            pomit = 1
            save_game()
        if pomitp == 0 and current_time >= cooldowns["pomitp"]:
            pomitp = 1
            save_game()
        if musor == 0 and current_time >= cooldowns["musor"]:
            musor = 1
            save_game()
        if dro == 0 and current_time >= cooldowns["dro"]:
            dro = 1
            save_game()
        if igr == 0 and current_time >= cooldowns["igr"]:
            igr = 1
            save_game()
        if rib == 0 and rrib == 1 and current_time >= cooldowns["rib"]:
            rib = 1
            save_game()
        if dayav == 0 and dss == 1 and day <= 3 and current_time >= cooldowns["dayav"]:
            dayav = 1
            save_game()
        if day > 4 and dayav2 == 0 and ddv == 1 and mmv2 >= 1 and current_time >= cooldowns["dayav2"]:
            dayav2 = 1
            save_game()
            
        if ochko >= 32 and not in_action and current_time >= cooldowns["call"]:
            available_calls = []
            if opencr == 0:
                available_calls.append(1)
            if gamecorp == 0:
                available_calls.append(2)
            if dss == 0:
                available_calls.append(3)
            if dss == 1 and day >= 2 and posilka == 0:
                available_calls.append(4)
            if chh == 0 and day >= 3:
                available_calls.append(5)
            if mmv == 0 and day >= 4:
                available_calls.append(6)
            if data_base == 1 and police == 0 and day >= 5:
                available_calls.append(7)
            if tolea_sdan == 1 and psiholog == 0:
                available_calls.append(8)
            if dike == 0:
                available_calls.append(9)
            
            if len(available_calls) > 0:
                zvv = True
                zvonok = 1
                answer_call = messagebox.askyesno("Звонок", "Вам поступил звонок. Принять?")
                zvonok = 0
                cooldowns["call"] = current_time + random.uniform(15.0, 40.0)
                
                ra = random.choice(available_calls)
                
                ldk = ""
                if drc == 1:
                    ldk = "Кстати у вас большой член."
                if answer_call and ra > 0:
                    if ra == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(1.2)
                        console.print("OpenCreate: Привет! Вам позвонила компания OpenCreate по поводу камер в вашем доме. Почему вы не зарегестрировали их в нашу компанию и не поставили пароль?")
                        time.sleep(1.5)
                        console.print("Вы: А почему я должен это сделать?")
                        time.sleep(1.7)
                        console.print(f"OpenCreate: Ради безопасности, без паролей камеры доступны всем людям, так-же нам по нашей публичной оферте и политике кондефендициальности наших камер. Мы можем смотреть в вашу камеру, эсли будет пароль не сможем. {ldk}")
                        time.sleep(1.7)
                        if drc == 1:
                            console.print("Вы: ОТКУДА ВЫ ЗНАЕТЕ? ВАМ НЕ СТЫДНО СЛЕДИТЬ ЗА МНОЙ?! СТАЛКЕРИНГ! Я ПОДАМ НА ВАС В СУД!")
                        else:
                            console.print("Вы: ВСМЫСЛЕ МОЖЕТЕ СМОТРЕТЬ? ПОДАМ В СУД")
                        time.sleep(1.7)
                        console.print("OpenCreate: В суде у вас ничего не получится, все законно. Пожалуйста не повышайте тон. Просто поставьте пароль за 10 очков и все!")
                        time.sleep(1.7)
                        console.print("Вы: ПЛАТИТЬ? КАКОГО ХЕРА ЗА ЭТО БЕРЕТСЯ ПЛАТА?")
                        console.print("Вы: Ладно, я подумаю")
                        console.print("[green]Выбор: [/]")
                        console.print("[green]1. Оплатить[/]")
                        console.print("[red]2. Отказаться[/]")
                        console.print("[white]3. Узнать подробнее[/]")
                        otzz6 = Prompt.ask(
                            "ВЫБИРАЙ:", 
                            choices=["1", "2", "3"], 
                            default="1"
                        )
                        console.print("OpenCreate: Т.к. мы предоставляем услугу, и нам нужно на что то жить.")
                        time.sleep(1.7)
                        if otzz6 == "1":
                            console.print("Вы: я готов")
                            time.sleep(1.7)
                            if ochko < 10:
                                console.print(f"OpenCreate: Спасибо! У вас недостаточно средств. но для вас у меня скидка {ochko} очков!")
                                ochko = 0
                            else:
                                ochko -= 10
                            opencr = 1
                            save_game()
                            console.print("OpenCreate: Спасибо! Сейчас мы все сделаем слушайте внимательнее...")
                            console.print("*Далее вы подключали камеру вместе с сотрудником...*")
                            time.sleep(2)
                            console.print("OpenCreate: Готово! Теперь ваши камеры защищены.")
                        elif otzz6 == "2":
                            time.sleep(1.7)
                            console.print("Вы: Я НЕ БУДУ ПЛАТИТЬ ИДИТЕ НАХУЙ")
                            console.print("OpenCreate: Как я понял, вы отказываетесь от нашей услуги. До свидания.")
                            if drc == 1:
                                console.print("OpenCreate: Кстати, не стесняйтесь показывать ваш ч, у вас он большой и красивый!")
                        elif otzz6 == "3":
                            time.sleep(1.7)
                            console.print("OpenCreate: Подробнее: Мы подключимся к вам и будем вас сопровождать, дадим секретный ключ который вы подключите к камере а потом его измените через CreateHub на нашем сайте OpenCreate, по политике мы не сможем к вам смотреть!")
                            console.print("[green]Выбор: [/]")
                            console.print("[green]1. Оплатить[/]")
                            console.print("[red]2. Отказаться[/]")
                            otzz10 = Prompt.ask(
                                "ВЫБИРАЙ:", 
                                choices=["1", "2", "3"], 
                                default="1"
                            )
                            time.sleep(1.7)
                            if otzz10 == "1":
                                console.print("Вы: я готов")
                                time.sleep(1.7)
                                if ochko < 10:
                                    console.print(f"OpenCreate: Спасибо! У вас недостаточно средств. но для вас у меня скидка {ochko} очков!")
                                    ochko = 0
                                else:
                                    ochko -= 10
                                opencr = 1
                                save_game()
                                console.print("OpenCreate: Спасибо! Сейчас мы все сделаем слушайте внимательнее...")
                                console.print("*Далее вы подключали камеру вместе с сотрудником...*")
                                time.sleep(2)
                                console.print("OpenCreate: Готово! Теперь ваши камеры защищены.")
                            elif otzz10 == "2":
                                time.sleep(1.7)
                                console.print("Вы: Я НЕ БУДУ ПЛАТИТЬ ИДИТЕ НАХУЙ")
                                console.print("OpenCreate: Как я понял, вы отказываетесь от нашей услуги. До свидания.")
                                if drc == 1:
                                    console.print("OpenCreate: Кстати, не стесняйтесь показывать ваш ч, у вас он большой и красивый!")
                        time.sleep(1.7)

                    elif ra == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(1.2)
                        console.print("Gamecorp o ration: Привет! Вам позвонила компания Gamecorp o ration по поводу ваших проектов. Как насчёт зарегстрировать их в нашу компанию и защитить?")
                        time.sleep(1.5)
                        console.print("Вы: А зачем защищать?")
                        time.sleep(1.7)
                        console.print(f"Gamecorp o ration: Ради вашего удовольствия, Мы защиту поставим, так ещё и заплатим вам. Мы рассмотрим ваши проекты. {ldk}")
                        time.sleep(1.7)
                        console.print(f"Вы: Нууу я подумаю")
                        time.sleep(1.7)
                        console.print(f"Gamecorp o ration: Мы будем брать 98% от прибыли каждый раз когда кто то покупает игру и платить вам 2%")
                        time.sleep(1.7)
                        console.print(f"Вы: 2 ПРОЦЕНТА? ВЫ НЕ ЗАЖРАЛИСЬ?")
                        time.sleep(1.7)
                        console.print(f"Gamecorp o ration: Таковы условия, игра будет стоит 1000 очков")
                        time.sleep(1.7)
                        console.print(f"Вы: СКОЛЬКО СКОЛЬКО? ЛЮДИ ЗА ТАКУЮ ЦЕНУ МОГУТ СДЕЛАТЬ НА ВСЮ СЕМЬЮ СТОЛ И ВКУСНО ПОЖРАТЬ МОЯ ИГРА УЛЬТРА ДЕЛЮКС ПО ВАШЕМУ?")
                        time.sleep(1.7)
                        console.print(f"Gamecorp o ration: Мы ещё сделаем ДЛС за 2000 очков и отдать вам 2.1% от каждой покупки ДЛС вы не против?")
                        time.sleep(1.7)
                        console.print(f"Gamecorp o ration: ИИИИИИИИИИ кстати за защиту 5000 очков")
                        time.sleep(1.7)
                        console.print(f"Вы: Хмммммм много, хотя деньги...")
                        console.print("[green]Выбор: [/]")
                        console.print("[green]1. Согласится[/]")
                        console.print("[red]2. Отказатся[/]")
                        otzz3 = Prompt.ask(
                            "ВЫБИРАЙ:", 
                            choices=["1", "2"], 
                            default="1"
                        )
                        gamecorp = 1
                        save_game()
                        if otzz3 == "1":
                            time.sleep(1.2)
                            console.print("Вы: Ладно я соглашаюсь")
                            time.sleep(1.7)
                            console.print(f"Gamecorp o ration: Отлично! Пришлите ваши проекты и мы их рассмотрим.")
                            time.sleep(1.2)
                            console.print("[green]Выбор: [/]")
                            console.print("[green]1. Скинуть проект[/]")
                            console.print("[red]2. Передумать[/]")
                            console.print("[white]3. Узнать подробнее[/]")
                            otzz4 = Prompt.ask(
                                "ВЫБИРАЙ:", 
                                choices=["1", "2", "3"], 
                                default="1"
                            )
                            if otzz4 == "1":
                                time.sleep(1.2)
                                console.print("Вы: Скинул!")
                                time.sleep(1.7)
                                console.print(f"Gamecorp o ration: Отлично! Нам нужен примерно месяц.")
                                time.sleep(2)
                                console.print(f"[white]Спустя месяц...")
                                time.sleep(2)
                                console.print(f"Gamecorp o ration: Это снова Gamecorp o ration Мы рассмотрели вашу игру и защитили теперь заплатите 250 очков")
                                time.sleep(2)
                                console.print(f"Вы: Но вы же сказали 5000 очков")
                                time.sleep(2)
                                console.print(f"Gamecorp o ration: У нас настроение просто хорошое ПЛАТИ ПОКА СУММА НЕ УВЕЛИЧИЛАСЬ ТО 7500 ОЧКОВ!")
                                time.sleep(1.2)
                                console.print("[green]Выбор: [/]")
                                console.print("[green]1. Заплатить[/]")
                                console.print("[red]2. Не платить[/]")
                                otzz5 = Prompt.ask(
                                    "ВЫБИРАЙ:", 
                                    choices=["1", "2"], 
                                    default="1"
                                )
                                if otzz5 == "1":
                                    if ochko >= 250:
                                        ochkoP = random.randint(200, 1200)
                                        ochko += ochkoP
                                        save_game()
                                        time.sleep(1.2)
                                        console.print("Вы: Заплатил!")
                                        time.sleep(1.7)
                                        console.print(f"Gamecorp o ration: Игра уже продаётся! Спасибо за сотрудничество!")
                                        time.sleep(2)
                                        console.print(f"[white]Спустя месяц вы заработали {ochkoP} очков![/]")
                                    else:
                                        time.sleep(1.2)
                                        console.print("Вы: У меня нет стольки очков!")
                                        time.sleep(1.7)
                                        console.print(f"Gamecorp o ration: Не переживайте, у нас для вас скидка. Сегодня ровно {ochko} очков!")
                                        time.sleep(1.2)
                                        console.print("Вы: Покупаю!!!!!")
                                        console.print(f"Gamecorp o ration: Игра уже продаётся! Спасибо за сотрудничество!")
                                        time.sleep(2)
                                        console.print(f"[white]Спустя месяц...[/]")
                                        time.sleep(2)
                                        console.print(f"Gamecorp o ration: Это снова Gamecorp o ration Мы рассмотрели вашу игру и защитили теперь заплатите {ochko * 4 + 30} очков")
                                        time.sleep(2)
                                        console.print(f"Вы: Но вы же сказали {ochko} очков")
                                        time.sleep(2)
                                        console.print(f"Gamecorp o ration: У нас настроение теперь плохое ПЛАТИ Я СКАЗАЛ ИНАЧЕ СУММА УВЕЛИЧИТСЯ ДО {ochko * 8 + 30} ОЧКОВ!")
                                        time.sleep(2)
                                        console.print(f"Вы: Во что я вляпался...")
                                        ochko = 0
                                        save_game()
                            elif otzz4 == "2":
                                console.print(f"Вы: Я передумал")
                                time.sleep(0.4)
                                console.print(f"Gamecorp o ration: но вы же согласились!")
                                time.sleep(0.6)
                                console.print(f"Вы: А баба яга обосралась короч всё пока")
                            elif otzz4 == "3":
                                console.print(f"Вы: А можно поподробнее?")
                                time.sleep(1)
                                console.print(f"Gamecorp o ration: Вы скинете нам ваши проекты, мы их рассмотрим, защитим, вы скинете нам деньги а потом выставим на продажу и заплатим вам 2% от каждой покупки.")
                                console.print("[green]Выбор: [/]")
                                console.print("[green]1. Скинуть проект[/]")
                                console.print("[red]2. Передумать[/]")
                                console.print("[white]3. Узнать подробнее[/]")
                                otzz4 = Prompt.ask(
                                    "ВЫБИРАЙ:", 
                                    choices=["1", "2", "3"], 
                                    default="1"
                                )
                                
                        elif otzz3 == "2":
                            console.print(f"Вы: ДА ПОШЛИ ВЫ Я ЗА СПРАВЕДЛИВОСТЬ!")
                            time.sleep(0.7)
                            console.print("Вы: *Сбрасывает звонок*")

                    elif ra == 3:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(1.2)
                        console.print("Sunne CL: Здравствуйте мы компания Sunne CL, хотим купить у вас рекламу которую вы повесите на окно.")
                        time.sleep(1.5)
                        console.print("Вы: А зачем на окно?")
                        time.sleep(1.7)
                        console.print(f"Sunne CL: Для распростронения нашего ПО, калькуляторы, рулетка. все чисто 100% бля буду")
                        time.sleep(1.7)
                        console.print(f"Вы: Нууу я подумаю")
                        time.sleep(1.2)
                        console.print("[green]Выбор: [/]")
                        console.print("[green]1. Согласится[/]")
                        console.print("[red]2. Отказатся[/]")
                        console.print("[white]3. Узнать подробнее[/]")
                        otzz = Prompt.ask(
                            "Ответ:", 
                            choices=["1", "2", "3"], 
                            default="1"
                        )
                        if otzz == "1":
                            time.sleep(1.2)
                            console.print("Вы: Я соглашаюсь, вы пришлете плакат?")
                            time.sleep(1.7)
                            console.print(f"Sunne CL: Конечно! Он вам придет в течении 2 дней. И после того как мы убедимся что вы его повесили. Сначало подпишите электронный документ.")
                            time.sleep(1.2)
                            console.print("[green]Выбор: [/]")
                            console.print("[green]1. Согласится[/]")
                            console.print("[red]2. Отказатся[/]")
                            console.print("[white]3. Узнать подробнее[/]")
                            otzz2 = Prompt.ask(
                                "Ответ:", 
                                choices=["1", "2", "3"], 
                                default="1"
                            )
                            if otzz2 == "1":
                                console.print("Вы: *Подписывает...*")
                                time.sleep(1.2)
                                console.print("Вы: Готово! Можно узнать подробности?")
                                time.sleep(1.7)
                                console.print(f"Sunne CL: Конечно! Мы будем платить вам 1 очко в год, и еще вы не можете отказатся от нашей услуги в течении года.")
                                time.sleep(1.7)
                                console.print("Вы: ЧЕ ТАК МАЛО??!!! ГОД?!?! ВО ЧТО Я ВЛИП...")
                                console.print("Вы: *Сбрасывает звонок*")
                                console.print("Открыт новый режим: Рыбалка")
                                rib = 1
                                rrib = 1
                                time.sleep(1.7)
                                dss = 1
                                save_game()
                            if otzz2 == "2":
                                console.print("Вы: Я отказываюсь, всего доброго")
                                console.print("Вы: *Сбрасывает звонок*")
                            if otzz2 == "3":
                                console.print("Вы: Можно узнать подробности?")
                                time.sleep(1.7)
                                console.print("Sunne CL: Конечно! Мы будем платить вам 1 очко в год, и еще вы не можете отказатся от нашей услуги в течении года.")
                                time.sleep(1.7)
                                console.print("Вы: Я отказываюсь, всего доброго")
                                console.print("Вы: *Сбрасывает звонок*")
                        if otzz == "2":
                            console.print("Вы: Я отказываюсь, всего доброго")
                            console.print("Вы: *Сбрасывает звонок*")
                        if otzz == "3":
                            console.print("Вы: Можно узнать подробности?")
                            time.sleep(1.7)
                            console.print("Sunne CL: Конечно! Мы будем платить вам 1 очко в год, и еще вы не можете отказатся от нашей услуги в течении года.")
                            time.sleep(1.4)
                            console.print("Вы: Я отказываюсь, всего доброго")
                            console.print("Вы: *Сбрасывает звонок*")
                                
                        time.sleep(0.7)
                    elif ra == 4:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        console.print("(все данные в игре вымышленны, не являются настоящими данными)")
                        time.sleep(1.2)
                        console.print("Sunne CL: Здравствуйте мы компания Sunne CL, мы о вашем контракте с рекламой на окно.")
                        time.sleep(1.5)
                        console.print("Вы: че надо? я сегодня злой")
                        time.sleep(1.7)
                        console.print(f"Sunne CL: К вам пришел плакат на почту, в стадии ожидания. Готовы вешать? Подготовились, надеюсь?")
                        time.sleep(1.7)
                        console.print("Вы: вроде бы")
                        time.sleep(1.7)
                        console.print(f"Sunne CL: Почта XurtIMail, отдел 839. Заберите плакат. Скажите ваши данные для удостоверения на почте. Требования.")
                        time.sleep(1.7)
                        console.print("Вы: щас скажу...")
                        time.sleep(1.7)
                        console.print("[green]Выбор: [/]")
                        console.print("[green]1. Сказать настоящие данные[/]")
                        console.print("[white]2. Сказать данные брата[/]")
                        console.print("[red]3. Соврать[/]")
                        otzz7 = Prompt.ask(
                            "Ответ:", 
                            choices=["1", "2", "3"], 
                            default="1"
                        )
                        if otzz7 == "1":
                            time.sleep(1.7)
                            console.print("Вы: Дмитрий Иванов Иванович, ИНН 390214677129")
                            time.sleep(1.7)
                            console.print(f"Sunne CL: Подождите вношу данные...")
                            time.sleep(2.7)
                            console.print(f"Sunne CL: Готово! Сегодня вы уже сможете забрать! Подкопи 80 очков, пригодятся перед походом на почту.")
                            time.sleep(1.7)
                            console.print(f"Sunne CL: До свидания.")
                            time.sleep(1.7)
                            console.print("Вы: До свидания.")
                            time.sleep(1.7)
                            posilka = 2
                            imya = 1
                            save_game()

                        elif otzz7 == "2":
                            time.sleep(1.7)
                            console.print("Вы: Иван Борисов Иванович, ИНН 194224477149")
                            time.sleep(1.7)
                            console.print(f"Sunne CL: Подождите вношу данные...")
                            time.sleep(2.7)
                            console.print(f"Sunne CL: Готово! Сегодня вы уже сможете забрать! Подкопи 80 очков, пригодятся перед походом на почту.")
                            time.sleep(1.7)
                            console.print(f"Sunne CL: До свидания.")
                            time.sleep(1.7)
                            console.print("Вы: До свидания.")
                            time.sleep(1.7)
                            posilka = 3
                            imya = 2
                            save_game()

                        elif otzz7 == "3":
                            time.sleep(1.7)
                            console.print("Вы: Алекс Джинг, ИНН 123412341234")
                            time.sleep(1.7)
                            console.print(f"Sunne CL: Подождите вношу данные...")
                            time.sleep(2.7)
                            console.print(f"Sunne CL: Готово! Сегодня вы уже сможете забрать! Подкопи 80 очков, пригодятся перед походом на почту.")
                            time.sleep(1.7)
                            console.print(f"Sunne CL: До свидания.")
                            time.sleep(1.7)
                            console.print("Вы: До свидания.")
                            time.sleep(1.7)
                            posilka = 4
                            imya = 3
                            save_game()

                    elif ra == 5:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        console.print(f"(все данные в игре вымышленны, не являются настоящими данными)")
                        time.sleep(1.2)
                        console.print(f"bankunex: Здраствуйте! ваша карта заблокирована по ошибке, чтобы разблокировать её, вам нужно будет ввести ваши данные.")
                        time.sleep(1.5)
                        console.print(f"Вы: Опа мошенник мне как раз скучно")
                        time.sleep(1.7)
                        console.print(f"bankunex: мы не мошенники мы проффесионалы которым можно доверять. {ldk}")
                        time.sleep(1.7)
                        console.print(f"Вы: Нуууууу...")
                        console.print("[green]Выбор: [/]")
                        console.print("[green]1. Ввести данные[/]")
                        console.print("[yellow]2. Поприкалыватся[/]")
                        console.print("[red]3. Сбросить трубку[/]")
                        otzz8 = Prompt.ask(
                            "ВЫБИРАЙ:", 
                            choices=["1", "2", "3"], 
                            default="1"
                        )
                        chh = 1
                        save_game()
                        if otzz8 == "1":
                            console.print(f"Вы: Номер карты 6715 8147 6701 7135")
                            time.sleep(1.7)
                            console.print(f"bankunex: А 3 цифры сзади?")
                            time.sleep(1.7)
                            console.print(f"Вы: 047")
                            time.sleep(1.7)
                            console.print(f"bankunex: Спасибо что повёлся ой тоесть дал все данные карта разблокируется в ближайшие 2 часа")
                            time.sleep(1.7)
                            console.print(f"[red]ты посмотрел на свои счет и там 0 очков после этого звонка...[/]")
                            ochko = 0
                            save_game()
                        elif otzz8 == "2":
                            console.print(f"Вы положили телефон внутри кастрюли и начал долбить в него ложкой")
                            time.sleep(1.7)
                            console.print(f"bankunex: АААААААААА! ВЫ ЧТО ДЕЛАЕТЕ?")
                            time.sleep(1.7)
                            console.print(f"трубка сброшена...")
                        elif otzz8 == "3":
                            console.print(f"Вы: Да да кончено короч идитединафиг ")
                            time.sleep(1.7)
                            console.print(f"Вы сбросили трубку.")
                        ddv = 1
                        save_game()
                    elif ra == 6:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(1.2)
                        console.print("Неизвестный: дарова срочно кидай мне 1000 очков на балик быстро")
                        time.sleep(2.5)
                        console.print("Вы: почему я должен кидать 1000 очков?")
                        time.sleep(2.5)
                        console.print("Неизвестный: а то твоя хата подлетит как ракета")
                        time.sleep(2.5)
                        console.print("Вы: всмысле?")
                        time.sleep(2.5)
                        console.print(f"Вы: Нуууууу...")
                        console.print("[green]Выбор: [/]")
                        console.print("[green]1. Скинуть[/]")
                        console.print("[red]2. Отказатся[/]")
                        console.print("[yellow]3. Поприкалыватся[/]")
                        otzz9 = Prompt.ask(
                            "ВЫБИРАЙ:", 
                            choices=["1", "2", "3"], 
                            default="1"
                        )
                        if otzz9 == "1":
                            console.print("Вы: скинул")
                            time.sleep(2.5)
                            if ochko < 1000:
                                console.print(f"Неизвестный: ооо вижуууу, но почему там не 1000 а {ochko}")
                                time.sleep(2.5)
                                console.print("Вы: у меня не было больше")
                                ochko = 0 
                            else:
                                console.print(f"Неизвестный: ооо вижуууу поккаааа")
                            time.sleep(2.5)
                        elif otzz9 == "2":        
                            console.print("Вы: кароче иди нафиг машенник")
                            time.sleep(2.5)
                            console.print(f"Неизвестный: мни на приору тонироват не хватаит выручии пжж")
                            time.sleep(2.5)
                            console.print("[green]Выбор: [/]")
                            console.print("[green]1. Скинуть[/]")
                            console.print("[red]2. Отказатся[/]")
                            otzz9 = Prompt.ask(
                                "ВЫБИРАЙ:", 
                                choices=["1", "2"], 
                                default="1"
                            )
                            if otzz9 == "1":
                                console.print("Вы: скинул")
                                time.sleep(2.5)
                                console.print(f"Неизвестный: ооо вижуууу поккаааа")
                                time.sleep(2.5)
                                console.print("Вы: пока")
                                time.sleep(2.5)
                                if ochko >= 1000:
                                    ochko -= 1000
                                else:
                                    ochko = 0
                            elif otzz9 == "2":
                                console.print(f"Неизвестный: бро ты знаешь что я к тибе домой приеду")
                                time.sleep(2.5)
                                console.print("Вы: мне посрать")
                                time.sleep(2.5)
                                koncovka_predatel("Неизвестный")

                        
                            
                        elif otzz9 == "3":        
                            time.sleep(2.5)
                            console.print(f"Неизвестный: бро ты знаешь что я к тибе домой приеду")
                            time.sleep(2.5)
                            console.print("Вы: *вы засунули телефон в кастрюлю и бьете молотком по ней*")
                            time.sleep(2.5)
                            console.print(f"Неизвестный: ААА ЧИ ТЭ ДЕЛААЭЭШЩ!?")
                            time.sleep(2.5)
                            console.print(f"Вы сбросили трубку.")
                            mmv2 = 2
                        dayav = 1
                        mmv = 1
                        mmv2 = 1
                        save_game()
                    elif ra == 7:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        console.print(f"(все данные в игре вымышленны, не являются настоящими данными)")
                        time.sleep(1.2)
                        console.print("Полиция: Здравствуйте, это полиция.")
                        time.sleep(2.5)
                        console.print("Вы: Что вам надо?")
                        time.sleep(2.5)
                        console.print("Полиция: Мы ищем Смирнова Анатолия Андреевича, Толю кароче. Вы его видели? Имели с ним дело?")
                        time.sleep(2.5)
                        console.print("Вы: А что он сделал и кто он?")
                        time.sleep(2.5)
                        console.print("Полиция: Он Хакер")
                        time.sleep(2.5)
                        console.print(f"Вы: Нуууууу...")
                        console.print("[green]Выбор: [/]")
                        console.print("[green]1. Сдать[/]")
                        console.print("[green]2. Сказать что не видел и узнать информацию.[/]")
                        console.print("[red]3. Сказать что не видел[/]")
                        otzz11 = Prompt.ask(
                            "ВЫБИРАЙ:", 
                            choices=["1", "2", "3"], 
                            default="1"
                        )
                        if otzz11 == "1":
                            time.sleep(2.5)
                            console.print("Вы: Да, видел. Он работал в почте. Его HP номер - 7-2L-C1-1032")
                            time.sleep(2.5)
                            console.print("Полиция: Спасибо.")
                            time.sleep(2.5)
                            tolea_sdan = 1
                            path_police = 1
                            save_game()
                        elif otzz11 == "2":
                            time.sleep(2.5)
                            console.print("Вы: Не видел, а что он сделал? Какое лицо?")
                            time.sleep(2.5)
                            console.print("Полиция: Такой старый мужик, он взломал базу данных Полиции округа Миноиро")
                            time.sleep(2.5)
                            console.print("Вы: Окей, эсли увижу - позвоню!")
                            time.sleep(2.5)
                            console.print("На вас накатило чувство, как будто вам стоило бы позвонить толе, но у тебя нету MearePhone-а, телефон для даркнета. Надо бы купить..")
                            time.sleep(2.5)
                            path_police = 2
                            save_game()
                        elif otzz11 == "3":
                            time.sleep(2.5)
                            console.print("Вы: Не видел.")
                            time.sleep(2.5)
                            path_police = 3
                            save_game()
                        police = 1
                        save_game()
                    elif ra == 8:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(1.2)
                        console.print("Вы: Здравствуйте, на меня наступило чувство тревоги. Пожалуйста помогите!")
                        time.sleep(2.5)
                        console.print("Психолог: Этот мир не будет прежним...")
                        time.sleep(3.5)
                        console.print("Вы: Всмысле?...")
                        time.sleep(4.5)
                        psiholog = 1
                        save_game()
                    elif ra == 9:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(1.2)
                        console.print('Díkè Níngjǐn: Здраствуйте это Díkè Níngjǐn компания мы звоним поводу умного унитаза 3000 "Juing Orus 3000"')
                        time.sleep(3.5)
                        console.print("Вы: Что вам надо")
                        time.sleep(2.5)
                        console.print("Díkè Níngjǐn: Вы обновили прошивку? Это прошивко срочно надо ставить.")
                        time.sleep(3.5)
                        console.print(f"Вы: Нуууууу...")
                        console.print("[green]Выбор: [/]")
                        console.print("[green]1. Сказать что прошил[/]")
                        console.print("[green]2. Сказать что у меня обычный унитаз[/]")
                        console.print("[red]3. Поприкалыватся[/]")
                        otzz12 = Prompt.ask(
                            "ВЫБИРАЙ:", 
                            choices=["1", "2", "3"], 
                            default="1"
                        )
                        if otzz12 == "1":
                            console.print(f"Вы: Да прошил останьте.")
                            time.sleep(2.5)
                            dike = 1
                            save_game()
                        elif otzz12 == "2":
                            console.print("Вы: У МЕНЯ ОБЫЧНРЫЙ УНИТАЗ ОТСТАНЬТЕ")
                            time.sleep(2.5)
                            console.print("Díkè Níngjǐn: ТОГДА КУПИТЕ НАШ НОВЫЙ УНИТАЗ ПО ССЫЛК—")
                            time.sleep(0.5)
                            console.print("*Звонок оборвался*")
                            time.sleep(2.5)
                            dike = 2
                            save_game()
                        elif otzz12 == "3":
                            console.print("Вы: ná nátoElda súya kemen lówi úvokarë lya atalyë engwë lya calamindo náavë. a egor na dhaug mello, na i thand, i 'urug vallen dancol.")
                            time.sleep(2.5)
                            console.print("Díkè Níngjǐn: ...")
                            time.sleep(3.5)
                    else:
                        console.print("Вы упустили важное")
                    
                    await asyncio.sleep(1.5)
                    zvv = False
        
        await asyncio.sleep(0.1)

async def tolyapath2():
    global path_tolya, tolya_dialog, day, daytolya, data_base, zvv, domtolya, ochko, imya, gamecorpscam, koncovka_active
    while True:
        if path_tolya == 2 and tolya_dialog == 1 and zvv == False:
            zvv = True
            if day >= daytolya + 2 and domtolya != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1.2)
                console.print('Вы просыпаетесь от стука в дверь, там Толя')
                time.sleep(2.5)
                console.print('Толя: бро нам надо быстрее сваливать в место безопаснее. Ко мне. Чтоб лавку не прикрыли.')
                time.sleep(2.5)
                console.print(f"Вы: Нуууууу...")
                console.print("[green]Выбор: [/]")
                console.print("[green]1. К нему домой[/]")
                console.print("[red]2. Остатся[/]")
                otzz = Prompt.ask(
                    "ВЫБИРАЙ:", 
                    choices=["1", "2"], 
                    default="1"
                )
                if otzz == "1":
                    console.print('Вы: Ну поехали к тебе быстрее!')
                    time.sleep(2.5)
                    console.print(f"Толя: Поехали садись в Tahoe.")
                    time.sleep(2.5)
                    console.print('*Вы уезжаете к нему домой*')
                    time.sleep(2.5)
                    domtolya = 1
                    save_game()
                elif otzz == "2":
                    console.print('Вы: Я не поеду, я останусь')
                    time.sleep(2.5)
                    console.print(f"Толя: Ладно, попробуем через HP.")
                    time.sleep(2.5)
                    console.print('*Вы остаетесь*')
                    time.sleep(2.5)
                    domtolya = 2
                    save_game()
            elif day >= daytolya + 4 and domtolya == 1:
                console.print('Вы просыпаетесь от голоса, Толя зовет вас скамить')
                time.sleep(2.5)
                if data_base == 1:
                    console.print("Вам начислено 200 очков.")
                    ochko += 200
                    save_game()
                    time.sleep(2.5)
                    console.print('Толя: Эй погна скамить Sunne, пора уже')
                    time.sleep(2.5)
                    console.print('Вы: Ну и как?')
                    time.sleep(2.5)
                    console.print('Толя: Будем шантажировать и угрожать.')
                    time.sleep(2.5)
                    console.print('Вы: Ну впринципе мне нравится.')
                    time.sleep(2.5)
                    console.print('Толя: Окей, завтра обсудим.')
                    time.sleep(2.5)
                else:
                    console.print("Вам начислено 300 очков.")
                    ochko += 300
                    save_game()
                    time.sleep(2.5)
                    console.print('Толя: Эй погна зажимать, пора уже')
                    time.sleep(2.5)
                    console.print('Вы: Ну и кого?')
                    time.sleep(2.5)
                    console.print('Толя: Вроде есть вредная компания такая называется вроде Gamecorp o ration.')
                    time.sleep(2.5)
                    console.print('Вы: Слышал такое, как скамить будем?')
                    time.sleep(2.5)
                    console.print('Толя: Мы им заплатим деньги все запишем а потом по их политике их же и засудим, круто придумал я?')
                    time.sleep(2.5)
                    console.print('Вы: Ну впринципе мне нравится, как раз 300 очков завалялось')
                    time.sleep(2.5)
                    console.print('Толя: Окей, завтра обсудим.')
                    time.sleep(2.5)

            elif day >= daytolya + 4 and domtolya == 2:
                console.print('Вы просыпаетесь от звонка на ДаркНет номер.')
                time.sleep(2.5)
                if data_base == 1:
                    time.sleep(2.5)
                    console.print('Толя: Эй последний раз предупреждаю, инфа прилетела что тебя уже ищут.')
                    time.sleep(2.5)    
                    console.print('Вы: Всмысле? На какое имя?')  
                    time.sleep(2.5)    
                    if imya == 1:
                        console.print("Толя: На данные Дмитрий Иванов Иванович, ИНН 390214677129.")
                        time.sleep(2.5) 
                        console.print('Вы: Зря я на свое имя плакат заказывал...')
                        time.sleep(2.5)
                        console.print("Толя: Понимаю, бывает. Но тебе надо ехать ко мне.")
                        time.sleep(2.5)
                    elif imya == 2:
                        console.print("Толя: На данные Иван Борисов Иванович, ИНН 194224477149.")
                        time.sleep(2.5) 
                        console.print('Вы: Зря я на имя брата плакат заказывал...')
                        time.sleep(2.5)
                        console.print("Толя: Понимаю, бывает. Но тебе надо ехать ко мне БЕЗ БРАТА.")
                        time.sleep(2.5)
                    elif imya == 3:
                        console.print("Толя: На данные Алекс Джинг, ИНН 123412341234/")
                        time.sleep(2.5) 
                        console.print('Вы: О это мои выдуманные данные! Круто!')
                        time.sleep(2.5)
                        console.print("Толя: Но тебе все равно надо ехать ко мне домой.")
                        time.sleep(2.5)
                    console.print("Толя: Ты поедешь ко мне домой?")
                    time.sleep(2.5)
                    console.print(f"Вы: Нуууууу...")
                    console.print("[green]Выбор: [/]")
                    console.print("[green]1. К нему домой[/]")
                    console.print("[red]2. Остатся[/]")
                    otzz2 = Prompt.ask(
                        "ВЫБИРАЙ:", 
                        choices=["1", "2"], 
                        default="1"
                    )
                    time.sleep(2.5)
                    if otzz2 == "1":
                        domtolya = 1
                        save_game()
                        console.print("Толя: Молодец, уверен это правильный выбор. Завтра сделаем.")
                        time.sleep(2.5)
                        console.print(f"Толя: Поехали садись в Tahoe.")
                        time.sleep(2.5)
                        console.print('*Вы уезжаете к нему домой*')
                        time.sleep(2.5)
                        domtolya = 1
                        save_game()
                    elif otzz2 == "2":
                        domtolya = 3
                        save_game()
                        console.print("Толя: Ладно, твой выбор. Завтра свяжемся.")
                        time.sleep(2.5)

            elif day >= daytolya + 6 and domtolya == 1 and gamecorpscam == 0:
                if domtolya == 1:
                    console.print('Вы просыпаетесь от голоса ночью.')
                elif domtolya == 2 or domtolya == 3:
                    console.print('Вы просыпаетесь от звонка на MearePhone, Толя')
                time.sleep(1.5)
                console.print(f"Толя: Вставай, пора обсуждать и начинать скамить.")
                if data_base == 0:
                    time.sleep(2)
                    console.print('Толя: Ты должен будешь включить запись и диктофон.')
                    time.sleep(2)
                    console.print(f"Вы: Диктофон на телефоне или где?")
                    time.sleep(2)
                    console.print('Толя: На телефоне, не тяни время. Быстрее.')
                    time.sleep(2)
                    console.print(f"Вы: Все, начинаю. надо им заплатить?")
                    time.sleep(2.5)
                    if domtolya == 1:
                        console.print('Толя дал вам MicroPhone')
                    time.sleep(2)
                    console.print(f"Звонок на +7 495-22...")
                    time.sleep(2)
                    console.print(f"Gamecorp o ration: Здравствуйте, ваш вопрос?")
                    time.sleep(2)
                    console.print(f"Вы: Я хочу защитить игру с помощью вас")
                    time.sleep(1.7)
                    console.print(
                        f"Gamecorp o ration: Конечно! Мы сможем вам игру защитить.")
                    time.sleep(1.7)
                    console.print(f"Вы: Сама игра скоко стоить будет")
                    time.sleep(1.7)
                    console.print(f"Gamecorp o ration: ИИИИИИгра будет стоит 1000 очков")
                    time.sleep(1.7)
                    console.print(
                        f"Вы: СКОЛЬКО СКОЛЬКО? ЛЮДИ ЗА ТАКУЮ ЦЕНУ МОГУТ СДЕЛАТЬ НА ВСЮ СЕМЬЮ СТОЛ И ВКУСНО ПОЖРАТЬ МОЯ ИГРА УЛЬТРА ДЕЛЮКС ПО ВАШЕМУ?")
                    time.sleep(1.7)
                    console.print(
                        f"Gamecorp o ration: Мы ещё сделаем ДЛС за 2000 очков и отдать вам 2.1% от каждой покупки ДЛС вы не против?")
                    time.sleep(1.7)
                    console.print(f"Gamecorp o ration: ИИИИИИИИИИ кстати за защиту 5000 очков")
                    time.sleep(1.7)
                    console.print(f"Вы: Хмммммм...")
                    console.print("[green]Выбор: [/]")
                    console.print("[green]1. Согласится[/]")
                    otzz3 = Prompt.ask(
                        "ВЫБИРАЙ:",
                        choices=["1"],
                        default="1"
                    )
                    if otzz3 == "1":
                        time.sleep(1.7)
                        console.print(
                            f"Вы: Я соглашаюсь. Сколько будет стоить?")
                        time.sleep(1.7)
                        console.print(
                            f"Gamecorp o ration: 200 очков. ")
                        time.sleep(1.7)
                        console.print(
                            f"Вы: Оплатил")
                        time.sleep(1.7)
                        console.print(f"Gamecorp o ration: Игра уже продаётся! Спасибо за сотрудничество!")
                        time.sleep(3)
                        console.print(
                            f"Gamecorp o ration:Мы рассмотрели вашу игру и защитили теперь заплатите {200 * 4 + 30} очков")
                        time.sleep(2)
                        console.print(f"Вы: Но вы же сказали 200 очков")
                        time.sleep(2)
                        console.print(
                            f"Gamecorp o ration: У нас настроение теперь плохое ПЛАТИ Я СКАЗАЛ ИНАЧЕ СУММА УВЕЛИЧИТСЯ ДО {200 * 8 + 30} ОЧКОВ!")
                        time.sleep(2)
                        console.print(f"Вы: не хочу.")
                        time.sleep(2)
                        console.print(
                            f"Gamecorp o ration: НУ И ИДИ НАХУЙ ТОГДА АЗАЗХАХАХХ ПОВЕЛСЯ ОЙ ТОЕСТЬ ОТКАЗАЛСЯ")
                        time.sleep(2)
                    console.print(
                        f"Толя: Молодец, теперь нам надо сделать бэкап их условий использования и политики...")
                    time.sleep(2)
                    console.print(
                        f"Толя: Сделал! Теперь нам надо им позвонить и угрожать")

                    time.sleep(2)
                    console.print(f"Gamecorp o ration: Здравствуйте, ваш очередной вопрос?")
                    time.sleep(2)
                    console.print(f"Вы: У нас есть все видеозаписи и бэкапы. Платите нам 5000 очков или мы подадим в суд с доказательствами, там сюсюкатся не будут.")
                    time.sleep(1.7)
                    console.print(
                        f"Gamecorp o ration: ААА!!!! ВСМЫСЛЕее!!!!???? ЩАСС ЗАПЛАУЧУ ПОДОЖДИее ТОЛЬКО НЕ В СУД НЕЕТ!")
                    time.sleep(1.7)
                    console.print(f"Вы: У меня настроение теперь плохое ПЛАТИ Я СКАЗАЛ ИНАЧЕ СУММА УВЕЛИЧИТСЯ ДО {3000 * 3 + 30} ОЧКОВ!")
                    time.sleep(1.7)
                    console.print(f"Gamecorp o ration: СКОЛЬКО НЕЕЕТ ЩАС ПОДОЖДИ")
                    time.sleep(1.7)
                    console.print(
                        f"Вы: ПЛАТИ Я СКАЗАЛ ИНАЧЕ СУММА УВЕЛИЧИТСЯ ДО {3000 * 5 + 30} ОЧКОВ!")
                    time.sleep(1.7)
                    console.print(
                        f"Gamecorp o ration: Плачу плачу все перевел")
                    time.sleep(1.7)
                    console.print(
                        f"[white]+ 3000 очков[/]")
                    ochko += 3000
                    save_game()
                    time.sleep(1.7)
                    console.print(
                        f"Вы: А ЧЕ ТОЛЬКО 3000 ОЧКОВ? Я СКАЗАЛ ПЛАТИ {3000 * 3 + 30} ИНАЧЕ СУММА УВЕЛИЧИТСЯ ДО {3000 * 5 + 30} ОЧКОВ!")
                    time.sleep(1.7)
                    console.print(
                        f"Gamecorp o ration: ЛАДНО ЛАДНО ЛАДНО")
                    time.sleep(1.7)
                    console.print(
                        f"[white]+ 9030 очков[/]")
                    time.sleep(1.7)
                    console.print(
                        f"Вы: Спасибо. ПОКА.")
                    time.sleep(1.7)
                    gamecorpscam = 1
                    ochko += 9030
                    save_game()
                else:
                    console.print('Толя: Ты должен будешь позвонить Sunne CL.')
                    time.sleep(2)
                    if domtolya == 1:
                        console.print(f"Толя дает MicroPhone")
                    time.sleep(2)
                    console.print('Толя: Звони.')
                    time.sleep(2)
                    console.print(f"Звонок на +7 800-62...")
                    time.sleep(2)
                    console.print(f"Sunne CL: Здравствуйте, ваш вопрос?")
                    time.sleep(2)
                    console.print(f"Вы: У МЕНЯ ЕСТЬ ВАША БАЗА ДАННЫХ ПЛАТИТЕ МНЕ 3000 ОЧКОВ И МЫ ОТСТАНЕМ. ЭСЛИ НЕ ОПЛАТИТЕ МЫ СОЛЬЕМ ДАННЫЕ В СЕТЬ ВМЕСТЕ С ДАННЫМИ КАРТ И ПАСПОРТОВ")
                    time.sleep(1.7)
                    console.print(
                        f"Sunne CL: Может быть бесплатно договоримся? Мы в суд на вас подадим!")
                    time.sleep(2)
                    console.print(
                        f"Вы: ПЛАТИ Я СКАЗАЛ ИНАЧЕ СУММА УВЕЛИЧИТСЯ ДО {3000 * 5 + 30} ОЧКОВ!")
                    time.sleep(2)
                    console.print(
                        f"Sunne CL: Ну пожалуйста...")
                    time.sleep(2)
                    console.print(
                        f"Вы: ПЛАТИ {3000 * 5 + 30} Я СКАЗАЛ ИНАЧЕ СУММА УВЕЛИЧИТСЯ ДО {3000 * 7 + 30} ОЧКОВ!")
                    time.sleep(2)
                    console.print(
                        f"Sunne CL: Оплатили. Отстаньте от нас.")
                    time.sleep(2)
                    console.print(
                        f"[white]+ 9030 очков[/]")
                    time.sleep(1.7)
                    console.print(
                        f"Вы: Спасибо. ПОКА.")
                    time.sleep(1.7)
                    ochko += 9030
                    save_game()
                    console.print(
                        f"Толя: Давай сольем пару данных в даркнет за 10 строк 1000 очков. И потом еще им позвоним с другого номера?")
                    time.sleep(2)
                    console.print(
                        f"Вы: Давай!")
                    time.sleep(2)
                    console.print(
                        f"Загрузка данных в даркнет...")
                    time.sleep(2)
                    console.print(
                        f"Толя: Звони им, я выставил")
                    time.sleep(2)
                    console.print(f"Sunne CL: Здравствуйте, ваш вопрос?")
                    time.sleep(2)
                    console.print(
                        f"Вы: ВАША БАЗА ДАННЫХ УЖЕ ПРОДАЕТСЯ ПЛАТИТЕ {3000 * 7 + 30}")
                    time.sleep(1.7)
                    console.print(
                        f"Sunne CL: Мы же уже оплатили 9030, еще?.")
                    time.sleep(2)
                    console.print(
                        f"Вы: ПЛАТИ {3000 * 7 + 30} Я СКАЗАЛ ИНАЧЕ СУММА УВЕЛИЧИТСЯ ДО {3000 * 10 + 60} ОЧКОВ!")
                    time.sleep(2)
                    console.print(
                        f"Sunne CL: Скинул. Удалите из даркнета пожалуйста... Мы очень ценим клиентов!")
                    time.sleep(2)
                    console.print(
                        f"[white]+ 21030 очков[/]")
                    time.sleep(1.7)
                    gamecorpscam = 1
                    ochko += 21030
                    save_game()
                time.sleep(2)
                console.print(
                        f"Толя: Какой же ты вырожденный скамер! Поздравляю! Следующий скам через год, живи у меня, я уезжаю в Финляндию по делам.")
                time.sleep(2)
                if domtolya == 1:
                    console.print(
                        f"Вы жили спокойно, хорошо. Никто вас не тревожил. Вы увидели в новостях что его задержали и он сел на 7 лет...")
                    if data_base == 1:
                        koncovka_data()
                    else:
                        koncovka_notdata()
                elif domtolya == 2 or domtolya == 3:
                    console.print(
                        f"Вы жили спокойно, хорошо. Через 2 дня к вам приехала полиция, вас задержали на 5 лет. Вы увидели в новостях что Толя уехал в Финляндию, на приезде его задержали и он сел на 7 лет.")
                    koncovka_police()

            zvv = False
        await asyncio.sleep(0.1)

if __name__ == '__main__':
    threading.Thread(target=asyncio.run, args=(main(),), daemon=True).start()
    threading.Thread(target=asyncio.run, args=(tolyapath2(),), daemon=True).start()
    time.sleep(1)
    print("Играй")
    time.sleep(1)
    while True:
        if koncovka_active == 1:
            koncovka_predatel("Толя")
            break
        elif koncovka_active == 2:
            koncovka_neutral()
            break
        elif koncovka_active == 3:
            koncovka_police()
            break
        elif koncovka_active == 4:
            koncovka_data()
            break
        elif koncovka_active == 5:
            koncovka_notdata()
            break

        if zvv:
            time.sleep(0.1)
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(nazvanie)
        if domtolya == 0:
            console.print("Ваш дом")
        else:
            console.print("Дом Толи")
        console.print(f"[green]Очки: {ochko} | День: {day} | Гвозди: {gvozd}[/]")
        console.print("[green]Активности:[/]")
        console.print("[green]Доступно:[/]")
        if pomit == 1:
            console.print("[green]1 - Помыть посуду (28 очко)[/]")
        else:
            console.print("[red]1 - Помыть посуду (28 очко)[/]")

        if pomitp == 1:
            console.print("[green]2 - Помыть полы (24 очко)[/]")
        else:
            console.print("[red]2 - Помыть полы (24 очко)[/]")

        if musor == 1:
            console.print("[green]3 - Вынести мусор (36 очко)[/]")
        else:
            console.print("[red]3 - Вынести мусор (36 очко)[/]")

        if dro == 1:
            console.print("[green]4 - Подрочить (24 очко)[/]")
        else:
            console.print("[red]4 - Подрочить (24 очко)[/]")

        if igr == 1:
            console.print("[green]5 - Поиграть (32 очко)[/]")
        else:
            console.print("[red]5 - Поиграть (32 очко)[/]")

        if rib == 1:
            console.print("[green]6 - Рыбалка (64 очко)[/]")
        else:
            console.print("[red]6 - Рыбалка (64 очко)[/]")

        if dss == 1 and (dayav == 1 or dayav2 == 1):
            console.print("[green]7 - Спать[/]")
        else:
            console.print("[red]7 - Спать[/]")

        if posilka == 2 or posilka == 3 or posilka == 4:
            console.print("[green]8 - Почта (забрать плакат)[/]")
        else:
            console.print("[red]8 - Почта (посылок нет)[/]")

        if posilka == 1 and gvozd >= 4:
            console.print("[green]9 - Вешать плакат[/]")
        elif posilka == 1 and gvozd < 4:
            console.print("[red]9 - Вешать плакат (нужно 4 гвоздя)[/]")
        elif posilka >= 2:
            console.print("[red]9 - Вешать плакат[/]")
        else:
            pass

        if mearephone == 1 and tolya_dialog == 0 and day >= 7:
            console.print("[green]0 - Позвонить Толе (MearePhone)[/]")
        elif mearephone == 1 and tolya_dialog == 1:
            console.print("[red]0 - Позвонить Толе (уже говорил)[/]")
        elif mearephone == 0 and path_police == 2:
            console.print("[red]0 - Позвонить Толе (нужен MearePhone)[/]")
            
        console.print("[green]Q - Магазин (гвозди, MearePhone)[/]")
            
        console.print("Выберите что вам сделать: ")
        ent = 0
        char = None
        
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char.isdigit():
                ent = int(char)
            elif char.lower() == 'q':
                ent = 11
        
        if ent == 0 and char != '0':
            time.sleep(0.05)
            continue
                        
        if int(ent) == 1:
            if pomit == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in track(range(100), description="Моем посуду...", style="green"):
                    time.sleep(0.1)
                ochko += 28
                pomit = 0
                cooldowns["pomit"] = time.time() + random.uniform(10.0, 50.0)
                save_game()
            else:
                console.print("[red]Данное действие недоступно. Иди жди![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 2:
            if pomitp == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in track(range(100), description="Моем полы...", style="green"):
                    time.sleep(0.35)
                ochko += 24
                pomitp = 0
                cooldowns["pomitp"] = time.time() + random.uniform(10.0, 100.0)
                save_game()
            else:
                console.print("[red]Данное действие недоступно. Иди жди![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 3:
            if musor == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in track(range(100), description="Выносим мусор...", style="green"):
                    time.sleep(0.65)
                ochko += 36
                musor = 0
                cooldowns["musor"] = time.time() + random.uniform(10.0, 200.0)
                save_game()
            else:
                console.print("[red]Данное действие недоступно. Иди жди![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 4:
            if dro == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in track(range(100), description="Дрочим...", style="green"):
                    time.sleep(0.12)
                ochko += 24
                dro = 0
                drc = 1
                cooldowns["dro"] = time.time() + random.uniform(20.0, 60.0)
                save_game()
            else:
                console.print("[red]Данное действие недоступно. Иди жди![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 5:
            if igr == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in track(range(100), description="Играем...", style="green"):
                    time.sleep(0.35)
                ochko += 32
                igr = 0
                cooldowns["igr"] = time.time() + random.uniform(100.0, 240.0)
                save_game()
            else:
                console.print("[red]Данное действие недоступно. Иди жди![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 6:
            if dss == 1 and rib == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print("[green]Рыбалка[/]")
                console.print("Нажми [green]Enter[/] когда удочка над зоной")
                console.print("[green]Зеленая[/] = 64 очка | [yellow]Желтая[/] = 32 очка")
                console.print()
                
                green_size = 2
                yellow_size = 2
                total_length = 20
                position = 0
                direction = 1
                attempts = 0
                max_attempts = 3
                
                while attempts < max_attempts:
                    line = [' '] * total_length
                    
                    green_start = (total_length - green_size) // 2
                    green_end = green_start + green_size
                    
                    yellow_start = green_start - yellow_size
                    yellow_end = green_end + yellow_size
                    
                    for i in range(total_length):
                        if green_start <= i < green_end:
                            line[i] = '[green]█[/]'
                        elif (yellow_start <= i < green_start) or (green_end <= i < yellow_end):
                            line[i] = '[yellow]█[/]'
                    
                    line[position] = '[white]|[/]'
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    console.print(f"Попытка: {attempts}/{max_attempts}")
                    console.print(''.join(line))
                    
                    if msvcrt.kbhit():
                        key = msvcrt.getwch()
                        if key == '\r':
                            attempts += 1
                            if green_start <= position < green_end:
                                ochko += 64
                                console.print("[green]Попал! +64 очка[/]")
                                time.sleep(0.5)
                            elif (yellow_start <= position < green_start) or (green_end <= position < yellow_end):
                                ochko += 32
                                console.print("[yellow]Попал! +32 очка[/]")
                                time.sleep(0.5)
                            else:
                                console.print("[red]Промах![/]")
                                time.sleep(0.5)
                    
                    position += direction
                    if position >= total_length - 1 or position <= 0:
                        direction *= -1
                    time.sleep(0.01)
                
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f"[green]Рыбалка окончена! Заработано очков: {ochko}[/]")
                rib = 0
                cooldowns["rib"] = time.time() + random.uniform(60.0, 200.0)
                save_game()
                time.sleep(2)
            else:
                console.print("[red]Данное действие недоступно![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 7:
            if (dayav == 1 or dayav2 == 1) and dss == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in track(range(100), description="Спим...", style="green"):
                    time.sleep(0.35)
                day += 1
                dayav = 0
                dayav2 = 0
                cooldowns["dayav"] = time.time() + random.uniform(10.0, 40.0)
                if tolea_sdan == 1:
                    paranoya_day += 1
                    if paranoya_day == 1 and paranoya_shown == 0:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(1.5)
                        console.print("")
                        console.print("[yellow]Вы проснулись...[/]")
                        time.sleep(2.5)
                        console.print("")
                        console.print("[yellow]Вы почувствовали ощущение, что абсолютно все теперь не как прежнему.[/]")
                        time.sleep(3)
                        console.print("[yellow]На вас наступило чувство тревоги.[/]")
                        time.sleep(3)
                        console.print("")
                        console.print("[white]Что-то изменилось. Воздух стал другим.[/]")
                        time.sleep(2.5)
                        console.print("[white]Стены комнаты кажутся чужими.[/]")
                        time.sleep(2.5)
                        console.print("[white]Вы не можете отделаться от мысли, что за вами наблюдают.[/]")
                        time.sleep(3)
                        console.print("")
                        console.print("[red]Тревога не отпускает.[/]")
                        time.sleep(3)
                        paranoya_shown = 1
                        save_game()
                        input("[white]Нажмите Enter чтобы продолжить...[/]")
                    elif paranoya_day >= 2:
                        koncovka_active = 1
                        save_game()
                        time.sleep(1)
                else:
                    save_game()
            else:
                console.print("[red]Данное действие недоступно. Иди жди![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 8:
            if posilka == 2 or posilka == 3 or posilka == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print("[white]Почта XurtIMail, отдел 839[/]")
                time.sleep(1.2)
                console.print("Вы подходите к стойке. За стойкой сидит мужик в грязной форме, курит прямо в помещении.")
                time.sleep(2.7)
                console.print("Толя: Чего надо?")
                time.sleep(2.2)
                console.print("Вы: Я за посылкой от Sunne CL. Плакат рекламный.")
                time.sleep(2.7)
                console.print("Толя: *лениво листает журнал* ФИО отправителя и получателя говори.")
                time.sleep(2.7)
                if posilka == 2:
                    console.print("Вы: Дмитрий Иванов.")
                elif posilka == 3:
                    console.print("Вы: Иван Борисов.")
                elif posilka == 4:
                    console.print("Вы: Алекс Джинг.")
                time.sleep(2.7)
                console.print("Толя: *долго ищет на полке, роняет коробки, матерится*")
                time.sleep(2.0)
                console.print("Толя: Вот твой плакат. Только слушай сюда...")
                time.sleep(2.7)
                console.print("Толя: У меня тут база клиентов этой вашей Sunne CL. Там ФИО, адреса, телефоны. Могу слить тебе за 15 очков. Пригодится.")
                time.sleep(2.7)
                console.print("[green]Выбор: [/]")
                console.print("[green]1. Купить базу за 80 очков[/]")
                console.print("[red]2. Отказаться и забрать плакат[/]")
                otzz8 = Prompt.ask(
                    "ВЫБИРАЙ:", 
                    choices=["1", "2"], 
                    default="2"
                )
                if otzz8 == "1":
                    if ochko >= 80:
                        ochko -= 80
                        data_base = 1
                        console.print("Вы: Давай сюда.")
                        time.sleep(2.2)
                        console.print("Толя: *протягивает флешку* Только ты меня не видел. Если что - я в отпуске. Мой HP (секретный даркнет) номер - 7-2L-C1-1032")
                        time.sleep(2.7)
                        console.print("[yellow]Вы получили базу данных клиентов Sunne CL. Открыта новая механика.[/]")
                        save_game()
                    else:
                        console.print("Вы: У меня нет столько...")
                        time.sleep(2.2)
                        console.print("Толя: Тогда проваливай, бездельник.")
                        time.sleep(2.2)
                        koncovka_neutral()
                elif otzz8 == "2":
                    console.print("Вы: Не надо мне ничего, давай плакат.")
                    time.sleep(2.2)
                    console.print("Толя: Как хочешь. Распишись здесь.")
                    time.sleep(2.2)
                    koncovka_neutral()
                console.print("*Вы забираете плакат и уходите из почты*")
                posilka = 1
                save_game()
                time.sleep(2.5)
            else:
                console.print("[red]На ваше имя нет посылок![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 9:
            if posilka == 1:
                if gvozd >= 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    console.print("[green]Вешаем плакат[/]")
                    console.print("Нужно забить 4 гвоздя. Минимум 2 успешных удара.")
                    console.print("[green]Зеленая[/] = успех | [yellow]Желтая[/] = палец | Пустая = промах")
                    console.print("Нажми [green]Enter[/] когда молоток над гвоздем")
                    time.sleep(2)
                    
                    successes = 0
                    for nail in range(4):
                        gvozd -= 1
                        save_game()
                        position = 0
                        direction = 1
                        hit = False
                        
                        console.print(f"\n[yellow]Гвоздь {nail + 1}/4 | Осталось гвоздей: {gvozd}[/]")
                        time.sleep(1)
                        
                        while not hit:
                            line = [' '] * 20
                            green_start = 9
                            green_end = 11
                            yellow_start = 7
                            yellow_end = 13
                            
                            for i in range(20):
                                if green_start <= i < green_end:
                                    line[i] = '[green]█[/]'
                                elif (yellow_start <= i < green_start) or (green_end <= i < yellow_end):
                                    line[i] = '[yellow]█[/]'
                            
                            line[position] = '[white]|[/]'
                            
                            os.system('cls' if os.name == 'nt' else 'clear')
                            console.print("[green]Вешаем плакат[/]")
                            console.print(f"Гвоздь {nail + 1}/4 | Успехов: {successes} | Гвоздей: {gvozd}")
                            console.print(''.join(line))
                            
                            if msvcrt.kbhit():
                                key = msvcrt.getwch()
                                if key == '\r':
                                    hit = True
                                    if green_start <= position < green_end:
                                        successes += 1
                                        console.print("[green]Попал в гвоздь![/]")
                                        time.sleep(0.5)
                                    elif (yellow_start <= position < green_start) or (green_end <= position < yellow_end):
                                        console.print("[red]Попал по пальцу![/]")
                                        time.sleep(0.5)
                                    else:
                                        console.print("[red]Промах![/]")
                                        time.sleep(0.5)
                            
                            position += direction
                            if position >= 19 or position <= 0:
                                direction *= -1
                            time.sleep(0.015)
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    console.print(f"[white]Результат:[/]")
                    console.print(f"Успешных ударов: {successes}/4")
                    
                    if successes >= 2:
                        console.print("[green]Плакат успешно повешен![/]")
                        plakat()
                        posilka = 5
                    else:
                        console.print("[red]Не удалось повесить плакат. Нужно минимум 2 успеха.[/]")
                    
                    save_game()
                    time.sleep(3)
                else:
                    console.print("[red]Недостаточно гвоздей! Нужно 4 гвоздя.[/]")
                    time.sleep(2)
            else:
                console.print("[red]Данное действие недоступно![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 0:
            if mearephone == 1 and tolya_dialog == 0 and day >= 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f"[white]День {day}. Ночь. Вы достаёте MearePhone...[/]")
                time.sleep(2.5)
                console.print("[yellow]Набираете HP номер: 7-2L-C1-1032[/]")
                time.sleep(3)
                console.print("[yellow]Гудки...[/]")
                time.sleep(2)
                console.print("[yellow]Гудки...[/]")
                time.sleep(2.5)
                console.print("Толя: Кто это? Откуда у тебя мой HP номер?")
                time.sleep(2.5)
                console.print("Вы: Здоров, Толя. Я тот самый, с почты. Помнишь плакат от Sunne CL?")
                time.sleep(2.5)
                console.print("Толя: А, помню. Чего надо?")
                time.sleep(2.5)
                console.print("Вы: Тут полиция приходила. Искали тебя. Говорили что ты хакер.")
                time.sleep(2.5)
                console.print("Толя: *молчание* ...И что ты им сказал?")
                time.sleep(3)
                console.print("[green]Выбор: [/]")
                console.print("[green]1. Сказать что сдал его полиции[/]")
                console.print("[green]2. Сказать что не сдал, хочу работать вместе[/]")
                console.print("[red]3. Сказать что не сдал, но хочу просто забыть[/]")
                otzz_tolya = Prompt.ask(
                    "ВЫБИРАЙ:", 
                    choices=["1", "2", "3"], 
                    default="2"
                )
                if otzz_tolya == "1":
                    time.sleep(2.5)
                    console.print("Вы: Я сдал тебя. Извини, но я не хочу проблем с законом.")
                    time.sleep(2.5)
                    console.print("Толя: *тяжёлый вздох* Понятно. ТЕБЕ ПИЗДА ЗАВТРА НОЧЬЮ.")
                    time.sleep(2.5)
                    console.print("Вы: Пока.")
                    time.sleep(2.5)
                    console.print("*Связь оборвалась*")
                    time.sleep(2)
                    path_tolya = 1
                    tolya_dialog = 1
                    tolea_sdan = 1
                    save_game()
                elif otzz_tolya == "2":
                    time.sleep(2.5)
                    console.print("Вы: Не сдал. И не собираюсь. Я хочу работать с тобой.")
                    time.sleep(2.5)
                    console.print("Толя: *удивлённо* Серьёзно? А зачем тебе это?")
                    time.sleep(2.5)
                    if data_base == 1:
                        console.print("Вы: У меня есть база клиентов Sunne CL. ФИО, адреса, телефоны. Можно сделать что-то интересное.")
                        time.sleep(2.5)
                        console.print("Толя: *заинтересованно* Хмм... База говоришь? Я же тебе её продавал! Это может быть полезно в связке.")
                        time.sleep(2.5)
                    elif data_base == 0:
                        console.print("Вы: У меня есть идея, будем скамерами??")
                        time.sleep(2.5)
                        console.print("Толя: *заинтересованно* Хмм... Скам? Это может быть сильно в связке.")
                        time.sleep(2.5)
                    console.print("Толя: Слушай, давай встретимся завтра. Расскажу что у меня есть на уме. У меня тут пара схем намечается.")
                    time.sleep(2.5)
                    console.print("Вы: Договорились. Где и когда?")
                    time.sleep(2.5)
                    console.print("Толя: Скину координаты через HP. Будь на связи.")
                    time.sleep(2.5)
                    console.print("*Связь оборвалась*")
                    time.sleep(2)
                    console.print("[green]Вы почувствовали что это начало чего-то большого.[/]")
                    time.sleep(3)
                    path_tolya = 2
                    tolya_dialog = 1
                    daytolya = day
                    save_game()
                elif otzz_tolya == "3":
                    time.sleep(2.5)
                    console.print("Вы: Не сдал. Но я хочу просто забыть обо всём этом. Не влезать.")
                    time.sleep(2.5)
                    console.print("Толя: Понял. Осторожность не помешает.")
                    time.sleep(2.5)
                    console.print("Толя: Спасибо что не сдал. Если что - ты уже не знаешь как меня найти.")
                    time.sleep(2.5)
                    console.print("Вы: Ага")
                    time.sleep(2.5)
                    console.print("*Связь оборвалась*")
                    time.sleep(2)
                    path_tolya = 3
                    tolya_dialog = 1
                    koncovka_neutral()
                    save_game()
            else:
                console.print("[red]У вас нет MearePhone или вы уже говорили с Толей![/]")
                time.sleep(2)
            in_action = False
        elif int(ent) == 11:
            os.system('cls' if os.name == 'nt' else 'clear')
            console.print("[white]МАГАЗИН[/]")
            time.sleep(1.5)
            console.print("")
            console.print(f"[green]Ваши очки: {ochko}[/]")
            console.print("")
            console.print("[green]Товары:[/]")
            console.print("[green]1 - Гвоздь (40 очков)[/]")
            if mearephone == 0 and police == 1:
                console.print("[green]2 - MearePhone (200 очков) - телефон для даркнета[/]")
            else:
                console.print("[red]2 - MearePhone[/]")
            if dike >= 1:
                if ochko >= 3000:
                    console.print("[green]3 -  (3000 очков) - Juing Orus 3000[/]")
                else:
                    console.print("[red]3 -  (3000 очков) - Juing Orus 3000 (нет очков)[/]")
            else:
                console.print("[red]3 -  (3000 очков) - Juing Orus 3000[/]")
            console.print("[red]4 - Выйти из магазина[/]")
            console.print("")
            otzz_mag = Prompt.ask(
                "Выбор:", 
                choices=["1", "2", "3", "4"], 
                default="3"
            )
            if otzz_mag == "1":
                if ochko >= 40:
                    ochko -= 40
                    gvozd += 1
                    save_game()
                    console.print(f"[green]Куплен 1 гвоздь! Осталось гвоздей: {gvozd}[/]")
                else:
                    console.print("[red]Недостаточно очков![/]")
                time.sleep(2)
            elif otzz_mag == "2":
                if mearephone == 1:
                    console.print("[yellow]У вас уже есть MearePhone![/]")
                    time.sleep(2)
                elif police == 0:
                    console.print("[red]Недоступно[/]")
                    time.sleep(2)
                else:
                    if ochko >= 200:
                        ochko -= 200
                        mearephone = 1
                        save_game()
                        console.print("[green]Вы купили MearePhone![/]")
                        time.sleep(1.5)
                        console.print("[yellow]Это специальный телефон для связи через даркнет.[/]")
                        time.sleep(2)
                        console.print("[yellow]С его помощью можно звонить по HP номерам.[/]")
                        time.sleep(2.5)
                        console.print("[yellow]Теперь у вас есть доступ к теневой сети.[/]")
                        time.sleep(3)
                    else:
                        console.print(f"[red]Недостаточно очков! Нужно 200, у вас {ochko}[/]")
                        time.sleep(2)
            elif otzz_mag == "3":
                if juing == 1:
                    console.print("[yellow]У вас уже есть Juing Orus 3000![/]")
                    time.sleep(2)
                elif dike >= 1:
                    console.print("[red]Недоступно[/]")
                    time.sleep(2)
                else:
                    if ochko >= 3000:
                        ochko -= 3000
                        juing = 1
                        save_game()
                        console.print("[green]Вы купили Juing Orus 3000![/]")
                        console.print("[yellow]Теперь у вас есть очень крутой унитаз.[/]")
                        time.sleep(3)
                    else:
                        console.print(f"[red]Недостаточно очков! Нужно 3000, у вас {ochko}[/]")
                        time.sleep(2)
            elif otzz_mag == "4":
                console.print("[white]Вы вышли из магазина.[/]")
                time.sleep(1)
            in_action = False
        elif int(ent) == 10:
            if ochko >= 40:
                ochko -= 40
                gvozd += 1
                save_game()
                console.print("[green]Куплен 1 гвоздь за 40 очков[/]")
            else:
                console.print("[red]Недостаточно очков для покупки гвоздя![/]")
            time.sleep(1)
            in_action = False
        else:
            console.print("[red]Неправильное написал[/]")
            time.sleep(0.1)
            in_action = False