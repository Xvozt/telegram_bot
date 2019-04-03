import telebot
import config

proxy = config.proxy
bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def repeat_messages(message):
    bot.send_message(message.chat_id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=2, timeout=60)
