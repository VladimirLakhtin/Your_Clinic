from aiogram.types import InputFile
from create_bot import bot
from text import texts
import keyboard


async def send_message_start(message):
    await bot.send_video(message.from_user.id, video=InputFile(path_or_bytesio="Video.mp4"), caption=f"<b>{texts['start']}</b> +7 (969) 000-40-40", reply_markup=keyboard.kb_mark_main, parse_mode='html')

async def send_message_price(message):
    await bot.send_message(message.from_user.id, texts["price"], reply_markup=keyboard.inl_kb_mark_site)

async def send_message_inst(message):
    await bot.send_message(message.from_user.id, texts["inst"], reply_markup=keyboard.inl_kb_mark_inst)

async def send_message_contacts(message):
    photo_file = InputFile(path_or_bytesio="locations.jpg")
    await bot.send_photo(message.from_user.id, photo=photo_file, caption=texts["contacts"], reply_markup=keyboard.inl_kb_mark_contacts)

async def send_message_queshions(message):
    await bot.send_message(message.from_user.id, texts["queshions"], reply_markup=keyboard.inl_kb_mark_queshions)

async def send_message_sign_up(message):
    await bot.send_message(message.from_user.id, texts["sign_up"], reply_markup=keyboard.inl_kb_mark_sign_up)

async def send_message_services(message):
    await bot.send_message(message.from_user.id, texts["services"], reply_markup=keyboard.inl_kb_mark_services)

async def edit_message_service_description(call):
    await bot.edit_message_text(
        text = texts[call.data],
        message_id = call.message.message_id,
        chat_id = call.message.chat.id, 
        reply_markup=keyboard.inl_kb_mark_service_description
    )

async def edit_message_all_services(call):
    await bot.edit_message_text(
        text = texts["services"],
        message_id = call.message.message_id,
        chat_id = call.message.chat.id, 
        reply_markup=keyboard.inl_kb_mark_services
    )

def register_handlers(dp):
    dp.register_message_handler(send_message_start, commands=["start"])
    dp.register_message_handler(send_message_price, lambda message: "прайс" in message.text.lower(), state=None)
    dp.register_message_handler(send_message_inst, lambda message: "instagram" in message.text.lower(), state=None)
    dp.register_message_handler(send_message_contacts, lambda message: "контакты" in message.text.lower(), state=None)
    dp.register_message_handler(send_message_queshions, lambda message: "вопрос" in message.text.lower(), state=None)
    dp.register_message_handler(send_message_sign_up, lambda message: "записаться" in message.text.lower(), state=None)
    dp.register_message_handler(send_message_services, lambda message: "услуги" in message.text.lower(), state=None)
    dp.register_callback_query_handler(edit_message_service_description, lambda callback: callback.data in ["ser_1", "ser_2", "ser_3"], state=None)
    dp.register_callback_query_handler(edit_message_all_services, lambda callback: callback.data == "back", state=None)
    dp.register_callback_query_handler(send_message_sign_up, lambda callback: callback.data == "sign_up", state=None)