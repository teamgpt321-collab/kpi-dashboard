import json
from pathlib import Path
from datetime import datetime


FILE = Path(
    "telebot/tools/bypass/history.json"
)


def load_history():

    if not FILE.exists():
        return []

    try:
        return json.loads(
            FILE.read_text(
                encoding="utf-8"
            )
        )

    except Exception:
        return []



def save_history(
    telegram_user,
    shd,
    result
):

    history = load_history()


    history.append(
        {
            "user": str(telegram_user),
            "shd": shd,
            "time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "result": result
        }
    )


    FILE.write_text(
        json.dumps(
            history,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )



def get_history():

    return load_history()

