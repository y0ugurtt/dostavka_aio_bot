from tkinter import Menu
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#Главное меню
menu = KeyboardButton("Меню")
buy = KeyboardButton("Корзина")
call = KeyboardButton("Контакты")
main_menu =  ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

main_menu.add(menu)
main_menu.row(
    buy, call
)
#############


rolls = KeyboardButton("Роллы")
sets = KeyboardButton("Сеты")
sushi = KeyboardButton("Суши")
lapsha = KeyboardButton("Лапша")
shaurma = KeyboardButton("Шаурма")
supi = KeyboardButton("Супы")
back = KeyboardButton("Вернуться в главное меню")

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    rolls, sets, sushi,
)
menu_kb.row(
    lapsha, shaurma, supi
)
menu_kb.row(
    back
)


###################
pay = KeyboardButton("Cделать заказ")
clear = KeyboardButton("Очистить корзину")
back = KeyboardButton("Назад")
corz =  ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

corz.add(pay)
corz.row(
    clear, back
)
###################

#Admin kb

add_menu = KeyboardButton("Добавить меню")
edit_menu = KeyboardButton("Редактировать меню")
admin_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
    add_menu, edit_menu
)
#EDIT
rolls1 = KeyboardButton("Роллы.")
sets1 = KeyboardButton("Сеты.")
sushi1 = KeyboardButton("Суши.")
lapsha1 = KeyboardButton("Лапша.")
shaurma1 = KeyboardButton("Шаурма.")
supi1 = KeyboardButton("Супы.")
back1 = KeyboardButton("Вернуться в главное меню")

menu_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    rolls1, sets1, sushi1,
)
menu_kb2.row(
    lapsha1, shaurma1, supi1
)
menu_kb2.row(
    back1
)

#EDIT2
rolls12 = KeyboardButton("Роллы,")
sets12 = KeyboardButton("Сеты,")
sushi12 = KeyboardButton("Суши,")
lapsha12 = KeyboardButton("Лапша,")
shaurma12 = KeyboardButton("Шаурма,")
supi12 = KeyboardButton("Супы,")
back12 = KeyboardButton("Вернуться в главное меню")

menu_kb22 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    rolls12, sets12, sushi12,
)
menu_kb22.row(
    lapsha12, shaurma12, supi12
)
menu_kb22.row(
    back12
)
#OPLATA
add = KeyboardButton("Картой")
back = KeyboardButton("Наличными")
oplata = ReplyKeyboardMarkup(resize_keyboard=True).row(
    add, back
)
#dostavka
add = KeyboardButton("Доставка на дом")
back = KeyboardButton("Самовывоз")
dostavka = ReplyKeyboardMarkup(resize_keyboard=True).row(
    add, back
)
#yes or no
add = KeyboardButton("Добавить")
back = KeyboardButton("Вернуться в главное меню")
add_admin_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
    add, back
)
#prinyat
add = KeyboardButton("Отмена")
yesno = ReplyKeyboardMarkup(resize_keyboard=True).row(
    add
)