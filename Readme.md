## Bot assistent built with Python!

<div>
  <ul>
    <a href="#user_machine">
      <li>How to use in your machine</li>
    </a>
    <a href="#configuration_bot">
      <li>How to configure the bot</li>
    </a>
    <a href="#explaning">
      <li>Explanation</li>
    </a>
  </ul>
</div>

* How to **find** the Bot assistent on Telegram

***link*** http://t.me/angelollima_bot or ***direct search on Telegram***

<img id="img" src="images/angelollima_bot.png" title="Bot assistant" alt="A picture of the bot" width="500px" height="160px">

<p id="user_machine"></p>

#

* ***How to use in your machine***

First thing to do is go to the terminal of your machine or your editor and **install** the package

`pip install PyTelegramBotAPI`

#

<p id="configuration_bot"></p>

* ***How to configure the bot for your use***

Before explaining how to configure the bot, you must have your own bot created!\

You will need your bot token

Create a new folder in your directory and create two files **apikey.txt** and **email.txt** (or whatever name you want to put)

* In the *apikey.txt* file, put your bot's token. In the *email.txt* file, put your preferred email!

#

<p id="explaning"></p>

#

* ***Explanation***

`bot = telebot.TeleBot(api)` The bot variable is receiving the bot token.

`bot.edit_message_text(call.message.chat.id, call.message.id)` For the text to be edited on top of each other, so to speak. Remembering that the function must have the parameter **call** to work.

`bot.send_message(call.message.chat.id)` To send a message normally.
