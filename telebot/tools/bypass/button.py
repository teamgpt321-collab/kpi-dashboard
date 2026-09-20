from telebot.tools.bypass.handler import start_bypass


async def bypass_button(update, context):

    await start_bypass(
        update,
        context
    )
