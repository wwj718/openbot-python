import openbot

CLIENT_ACCESS_TOKEN = "openbot"
HOST = "http://127.0.0.1:8000"
def main():
    bot = openbot.OpenBot(HOST,CLIENT_ACCESS_TOKEN)

    # session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    query = "你叫什么"

    response = bot.chat(query)

    print(response)


if __name__ == '__main__':
    main()
