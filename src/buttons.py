from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#first_options_buttons

def greetButtons():
    button1 = InlineKeyboardButton(text="Budget", callback_data="Budget")
    button2 = InlineKeyboardButton(text="Portfolio", callback_data="Portfolio")
    keyboardInline = InlineKeyboardMarkup().add(button1, button2)
    return keyboardInline


#new_options_buttons
def buttons():
    button1 = InlineKeyboardButton(text="AppBot", callback_data="Bot")
    button2 = InlineKeyboardButton(text="WebPage", callback_data="WebPage")
    keyboardInline = InlineKeyboardMarkup().add(button1, button2)
    return keyboardInline


#budget_options_buttons
def buttons_options():
    button1 = InlineKeyboardButton(text="New", callback_data="New")
    button2 = InlineKeyboardButton(text="Upgrade", callback_data="Upgrade")
    button3 = InlineKeyboardButton(text="Maintenance", callback_data="Maintenance")
    keyboardInline = InlineKeyboardMarkup().add(button1, button2, button3)
    return keyboardInline


#portfolio_options_button

def portfolio_buttons():
    button1 = InlineKeyboardButton(text="Yes", callback_data="Yes")
    button2 = InlineKeyboardButton(text="Maybe later", callback_data="Maybe later")
    keyboardInline = InlineKeyboardMarkup().add(button1, button2)
    return keyboardInline

