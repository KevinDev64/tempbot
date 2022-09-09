#!/bin/python3

# Telegram Bot for Server's temperature control

import os
import telebot

print("Bot starting...")

# Token for Bot

bot = telebot.TeleBot('5793419077:AAFtVnhUv2sXR1qTbPAp0Nq69CYaAtvs0DE')
    
def get_temp():
    temp_file = open("/sys/devices/virtual/thermal/thermal_zone0/temp", 'r')
    
    temp_raw = int(temp_file.readline())
    temp = temp_raw // 100
    temp = temp / 10
    
    temp_file.close()
    
    return temp

@bot.message_handler(commands=["start", "help"])

def start(m, res=False):
    bot.send_message(m.chat.id, "Привет! Я буду уведомлять тебя каждые 30 минут о моей температуре!\nТакже ты модешь узнать её сам команда:\n/temp или /t\n\nЕсть команды выключения и перезагрузки:\n/shutdown и /reboot")  
    
@bot.message_handler(commands=["temp", "t", "temperature"])

def show_temp(m, res=False):
    bot.send_message(m.chat.id, "Температура CPU - " + str(get_temp()) + " С°")
    

@bot.message_handler(commands=["shutdown"])

def shutdown(m, res=False):
    bot.send_message(m.chat.id, "Экстренное выключение...")
    print("shutdown")
    
@bot.message_handler(commands=["reboot"])

def reboot(m, res=False):
    print("Rebooting...")
    
bot.polling(none_stop=True, interval=0)  