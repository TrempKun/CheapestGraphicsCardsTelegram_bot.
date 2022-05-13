from email import message
import telebot
from parsing import get_prices


bot=telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def handle_message(message):
    message_split = message.text.split(" ")
    if message_split[0] == "@Card" and len(message_split) == 2:
        message_card_name = get_prices(message_split[1])
        bot.send_message(message.chat.id, message_card_name)
        
bot.infinity_polling()
