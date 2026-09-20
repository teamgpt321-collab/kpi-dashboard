from telebot.sessions.state import (
    set_state,
    get_state,
    clear_state
)

from telebot.tools.reset_mac.reset_mac import run

from telebot.user_registry import save_user

import asyncio



async def start_reset_mac(update, context):

    user_id = update.message.from_user.id


    set_state(
        user_id,
        {
            "action": "reset_mac"
        }
    )


    await update.message.reply_text(
        "🔄 Reset MAC\n\n"
        "Nhập số hợp đồng SHĐ:"
    )




async def receive_reset_mac_input(update, context):

    user_id = update.message.from_user.id


    save_user(
        update.message.from_user
    )


    state = get_state(
        user_id
    )


    if not state:
        return


    if state.get("action") != "reset_mac":
        return



    shd = update.message.text.strip()


    clear_state(
        user_id
    )


    await update.message.reply_text(
        f"🚀 Bắt đầu Reset MAC\n"
        f"SHĐ: {shd}"
    )


    try:


        result = await asyncio.to_thread(
            run,
            shd
        )


        await update.message.reply_text(
            result
        )


    except Exception as e:


        await update.message.reply_text(
            f"❌ Reset MAC lỗi:\n{e}"
        )
