from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query


# Главная клавиатура (Выбор платформы)
platforms = InlineKeyboardMarkup()
pc = InlineKeyboardButton("PC", callback_data="in_platform_pc")
phone = InlineKeyboardButton("Phone", callback_data="in_platform_phone")

platforms.add(pc, phone)


# PC
platform_pc = InlineKeyboardMarkup()
btn_mod_ES = InlineKeyboardButton("Mod for endless summer 🧚‍", callback_data="game_modES") # ИГРА
btn_calculator = InlineKeyboardButton("Calculator", callback_data="game_calculator") # ИГРА
btn_back_pc = InlineKeyboardButton("back", callback_data="btn_back_pc")

platform_pc.add(btn_mod_ES, btn_calculator)
platform_pc.add(btn_back_pc)


# PHONE
platform_phone = InlineKeyboardMarkup()
android = InlineKeyboardButton("Android", callback_data="in_android")
ios = InlineKeyboardButton("IOS", callback_data="in_ios")
btn_back_phone = InlineKeyboardButton("back", callback_data="btn_back_phone")

platform_phone.add(android, ios)
platform_phone.add(btn_back_phone)


# Android
android = InlineKeyboardMarkup()
btn_mosaic = InlineKeyboardButton("Mosaic 🧠", callback_data="game_mosaic") # ИГРА
btn_cars = InlineKeyboardButton("Cars 🚗", callback_data="game_cars") # ИГРА
btn_back_android = InlineKeyboardButton("back", callback_data="btn_back_android")

android.add(btn_mosaic, btn_cars)
android.add(btn_back_android)


# IOS
ios = InlineKeyboardMarkup()
btn_back_ios = InlineKeyboardButton("back", callback_data="btn_back_ios")

ios.add(btn_back_ios)