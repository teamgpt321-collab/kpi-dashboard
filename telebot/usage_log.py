import json
from pathlib import Path
from datetime import datetime

import requests



FILE = Path(
    "telebot/data/usage_history.json"
)



# API Vercel nhận log
API_URL = (
    "https://kpi-dashboard-woad.vercel.app/api/tool-usage/save"
)





def load_usage():

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







def save_usage(
    tool,
    user,
    shd,
    result
):

    now = datetime.now()


    time_text = now.strftime(
        "%Y-%m-%d %H:%M:%S"
    )



    data = {

        "tool": tool,

        "user": str(user),

        "shd": shd,

        "time": time_text,

        "result": result

    }



    # =========================
    # GỬI VỀ VERCEL API
    # =========================

    try:

        response = requests.post(
            API_URL,
            json=data,
            timeout=10
        )


        if response.status_code == 200:

            print(
                "Saved Vercel:",
                data
            )

        else:

            print(
                "Vercel save error:",
                response.status_code,
                response.text
            )


    except Exception as e:

        print(
            "Vercel connection error:",
            e
        )






    # =========================
    # BACKUP LOCAL JSON
    # =========================

    try:

        history = load_usage()


        history.append(
            data
        )


        FILE.write_text(
            json.dumps(
                history,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )


    except Exception as e:

        print(
            "Local log error:",
            e
        )
