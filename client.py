from aiogram import types, Dispatcher

from aiogram.utils import executor

import logging
from aiogram import Bot, Dispatcher, types, executor

from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query

# Объекты для команд бота
from aiogram.types import BotCommand, BotCommandScopeChat

from aiogram.types import InputMediaPhoto

from aiogram.utils.markdown import link

from aiogram import types

from client import *


TOKEN = "your token"
logging.basicConfig(level=logging.INFO)


# прокси
proxy_url = "your proxy url"


bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)


# Функция (запуск бота)
async def on_startup(dp):
	await bot.send_message(your id, "Я запустился")

# Функция (выключение бота)
async def on_shutdown(dp):
	await bot.send_message(your id, "Я завершил работу")

# Токен оплаты
SBER_TOKEN = 'your sber token'


from keyboards import *


# Фотографии
menu = ("https://downloader.disk.yandex.ru/preview/711bb1adff875b15eb27bc2e953f8d0b36a69eecb3a2ca4648143ee0aa223585"
			"/63c1af3e/_6tncDV3aVZTsQg0TZbCornwjRjeQl6Sbl7ryrTKPw9pPdoQLXcQ1r0Yu5Untrt8SGGTmFGHYgs8E_rm6dSkYA%3D%3D?uid=0&"
			"filename=menu_one.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

platform = ("https://downloader.disk.yandex.ru/preview/e0779c47f7523699a0550b0e831705cc9cd499b05323a175930a608a4b059d3c"
				"/64431dd2/Vrk10M4lxUmYpAxy9taM378RG94hQbd9Gv2UXx_WTEckVyY85790xKgkDYejJE6kHQEOr2LtAwefMMR0vek7JQ%3D%3D?uid=0&"
				"filename=rus_platform.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

pc = ("https://downloader.disk.yandex.ru/preview/c2f1fbb4c7d3c2a355d7d61785ab22188ea5f22530e92a1f322a740a6501e478"
		"/63c1afe4/MNQlWgSL62OIKo3AGtl_v6X3ATg9TGRKmTLY0YJUpIQD6nmvIEl_RH7MzyL3Flp8Iowu8MDThx2y9aZ5ZE9loQ%3D%3D?uid=0&"
		"filename=pc.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")


# Функция для редактирования инлайн клавиатур
async def edit_message(call: types.CallbackQuery, photo,
                       kb: InlineKeyboardMarkup, caption: str):

	image = InputMediaPhoto(photo)
	await call.message.edit_media(media=image)

	await call.message.edit_caption(caption, parse_mode="HTML")
	await call.message.edit_reply_markup(reply_markup=kb)


# /start
@dp.message_handler(commands="start")
async def start(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=menu, caption=f"Здравствуйте, {message.from_user.full_name}!\n"
    															f"Вас приветствует New Vision Shop\n"
    															f"Для покупки игры выоберите нужную вам платформу ⬇",
    															reply_markup=platforms)


# Переходы
@dp.callback_query_handler(text_contains="in_")
async def in_(call: types.CallbackQuery):

	if call.data == "in_platform_pc":
		image = pc
		await edit_message(call, photo=image, caption="Выберите игру ⬇", kb=platform_pc)

	elif call.data == "in_platform_phone":
		image = platform
		await edit_message(call, photo=image, caption="Выберите платформу ⬇", kb=platform_phone)

	elif call.data == "in_android":
		image = menu
		await edit_message(call, photo=image, caption="Выберите игру ⬇", kb=android)

	elif call.data == "in_ios":
		image = menu
		await edit_message(call, photo=image, caption="Выберите игру ⬇", kb=ios)


# Переходы в игры
@dp.callback_query_handler(text_contains="game_")
async def games(call: types.CallbackQuery):

	await call.message.delete()

	if call.data == "game_mosaic":
		await call.answer()
		await bot.send_invoice(chat_id=call.from_user.id,
	                       title='Mosaic',
	                       description="""
    											Игра в жанре казуальные "Mosaic" для Android.
    											Разработчик: Komori.
    											Издатель: New Vision.
    											Жанр: Казуальные.
    											Платформа: Android.
    											Язык: Русский.
    											""",
	                       payload='mosaic',
	                       provider_token=SBER_TOKEN,
	                       currency='RUB',
	                       photo_url="https://downloader.disk.yandex.ru/preview/04c7efec54e436cec100c3a0c31855488f0c2089bb0499f322db1a494a4db9b7/6499f3de/XxOy4RGwmFLuyf83Ej6A5cGD5lx9DMHYfDyJ0VrtMkTouTdTjApFxDF2y-dgQyLozwrIIsA6h-u1WxikiysUgg%3D%3D?uid=0&filename=mosaic.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048",
    										 photo_size=800,
	                       prices=[
		                       types.LabeledPrice(label='Mosaic', amount=100_00)
	                       ])

	elif call.data == "game_cars":
		await call.answer()
		await bot.send_invoice(chat_id=call.from_user.id,
	                       title='Cars',
	                       description="""
    											Игра в жанре казуальные "Cars" для Android.
    											Разработчик: Komori.
    											Издатель: New Vision.
    											Жанр: Казуальные.
    											Платформа: Android.
    											Язык: Русский.
    											""",
	                       payload='cars',
	                       provider_token=SBER_TOKEN,
	                       currency='RUB',
	                       photo_url="https://downloader.disk.yandex.ru/preview/8c48370fab67cb42a9408b1d8f73425153f02a4a09e10bda2b7fa71f52f4472f/649afbac/aG7xacNyFljOd_1gt2TP_H0z5pF4H_j88sf3649jAzy1QEw3BBqVF6UGMyh16yATbbsYpFaS8BZHafF9l2Ay5w%3D%3D?uid=0&filename=cars.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048",
    										 photo_size=800,
	                       prices=[
		                       types.LabeledPrice(label='Cars', amount=100_00)
	                       ])

	elif call.data == "game_modES":
		await call.answer()
		await bot.send_invoice(chat_id=call.from_user.id,
	                       title='Mod ES',
	                       description="""
    											Мод в стиле забавные для игры Бесконенчое лето "The Adventures of Fedor" для ПК.
    											Разработчик: Komori, Basket.
    											Издатель: New Vision.
    											Жанр: Забавные.
    											Платформа: PC.
    											Язык: Русский.
    											""",
	                       payload='modES',
	                       provider_token=SBER_TOKEN,
	                       currency='RUB',
	                       photo_url="https://downloader.disk.yandex.ru/preview/ae23fdff727c37ec7be2fd23cccaee36784f41f9de9d63f84794a3231c6850bc/649afbc1/CBxM-YisCnJlR74orLAowZfnTKFlkYr3bagiK8noXhjh8-PAXSjcLunb1haH48f9Vrqty3rRuC62549cqEXqXw%3D%3D?uid=0&filename=Everlasting_Summer_NdNfec8MxX.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048",
    										 photo_size=800,
	                       prices=[
		                       types.LabeledPrice(label='MOD ES', amount=100_00)
	                       ])

	elif call.data == "game_calculator":
		await call.answer()
		await bot.send_invoice(chat_id=call.from_user.id,
	                       title='Calculator',
	                       description="""
    											Калькулятор.
    											Разработчик: Komori.
    											Издатель: New Vision.
    											Жанр: Казуальные.
    											Платформа: PC.
    											Язык: Русский.
    											""",
	                       payload='calculator',
	                       provider_token=SBER_TOKEN,
	                       currency='RUB',
	                       photo_url="https://downloader.disk.yandex.ru/preview/bc7b91f14cb257644552a27d148ab4eddfcdb05fb0d4f0426cf2ad999ee2ffbd/649b027f/gUXWHHf1FkV8tZdQtPhJDtkzrgba_bK3UCc1GE6l1pf97zS8wxGFG6e1d43g_ROGMjY--FYRdW0fMN9FgH5wfg%3D%3D?uid=0&filename=calculator.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048",
    										 photo_size=800,
	                       prices=[
		                       types.LabeledPrice(label='Calculator', amount=100_00)
	                       ])


# Кнопки назад
@dp.callback_query_handler(text_contains="btn_back_")
async def back(call: types.CallbackQuery):

	if call.data == "btn_back_pc":
		image = menu
		await edit_message(call, photo=image, caption="Здравствуйте, eщё раз!\n"
    															"Вас приветствует New Vision Shop\n"
    															"Для покупки игры выоберите нужную вам платформу ⬇",
    															kb=platforms)

	elif call.data == "btn_back_phone":
		image = menu
		await edit_message(call, photo=image, caption="Здравствуйте, ещё раз!\n"
    															"Вас приветствует New Vision Shop\n"
    															"Для покупки игры выоберите нужную вам платформу ⬇",
    															kb=platforms)

	elif call.data == "btn_back_android":
		image = platform
		await edit_message(call, photo=image, caption="Выберите платформу ⬇", kb=platform_phone)

	elif call.data == "btn_back_ios":
		image = platform
		await edit_message(call, photo=image, caption="Выберите платформу ⬇", kb=platform_phone)


@dp.pre_checkout_query_handler()
async def check(query: types.PreCheckoutQuery):
	await bot.answer_pre_checkout_query(query.id, ok=True)


# Покупка игры
@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def send_file(message: types.Message):

	if message.successful_payment.invoice_payload == 'mosaic':
		await message.reply_document(open('mosaic.apk', 'rb'))
		await message.answer('Вы купили игру Mosaic.')

	elif message.successful_payment.invoice_payload == 'cars':
		await message.reply_document(open('cars.apk', 'rb'))
		await message.answer('Вы купили игру Cars.')

	elif message.successful_payment.invoice_payload == 'modES':
		await message.reply_document(open('fedor_adventure_mod_bez_ozvuhki.7z', 'rb'))
		await message.answer('Вы купили мод на бесконечное лето.')

	elif message.successful_payment.invoice_payload == 'calculator':
		await message.reply_document(open('calculator.exe', 'rb'))
		await message.answer('Вы купили калькулятор.')


# Продвинутое эхо
@dp.message_handler(content_types=[
	types.ContentType.DOCUMENT, types.ContentType.PHOTO,
	types.ContentType.STICKER, types.ContentType.VIDEO,
	types.ContentType.TEXT,  types.ContentType.ANIMATION,
	types.ContentType.VOICE
])
async def download_doc(message: types.Message):

	if "document" in message:
		await message.answer_document(message.document.file_id)

	elif "photo" in message:
		await message.answer_photo(message.photo[-1].file_id)

	elif "sticker" in message:
		await message.answer_sticker(message.sticker.file_id)

	elif "video" in message:
		await message.answer_video(message.video.file_id)

	elif "text" in message:
	    await message.answer(message.text)

	# Голосовое сообщение
	elif "voice" in message:
	    await message.answer_voice(message.voice.file_id)


def register_handlers_client(dp : Dispatcher):
  dp.register_message_handler(command_start, commands=["start"])

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)