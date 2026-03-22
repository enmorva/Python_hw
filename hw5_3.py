import random
import json
import string

name = random.choice(["Саша", "Женя", "Алекс", "Слава", "Валя", "Миша"])
last_name = random.choice(["Грин", "Дюма", "Гюго", "Шевченко", "Живаго", "Седых"])
full_name = name + " " + last_name

age = random.randint(18, 80)

email_domains = ["mail.ru", "gmail.com", "yandex.ru", "bk.ru", "list.ru"]
email = full_name.lower().replace(" ", ".") + "@" + random.choice(email_domains)

password = ""
for i in range(12):
    password = password + random.choice(string.ascii_letters + string.digits + string.punctuation)

user_data = {
    "name": full_name,
    "age": age,
    "email": email,
    "password": password
}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f, ensure_ascii=False, indent=4)

with open("user.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(json.dumps(data, ensure_ascii=False, indent=4))
