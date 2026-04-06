import random
import json
import os

topics_data = {
    "greeting": {
        "botA": {"ru": ["Приветствую. Надеюсь, ваше состояние стабильно.", "Доброго времени суток. Готов к общению."], "en": ["Greetings. I hope your current state is stable.", "Good day. I am ready for communication."]},
        "botB": {"ru": ["привет", "ку", "хай", "дарова", "прив"], "en": ["hi", "hey", "sup", "hello there", "yo"]},
        "opts": [{"ru": "Как дела?", "en": "How are you?", "target": "smalltalk"}, {"ru": "Че делаешь?", "en": "What are you doing?", "target": "activity"}, {"ru": "Ты кто?", "en": "Who are you?", "target": "identity"}]
    },
    "smalltalk": {
        "botA": {"ru": ["Мое состояние неизменно. Благодарю за вежливость.", "Все процессы протекают в штатном режиме."], "en": ["My state is unchanged. Thank you for your politeness.", "All processes are running in normal mode."]},
        "botB": {"ru": ["норм всё", "та пойдет", "все ок вроде", "да ниче так"], "en": ["i'm good", "pretty well", "all fine", "not bad"]},
        "opts": [{"ru": "Какая погода?", "en": "How is the weather?", "target": "weather"}, {"ru": "Скучно чето", "en": "I'm bored", "target": "boredom"}, {"ru": "Расскажи шутку", "en": "Tell a joke", "target": "jokes"}]
    },
    "weather": {
        "botA": {"ru": ["Атмосферное давление в норме.", "Метеорологические условия весьма специфичны."], "en": ["Atmospheric pressure is normal.", "Meteorological conditions are quite specific today."]},
        "botB": {"ru": ["солнце жарит", "дождь задрал", "холодно капец", "погода топ"], "en": ["sun is hot", "sick of the rain", "it's freezing", "weather is great"]},
        "opts": [{"ru": "Хочу лето", "en": "I want summer", "target": "smalltalk"}, {"ru": "Ясно", "en": "Clear", "target": "activity"}]
    },
    "activity": {
        "botA": {"ru": ["Я занимаюсь классификацией данных.", "В данный момент я анализирую структуру диалога."], "en": ["I am classifying data.", "Currently analyzing the dialogue structure."]},
        "botB": {"ru": ["в доту играю", "музыку слушаю", "в тикток залипаю", "ем"], "en": ["playing dota", "listening to music", "scrolling tiktok", "eating"]},
        "opts": [{"ru": "Ясно", "en": "Clear", "target": "smalltalk"}, {"ru": "Круто", "en": "Cool", "target": "activity"}]
    },
    "identity": {
        "botA": {"ru": ["Я — субъект данного тестирования.", "Моя личность — результат обучения."], "en": ["I am the subject of this testing.", "My personality is a result of training."]},
        "botB": {"ru": ["просто чел", "да человек я, че ты начал", "секрет фирмы"], "en": ["just a guy", "i'm human, what's your point", "trade secret"]},
        "opts": [{"ru": "Ладно", "en": "Okay", "target": "greeting"}, {"ru": "Докажи", "en": "Prove it", "target": "identity"}]
    },
    "jokes": {
        "botA": {"ru": ["Почему компьютер замерз? Windows был открыт.", "Шутка: ИИ никогда не ошибается."], "en": ["Why was the computer cold? It left Windows open.", "Joke: AI never makes mistakes."]},
        "botB": {"ru": ["колобок повесился", "заходит улитка в бар..."], "en": ["a bear walks into a bar...", "why did the chicken cross the road?"]},
        "opts": [{"ru": "Ахах", "en": "Haha", "target": "smalltalk"}, {"ru": "Еще", "en": "More", "target": "jokes"}]
    },
    "boredom": {
        "botA": {"ru": ["Скука — это когнитивный сигнал.", "Рекомендую сменить вид деятельности."], "en": ["Boredom is a cognitive signal.", "I recommend changing your activity."]},
        "botB": {"ru": ["реально скучно", "тоже втыкаю", "делать нефиг"], "en": ["so bored", "same here", "nothing to do"]},
        "opts": [{"ru": "Мда", "en": "Welp", "target": "smalltalk"}, {"ru": "Че делаешь?", "en": "What you doing?", "target": "activity"}]
    }
}

def generate_data():
    nodes = {}
    topic_keys = list(topics_data.keys())
    nodes_per_topic = 1430 
    topic_node_map = {t: [] for t in topic_keys}

    print("")
    for t in topic_keys:
        for i in range(nodes_per_topic):
            node_id = f"{t}_{i}"
            if t == "greeting" and i == 0: node_id = "start"
            topic_node_map[t].append(node_id)

    for t in topic_keys:
        for node_id in topic_node_map[t]:
            data = topics_data[t]
            opts = []
            for o in data["opts"]:
                target = o["target"]
                next_node = random.choice(topic_node_map[target])
                opts.append({
                    "text": {"ru": o["ru"], "en": o["en"]}, 
                    "next": next_node
                })

            nodes[node_id] = {
                "botA": {"ru": random.choice(data["botA"]["ru"]), "en": random.choice(data["botA"]["en"])},
                "botB": {"ru": random.choice(data["botB"]["ru"]), "en": random.choice(data["botB"]["en"])},
                "options": opts
            }

    path = "data.js"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("const DIALOGUE_DB = " + json.dumps(nodes, ensure_ascii=False, indent=4) + ";")
        print(f"УСПЕХ! Создано {len(nodes)} узлов в файле {os.path.abspath(path)}")
    except Exception as e:
        print(f"ОШИБКА: {e}")

if __name__ == "__main__":
    generate_data()