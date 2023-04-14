import random
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

word_dict = {
    'history': 'історія',
    'science': 'наука',
    'technology': 'технологія',
    'religion': 'релігія',
    'politics': 'політика',
    'government': 'уряд',
    'law': 'право',
    'justice': 'правосуддя',
    'humanity': 'людство'
}

score = 0

def get_random_word():
    word = random.choice(list(word_dict.keys()))
    return word, word_dict[word]

def start(update, context):
    global score
    score = 0
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю! Це гра для вивчення англійських слів. Щоб почати, введіть команду /play")

def play(update, context):
    global score
    word, translation = get_random_word()
    context.user_data['answer'] = translation
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Як перекласти слово '{word}' на українську?")
    
def answer(update, context):
    global score
    user_answer = update.message.text.lower()
    correct_answer = context.user_data['answer'].lower()
    if user_answer == correct_answer:
        score += 1
        context.bot.send_message(chat_id=update.effective_chat.id, text="Правильно! 🎉")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Неправильно. Правильна відповідь: '{correct_answer}'")
    word, translation = get_random_word()
    context.user_data['answer'] = translation
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Як перекласти слово '{word}' на українську?")


def get_score(update, context):
    global score
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Ваш рахунок: {score}")


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Невідома команда. Спробуйте ще раз.")

def main():
    updater = Updater(token='5989079525:AAFBPeSxAUMcQaCPUAdmWp4jhGFwHPeGf0s', use_context=True)
    
    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler)

    
    play_handler = CommandHandler('play', play)
    updater.dispatcher.add_handler(play_handler)

    
    answer_handler = MessageHandler(filters.text & ~filters.command, answer)
    updater.dispatcher.add_handler(answer_handler)

    
    score_handler = CommandHandler('score', get_score)
    updater.dispatcher.add_handler(score_handler)

    
    unknown_handler = MessageHandler(filters.command, unknown)
    updater.dispatcher.add_handler(unknown_handler)

    
    updater.start_polling()

    
    updater.idle()

    if __name__ == '__main__':
        main()