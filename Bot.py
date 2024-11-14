import telebot

bot = telebot.TeleBot('')
TOKEN = 'ТОКЕН ИЗ BOTFATHER'

user_ids = set()

@bot.message_handler(commands=['start'])
def main(message):
     user_ids.add(message.from_user.id)
     bot.send_message(message.chat.id, f'<b>Привет</b> {message.from_user.first_name}, это бот для ...😎😎😎', parse_mode='html')

@bot.message_handler(commands=['wtf'])
def catalog(message):
    ctg1 = open('Путь к картинке для отправки', 'rb')
    bot.send_photo(message.chat.id, ctg1)
    bot.send_message(message.chat.id, f'<b>текст</b>', parse_mode='html')

@bot.message_handler(commands=['smth'])
def main2(message):
     print (f'{message.from_user.first_name} получил текст')
     bot.send_message(message.chat.id, "текст")
     #bot.send_message(message.chat.id, 'можно встроить ссылку для отправки ее по комманде')
@bot.message_handler(commands=["onas"])
def onas1(message):
    print (f'{message.from_user.first_name} нажал onas')
    bot.send_message(message.chat.id, 'текст')

def send_broadcast(message):
    for user_id in user_ids:
        try:
            bot.send_message(user_id, message)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")

@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    msg = message.text.split(' ', 1)
    if len(msg) < 2:
        bot.reply_to(message, "Укажите сообщение для рассылки.👌🏿")
        return

    # рассылка
    send_broadcast(msg[1])
    bot.reply_to(message, "👌🏿отослал👌🏿")

@bot.message_handler()
def info(message):
    if message.text.lower() == "команда":
        print (f'{message.from_user.first_name} команду Ввели')
        bot.send_message(message.chat.id, 'текст')
    elif message.text.lower() == 'комманда2':
        print (f'{message.from_user.first_name} комманда2 ввели ввели')
        bot.send_message(message.chat.id, 'текст')
    elif message.text.lower() == 'комманда3':
        print (f'{message.from_user.first_name} комманда3 Ввели')
        bot.send_message(message.chat.id, 'текст')
    elif message.text.lower() == "комманда4":
        print (f"{message.from_user.first_name} Ввели комманда4")
        file = open('Путь к .mp3 файлу (ОТПРАВЛЯЕТ ГОЛОСОВОЕ)', 'rb')
        bot.send_voice(message.chat.id, file)
    else:
        file = open('Путь до файла картинки при вводе неверной комманды', 'rb')
        bot.send_photo(message.chat.id, file)
        print (f'{message.from_user.first_name} ввел некорректную команду😎')
        bot.send_message(message.chat.id, f'ой, похоже {message.from_user.first_name} ввел неверную комманду😂')

# Не закрывает😎
bot.polling(none_stop=True)
