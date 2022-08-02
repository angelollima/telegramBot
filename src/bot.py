import telebot
from buttons import *
from dic import *

# Open the bot token, email and set the bot with it.

with open('./config/apikey.txt', 'r') as data_api:
    api = data_api.readline()

with open('./config/email.txt', 'r') as data_email:
    email = data_email.readline()

bot = telebot.TeleBot(api)

ready_message = "Click on one of the options below:"


# budget selection.


def budget(call):
    text = """
Great decision!!

Tell me a little more about the project you have in mind.

{}
    """.format(ready_message)
    bot.edit_message_text(text, call.message.chat.id, call.message.id , reply_markup=buttons())


#All about the bot functions.


def iBot(call):
    text = """
We have come to an important point,
tell me which of the options below you want about the Bot!

{}
    """.format(ready_message)
    bot.edit_message_text(text, call.message.chat.id, call.message.id , reply_markup=buttons_options())


def newBot(call):
    text = """
Below is the price table, which
are usually used on a budget
for this kind of work (Bot) -> (New)!!

{}

If you want to close this project with me,
contact by email:
    """.format('\n'.join([f"{key} {' à '.join(map(lambda i: 'R$' + str(i), value))}"
    for key, value in first_bot_formatted_option]))

    bot.edit_message_text(text, call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, email)


def upgradeBot(call):
    text = """
Below is the price table, which
are usually used on a budget
for this kind of work (Bot) -> (Upgrade)!!

{}

If you want to close this project with me,
contact by email:
    """.format('\n'.join([f"{key} {' à '.join(map(lambda i: 'R$' + str(i), value))}"
    for key, value in second_bot_formatted_option]))

    bot.edit_message_text(text, call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, email)


def maintenanceBot(call):
    text = """
Below is the price table, which
are usually used on a budget
for this kind of work (Bot) -> (Maintenance)!!

{}

If you want to close this project with me,
contact by email:
    """.format('\n'.join([f"{key} {' à '.join(map(lambda i: 'R$' + str(i), value))}"
    for key, value in third_bot_formatted_option]))

    bot.edit_message_text(text, call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, email)


#All about the WebPage


def iWebPage(call):
    text = """
Below is the price table, which
are usually used on a budget
for this type of work (Web page) -> (New)!!

{}

If you want to close this project with me,
contact by email:
    """.format('\n'.join([f"{key} {' à '.join(map(lambda i: 'R$' + str(i), value))}"
    for key, value in third_formatted_option]))

    bot.edit_message_text(text, call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, email)


# portfolio function. It can also call the (budget function)


def portfolio(call):
    text = """
I'm glad you're interested in
meet my work!

This link has some of my projects done before!

If you are interested in making a quote with me, click on "Yes", otherwise, click on "Maybe later"

https://github.com/Angelollima
    """
    bot.edit_message_text(text, call.message.chat.id, call.message.id , reply_markup=portfolio_buttons())


#options portfolio (yes/no)


def yes(call):
    return budget(call)

def maybeLater(call):       # -> (No)
    text= """
No problems.
Thank you very much for contacting me and
I'm available if you want to talk again.

To chat with me again, a simple 'Hi' will be enough!
😉"""
    bot.edit_message_text(text, call.message.chat.id, call.message.id)


# setting the callback_query_handler of the buttons/functions.


@bot.callback_query_handler(func=lambda call: True)
def callbackHandlers(call):
    if call.data == "Budget":
        budget(call)
    elif call.data == "Bot":
        iBot(call)
    elif call.data == "New":
        newBot(call)
    elif call.data == "Upgrade":
        upgradeBot(call)
    elif call.data == "Maintenance":
        maintenanceBot(call)
    elif call.data == "WebPage":
        iWebPage(call)
    elif call.data == "Portfolio":
        portfolio(call)
    elif call.data == "Yes":
        yes(call)
    elif call.data == "Maybe later":
        maybeLater(call)


# bot startup


def verify(message):
    return True


@bot.message_handler(func=verify)
def greet(message):
    text = """
Hi {}! I'm Angelo Lima, freelance developer.

Choose one of the options below.
    """.format(message.from_user.first_name)
    bot.send_message(message.chat.id, text, reply_markup=greetButtons())

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
