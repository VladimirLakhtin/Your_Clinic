from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


btn_sign_up = KeyboardButton("Записаться")
btn_queshion = KeyboardButton("Задать вопрос")
btn_sales = KeyboardButton("Прайс с акциями -50%")
btn_inst = KeyboardButton("Наши работы в Instagram")
btn_contacts = KeyboardButton("Наши контакты")
kb_mark_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_mark_main.add(btn_sign_up).row(btn_queshion, btn_sales).add(btn_inst).add(btn_contacts)

btn_site_url = InlineKeyboardButton("Перейти на сайт", url="https://www.your-clinic.pro/")
inl_kb_mark_site = InlineKeyboardMarkup().add(btn_site_url)

btn_inst_url = InlineKeyboardButton("Перейти в Instagram", url="https://instagram.com/yourclinic.ru?igshid=YmMyMTA2M2Y=")
inl_kb_mark_inst = InlineKeyboardMarkup().add(btn_inst_url)

btn_contacts_inst = InlineKeyboardButton("Instagram", url="https://instagram.com/yourclinic.ru?igshid=YmMyMTA2M2Y=")
btn_contacts_site = InlineKeyboardButton("Сайт", url="https://www.your-clinic.pro/")
btn_contacts_wa = InlineKeyboardButton("Whats App", url="https://api.whatsapp.com/send/?phone=79690004040&text&type=phone_number&app_absent=0")
btn_contacts_tg = InlineKeyboardButton("Telegram", url="https://t.me/YourClinic_pro")
inl_kb_mark_contacts = InlineKeyboardMarkup().add(btn_contacts_inst).add(btn_contacts_wa).add(btn_contacts_tg).add(btn_contacts_site)

btn_tg = InlineKeyboardButton("Диалог Telegram", url="https://t.me/yourclinicpro")
btn_num = InlineKeyboardButton("Позвонить", url="https://clicks.su/gbNLJL")
inl_kb_mark_queshions = InlineKeyboardMarkup().add(btn_tg).add(btn_num)

btn_sign_up_num = InlineKeyboardButton("По телефону", url="https://clicks.su/gbNLJL")
btn_sign_up_tg = InlineKeyboardButton("Telegram", url="https://t.me/yourclinicpro")
btn_sign_up_site = InlineKeyboardButton("На сайте", url="https://www.your-clinic.pro/")
inl_kb_mark_sign_up = InlineKeyboardMarkup().add(btn_sign_up_num).add(btn_sign_up_tg).add(btn_sign_up_site)