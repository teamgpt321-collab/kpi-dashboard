import json
from pathlib import Path
from datetime import datetime


FILE = Path("telebot/users.json")


def load_users():

    if not FILE.exists():
        return []

    return json.loads(
        FILE.read_text(
            encoding="utf-8"
        )
    )



def save_user(user):

    users = load_users()


    for u in users:
        if u["id"] == user["id"]:
            return


    users.append(user)


    FILE.write_text(
        json.dumps(
            users,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )



def count_users():

    return len(
        load_users()
    )
