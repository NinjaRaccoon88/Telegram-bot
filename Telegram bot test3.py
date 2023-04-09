import telebot
import requests
import json
from bs4 import BeautifulSoup
import random

bot = telebot.TeleBot("6238930344:AAEgXRfad1ZCpG3SFVIB9Xe3f_9DUwL7oBg")

# Команда старта бота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привіт! Я бот для вивчення англійської мови. Введіть '/word', щоб отримати нове слово англійською мовою та його переклад українською. Введіть '/daily', щоб отримати щоденне завдання для вивчення англійської мови.")

# Команда для випадкового слова та його перекладу
@bot.message_handler(commands=['word'])
def send_word(message):
    url = "https://www.vocabulary.com/dictionary/randomword"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    word = soup.find("h1", class_="dynamictext").text.strip().lower()
    definition = soup.find("p", class_="short").text.strip()
    translation = soup.find("div", class_="definition").find("a").text.strip()
    bot.reply_to(message, f"{word.capitalize()} - {translation.capitalize()}: {definition}")

# Команда для щоденного завдання
@bot.message_handler(commands=['daily'])
def send_daily_task(message):
    # Вибрати випадкове завдання
    tasks = [
        "Напишіть опис свого дня англійською мовою.",
        "Вивчіть 5 нових слів та їх переклад на українську мову.",
        "Перегляньте відео або послухайте подкаст на англійській мові.",
        "Знайдіть новину або статтю на англійській мові та перекладіть її на українську мову.",
        "Знайдіть пісню на англійській мові, вивчіть тексти та спробуйте співати.",
        "Вивчіть нову граматичну конструкцію та спробуйте її застосувати у розмові або письмі.",
        "Подивіться фільм або серіал на англійській мові та спробуйте описати його зміст англійською мовою.",
    ]
task = random.choice(tasks)
bot.reply_to(message, f"Щоденне завдання: {task}")