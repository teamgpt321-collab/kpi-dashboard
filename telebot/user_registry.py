import json
from pathlib import Path


FILE = Path(
    "/home/tiendv1/kpi-dashboard/telebot/data/telegram_users.json"
)


def save_user(user):

    print(
        "SAVE_USER CALL:",
        user.id if user else None,
        user.username if user else None
    )


    if not user:
        return


    FILE.parent.mkdir(
        exist_ok=True
    )


    users = []


    if FILE.exists():

        try:

            content = FILE.read_text(
                encoding="utf-8"
            )

            if content.strip():
                users = json.loads(content)

        except Exception as e:

            print(
                "READ USER ERROR:",
                e
            )

            users = []



    user_id = str(user.id)


    found = False


    for item in users:

        if item.get("id") == user_id:

            item["username"] = user.username

            item["name"] = (
                f"{user.first_name or ''} "
                f"{user.last_name or ''}"
            ).strip()

            found = True
            break



    if not found:

        users.append(
            {
                "id": user_id,
                "username": user.username,
                "name": (
                    f"{user.first_name or ''} "
                    f"{user.last_name or ''}"
                ).strip()
            }
        )



    FILE.write_text(
        json.dumps(
            users,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    print(
        "SAVE_USER DONE:",
        user_id
    )
