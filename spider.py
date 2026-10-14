import random
import urllib.request
import urllib.parse
import json

TOKEN = "8656135022:AAH9F7k1vuqHdbSEIACPerznHRXCBfC9rNQ"
CHANNEL_ID = "@orakul_zvezd"

HOOKS_TEEN = [
    "Твой код судьбы скрывает цифру, которую знают только 3% людей. Проверь свою матрицу Пифагора прямо сейчас! https://t.me/pass_farm_game_bot/play",
    "Какая цифра отвечает за твою популярность и удачу в этом месяце? Рассчитай по дате рождения! https://t.me/pass_farm_game_bot/play",
    "Совпадение по дате рождения: узнай всю правду о человеке за 5 секунд. https://t.me/pass_farm_game_bot/play"
]

HOOKS_ADULT = [
    "Финансовый код по Пифагору: почему одни богатеют в 30, а другие теряют? Узнай свой код богатства. https://t.me/pass_farm_game_bot/play",
    "Скрытый потенциал твоей даты рождения: чего ты о себе не знал? Глубокий нумерологический разбор. https://t.me/pass_farm_game_bot/play",
    "Кризис или точка роста? Что ждет тебя в ближайшие 3 года по картам судьбы. https://t.me/pass_farm_game_bot/play"
]

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHANNEL_ID, "text": text}).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req) as response:
            print("Пост успешно отправлен в Telegram!")
    except Exception as e:
        print("Ошибка отправки:", e)

if __name__ == "__main__":
    category = random.choice([HOOKS_TEEN, HOOKS_ADULT])
    post_text = random.choice(category)
    print("Текст:", post_text)
    send_telegram(post_text)
