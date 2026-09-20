import asyncio


from telegram import (
    Update,
    ReplyKeyboardMarkup
)


from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)


from telebot.config import TOKEN


from telebot.tools.osp.handler import (
    start_osp,
    receive_osp_input
)


from telebot.tools.bypass.handler import (
    start_bypass,
    receive_bypass
)

from telebot.tools.reset_mac.handler import (
    start_reset_mac,
    receive_reset_mac_input
)


from telebot.sessions.state import get_state


from telebot.tools.osp.osp_queue import (
    osp_worker
)



MENU = [
    [
        "🛠 Set OSP"
    ],
    [
        "🔧 Bypass",
        "🔄 Reset MAC"
    ]
]



async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = ReplyKeyboardMarkup(
        MENU,
        resize_keyboard=True
    )


    await update.message.reply_text(
        "🤖 KPI Tool Bot\n\n"
        "Chọn chức năng:",
        reply_markup=keyboard
    )



async def menu_handler(
    update,
    context
):

    text = update.message.text


    if text == "🛠 Set OSP":

        await start_osp(
            update,
            context
        )


    elif text == "🔧 Bypass":

        await start_bypass(
            update,
            context
        )


    elif text == "🔄 Reset Mac":

        await start_reset_mac(
            update,
            context
        )



async def receive_text(
    update,
    context
):

    state = get_state(
        update.message.from_user.id
    )


    if not state:
        return


    action = state.get(
        "action"
    )


    if action == "set_osp":

        await receive_osp_input(
            update,
            context
        )


    elif action == "bypass":

        await receive_bypass(
            update,
            context
        )


    elif action == "reset_mac":

        await receive_reset_mac_input(
            update,
            context
        )



async def startup(
    app: Application
):

    asyncio.create_task(
        osp_worker()
    )


    print(
        "🛠 OSP Queue Worker started"
    )



app = Application.builder() \
    .token(TOKEN) \
    .post_init(startup) \
    .build()



app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


app.add_handler(
    CommandHandler(
        "bypass",
        start_bypass
    )
)



app.add_handler(
    MessageHandler(
        filters.Regex(
            "^(🛠 Set OSP|🔧 Bypass|🔄 Reset Mac)$"
        ),
        menu_handler
    )
)



app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        receive_text
    )
)



print(
    "Bot running..."
)


app.run_polling()
