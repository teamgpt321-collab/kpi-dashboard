import asyncio
import os


from telebot.sessions.state import (
    set_state,
    get_state,
    clear_state
)


from telebot.user_registry import save_user


from telebot.tools.thong_tin_khach.thong_tin_khach import (
    run
)


from telebot.usage_log import save_usage




async def start_thong_tin_khach(
    update,
    context
):

    user_id = update.message.from_user.id


    set_state(
        user_id,
        {
            "action": "thong_tin_khach"
        }
    )


    await update.message.reply_text(
        "📋 Thông tin khách\n\n"
        "Nhập số hợp đồng SHĐ:"
    )






async def receive_thong_tin_khach_input(
    update,
    context
):

    user_id = update.message.from_user.id


    save_user(
        update.message.from_user
    )


    state = get_state(
        user_id
    )


    if not state:
        return



    if state.get("action") != "thong_tin_khach":
        return



    shd = update.message.text.strip()



    clear_state(
        user_id
    )



    await update.message.reply_text(
        f"🔎 Đang lấy thông tin SHĐ: {shd}"
    )



    try:


        image_path = await asyncio.to_thread(
            run,
            shd
        )


        save_usage(
            tool="thong_tin_khach",
            user=user_id,
            shd=shd,
            result="success"
        )


        await context.bot.send_photo(
            chat_id=user_id,
            photo=open(
                image_path,
                "rb"
            ),
            caption=f"📋 Thông tin khách\nSHĐ: {shd}"
        )



        if os.path.exists(image_path):

            os.remove(
                image_path
            )


            print(
                "Đã xóa ảnh:",
                image_path
            )



    except Exception as e:


        save_usage(
            tool="thong_tin_khach",
            user=user_id,
            shd=shd,
            result="failed"
        )


        await update.message.reply_text(
            f"❌ Lỗi lấy thông tin khách:\n{e}"
        )
