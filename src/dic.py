list_option = {
    "Bot": {
        "New": {"Whatsapp": [100, 1000], "Telegram": [100, 500], "Discord": [500, 1500]},
        "Upgrade": {"Whatsapp": [100, 300], "Telegram": [100, 250], "Discord": [200, 750]},
        "Maintenance": {"Whatsapp": [50, 250], "Telegram": [50, 150], "Discord": [100, 450]},
    },
    "WebPage": {
        "New Page": [90, 120],
        "Upgrade Page": [50, 80],
        "Maintenance Page": [50, 70]
    }
}

#list Bot formatting

first_bot_formatted_option = list_option["Bot"]["New"].items()
second_bot_formatted_option = list_option["Bot"]["Upgrade"].items()
third_bot_formatted_option = list_option["Bot"]["Maintenance"].items()

#list WebPage formatting

third_formatted_option = list_option["WebPage"].items()