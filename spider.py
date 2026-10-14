import random

HOOKS_TEEN = [
    "Твой код судьбы скрывает цифру, которую знают только 3% людей. Проверь свою матрицу Пифагора прямо сейчас! t.me/pass_farm_game_bot/play",
    "Какая цифра отвечает за твою популярность и удачу в этом месяце? Рассчитай по дате рождения! t.me/pass_farm_game_bot/play",
    "Совпадение по дате рождения: узнай всю правду о человеке за 5 секунд. t.me/pass_farm_game_bot/play"
]

HOOKS_ADULT = [
    "Финансовый код по Пифагору: почему одни богатеют в 30, а другие теряют? Узнай свой код богатства. t.me/pass_farm_game_bot/play",
    "Скрытый потенциал твоей даты рождения: чего ты о себе не знал? Глубокий нумерологический разбор. t.me/pass_farm_game_bot/play",
    "Кризис или точка роста? Что ждет тебя в ближайшие 3 года по картам судьбы. t.me/pass_farm_game_bot/play"
]

def generate_post():
    category = random.choice([HOOKS_TEEN, HOOKS_ADULT])
    return random.choice(category)

if __name__ == "__main__":
    print("Сгенерированный пост для публикации:\n", generate_post())
