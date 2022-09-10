#!/bin/python3

# Telegram Bot for Server's temperature control

import os
import telebot
import datetime

print("Bot starting...")

time = datetime.datetime.today()

months = {"1": "Января",
          "2": "Декабря",
          "3": "Марта",
          "4": "Апреля",
          "5": "Мая",
          "6": "Июня",
          "7": "Июля",
          "9": "Августа",
          "9": "Сентября",
          "10": "Октября",
          "11": "Ноября",
          "12": "Декабря"
          }

# Token for Bot

bot = telebot.TeleBot('5793419077:AAFtVnhUv2sXR1qTbPAp0Nq69CYaAtvs0DE')
    
def get_temp():
    temp_file = open("/sys/devices/virtual/thermal/thermal_zone0/temp", 'r')
    
    temp_raw = int(temp_file.readline())
    temp = temp_raw // 1000
    # temp = temp / 10
    
    temp_file.close()
    
    return temp


@bot.message_handler(commands=["start", "help"])

def start(m, res=False):
    bot.send_message(m.chat.id, "*Привет\!* Вот мои команды:\n*/off \| /shutdown* \- *_Выключает сервер_*\n*/reboot \| /restart* \- *_Перезагружает сервер_*\n*/t \| /temp \| /temperature* \- *_отображает температуру процессора сервера_*", parse_mode="MarkdownV2")  
    
@bot.message_handler(commands=["temp", "t", "temperature"])

def show_temp(m, res=False):
    # Get date info 
    year = time.year
    month_raw = str(time.month)
    day = time.day
    hour = time.hour
    minutes = time.minute
    seconds = time.second
    
    bot.send_message(m.chat.id, "Сегодня \- *_" + str(day) + " " + months[month_raw] + " " + str(year) + " года_*", parse_mode="MarkdownV2")
    bot.send_message(m.chat.id, "Время \- *_" + str(hour) + "\:" + str(minutes) + "\:" + str(seconds) + "_*", parse_mode="MarkdownV2")
    bot.send_message(m.chat.id, "Температура *CPU* \- *" + str(get_temp()) + " С°*", parse_mode="MarkdownV2")
    

@bot.message_handler(commands=["shutdown", "off"])

def shutdown(m, res=False):
    bot.send_message(m.chat.id, "*Экстренное выключение \.\.\.*", parse_mode="MarkdownV2")
    os.system("shutdown now")

    
@bot.message_handler(commands=["reboot", "restart"])

def reboot(m, res=False):
    bot.send_message(m.chat.id, "*Перезагрузка сервера \.\.\.*", parse_mode="MarkdownV2")
    bot.send_message(m.chat.id, "*Внимание\! Для последующего управления потребуется\n_РУЧНОЙ ВХОД В СИСТЕМУ С ПАНЕЛИ УПРАВЛЕНИЯ\!\!\!_*", parse_mode="MarkdownV2")
    os.system("reboot")
    
bot.polling(none_stop=True, interval=0)  