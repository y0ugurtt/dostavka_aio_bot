from ast import Store
from cgitb import text
from distutils.command import config
from hashlib import new
from pyexpat.errors import messages
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
import logging
import sqlite3
import function
import datetime
import keyboards as kb
from config import TOKEN
from config import YourPrivatKey
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random
from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMethods

QIWI_PRIV_KEY = YourPrivatKey
logging.basicConfig(level=logging.INFO)
p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)
storage = MemoryStorage()
class Form(StatesGroup):
    name = State() 
    sell = State() 
    opis = State() 
    photo = State() 
    delete = State()
    name1 = State()
    sell1 = State()
    opis1 = State() 
    photo1 = State()
    fio = State() 
    number = State() 
    dost = State()
    addres = State()
    comment = State()
    collvoPers = State()
    oplata = State()


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()

@dp.message_handler(commands=['admin'])
async def admin_menu(message: types.Message):
    await message.reply("Приветствую, владыка всея кухни!", reply_markup=kb.admin_kb)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    check_new_user = function.get_id(message.from_user.id)
    if check_new_user == None:
        await bot.send_message(message.from_user.id, "Привет! Выбери нужную кнопку:", reply_markup=kb.main_menu)
        function.db_table_val(user_id=message.from_user.id, username = message.from_user.first_name, pokypki=0, date=1, corz='Пусто', admin=0, dopstl=0, fio=0, number=0, dost=0, addres=0, comment=0, collvo=0, pay=0, )
        function.corzina(user_id=message.from_user.id, tovar=0, sum=0, id_tovar=0, name_tovar=0)
    else:
        await bot.send_message(message.from_user.id, "Привет! Выбери нужную кнопку:", reply_markup=kb.main_menu)

#BACK

@dp.message_handler(text="Вернуться в главное меню")
async def back_menu(message: types.Message):
    await message.reply("Привет! Выбери нужную кнопку:", reply_markup=kb.main_menu)

@dp.message_handler(text="Назад")
async def back_menu(message: types.Message):
    await message.reply("Привет! Выбери нужную кнопку:", reply_markup=kb.main_menu)

@dp.message_handler(text='Добавить меню')
async def corz(message: types.Message):
    await message.reply(f"Выберите раздел:", reply_markup=kb.menu_kb22)

#КОРЗИНА

@dp.message_handler(text='Корзина')
async def corz(message: types.Message):
    try:
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        request = f"""SELECT * FROM corzina WHERE user_id={message.from_user.id}"""
        cur.execute(request)
        records = cur.fetchall()
        l = []
        # C
        for row in records:
            l.append(f'{row[5]} : {row[3]} ₽')
        otvet1 = '\n'.join(map(str,l))
        asd = function.get_checkers_ids(message.from_user.id)
        # otvet2 = int('+'.join(map(str,l)))
        result = function.obshee_corz(message.from_user.id)[0]
        if result == None:
            await message.reply(f"Ваша корзина:\n➖➖➖➖➖➖➖\n<b>Пусто</b>\n➖➖➖➖➖➖➖\nОбщая сумма корзины: <code>0 ₽</code>", parse_mode='HTML', reply_markup=kb.corz)
        else:
            await message.reply(f"Ваша корзина:\n➖➖➖➖➖➖➖\n<b>{otvet1}</b>\n➖➖➖➖➖➖➖\nОбщая сумма корзины: <code>{result} ₽</code>", parse_mode='HTML', reply_markup=kb.corz)
        cursor.close()
    except TypeError:
        await message.reply(f"Ваша корзина:\n➖➖➖➖➖➖➖\n<b>Пусто</b>\n➖➖➖➖➖➖➖\nОбщая сумма корзины: <code>0 ₽</code>", parse_mode='HTML', reply_markup=kb.corz)
#MENU
@dp.message_handler(text="Меню")
async def menu(message: Message):
    await message.reply("Выбери категорию еды", reply_markup=kb.menu_kb)
#ADMIN MENU
@dp.message_handler(text="Редактировать меню")
async def menu(message: Message):
    await message.reply("Выбери категорию для редактирования", reply_markup=kb.menu_kb2)
#ТОВАР
@dp.callback_query_handler(lambda call: True)
async def process_callback_button1(call):
    if call.data == 'check':
        bills = function.get_bill_id(call.from_user.id)[0]
        bill_id = function.get_new_bill(call.from_user.id)[0]
        status = p2p.check(bill_id=new_bill.bill_id).status
        if status == 'PAID':
            await call.message.reply('Оплата прошла успешно!')
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            request = f"""SELECT * FROM corzina WHERE user_id={call.from_user.id}"""
            cur.execute(request)
            records = cur.fetchall()
            l = []
            # C
            for row in records:
                l.append(f'{row[5]} : {row[3]} ₽')
            otvet1 = '\n'.join(map(str,l))
            asd = function.get_checkers_ids(call.from_user.id)
            result = function.obshee_corz(call.from_user.id)[0]
            markupsub1 = types.InlineKeyboardMarkup(row_width=1)
            btn0 = types.InlineKeyboardButton(text='Принять', callback_data=f'yes_{call.from_user.id}')
            btn1 = types.InlineKeyboardButton(text='Отказать', callback_data=f'no_{call.from_user.id}')
            markupsub1.add(btn0, btn1)
            await bot.send_message(-1001832748921, f'''Заказ #1:
{otvet1}
Всего: {result} рублей

ФИО заказчика: {function.get_fio(call.from_user.id)[0]}
Номер телефона: {function.get_number(call.from_user.id)[0]}
Доставка или самовывоз: {function.get_dost(call.from_user.id)[0]}
Адрес доставки: {function.get_addres(call.from_user.id)[0]}
Комментарий к заказу: {function.get_comment(call.from_user.id)[0]}
Кол-во персон: {function.get_collvo(call.from_user.id)[0]}
Оплата: {function.get_pay(call.from_user.id)[0]}
Счёт оплачен!✅''', reply_markup=markupsub1)
        else:
            await call.message.reply("❌Счёт не оплачен!")
            # await bot.answer_callback_query(callback_query_id=cmd.id, text="Неверно, Верный ответ...", show_alert=True)

    if 'yes_' in call.data:
        id_tovar = call.data.replace('yes_', '')
        await bot.send_message(id_tovar, text = f'Ваш заказ принят, с Вами свяжется менеджер для уточнения заказа.', reply_markup=None)
        await bot.send_message(-1001832748921, text = f'Вы приняли заказ', reply_markup=None)
    if 'no_' in call.data:
        id_tovar = call.data.replace('no_', '')
        await bot.send_message(id_tovar, text = f'Ваш заказ отклонен. Проверьте правильность заполненных данных в заказе.', reply_markup=None)
        await bot.send_message(-1001832748921, text = f'Вы отклонили', reply_markup=None)
    if 'buysoft_' in call.data:
        id_tovar = call.data.replace('buysoft_', '')
        tovar_name = function.get_tovar_name(id_tovar)[0]
        tovar_price = function.get_sum_tovar(id_tovar)[0]
        # function.update_corzina_sum(tovar_price, call.from_user.id)
        # function.update_corzina_name(tovar_name, call.from_user.id)
        # function.update_corz(tovar_name, call.from_user.id)
        function.corzina(user_id=call.from_user.id, tovar=0, sum=tovar_price, id_tovar=id_tovar, name_tovar=tovar_name)
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, text = f'Товар добавлен в корзину!', parse_mode='html', reply_markup=None)
    if call.data == 'back':
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    if 'redact_name_' in call.data:
        id_tovar = call.data.replace('redact_name_', '')
        function.update_admin(id_tovar, call.from_user.id)
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await Form.name.set()
        await bot.send_message(call.message.chat.id, text = f'Введите новое название:', parse_mode='html', reply_markup=None)
    if 'redact_sell_' in call.data:
        id_tovar = call.data.replace('redact_sell_', '')
        function.update_admin(id_tovar, call.from_user.id)
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await Form.sell.set()
        await bot.send_message(call.message.chat.id, text = f'Введите новую цену:', parse_mode='html', reply_markup=None)
    if 'redact_opis_' in call.data:
        id_tovar = call.data.replace('redact_opis_', '')
        function.update_admin(id_tovar, call.from_user.id)
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await Form.opis.set()
        await bot.send_message(call.message.chat.id, text = f'Введите новое описание:', parse_mode='html', reply_markup=None)
    if 'redact_photo_' in call.data:
        id_tovar = call.data.replace('redact_photo_', '')
        function.update_admin(id_tovar, call.from_user.id)
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await Form.photo.set()
        await bot.send_message(call.message.chat.id, text = f'Пришлите новое фото:', parse_mode='html', reply_markup=None)
    if 'deleate_' in call.data:
        id_tovar = call.data.replace('deleate_', '')
        function.delete(id_tovar)
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = f"DELETE FROM tovar WHERE id={id_tovar}"
        cur.execute(request)
        conn.commit()
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await bot.send_message(call.message.chat.id, text = f'Товар удален!', parse_mode='html', reply_markup=None)
    if 'sort_' in call.data:
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar"""
        cur.execute(request)
        records = cur.fetchall()
        for row in records:
            if call.data == f'sort_{row[1]}':
                markupsub = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton(text='Редактировать название', callback_data=f'redact_name_{row[1]}')
                btn2 = types.InlineKeyboardButton(text='Редактировать цену', callback_data=f'redact_sell_{row[1]}')
                btn3 = types.InlineKeyboardButton(text='Редактировать описание', callback_data=f'redact_opis_{row[1]}')
                # btn4 = types.InlineKeyboardButton(text='Редактировать фото', callback_data=f'redact_photo_{row[1]}')
                btn5 = types.InlineKeyboardButton(text='Удалить', callback_data=f'deleate_{row[1]}')
                markupsub.add(btn1, btn2, btn3, btn5)
                await bot.send_message(call.message.chat.id, text = f'<b>Назваие товара:</b> {row[2]}\n\n<b>Цена:</b> <code>{row[3]} ₽</code>\n\n<b>Информация:</b>\n{row[5]}', parse_mode='html', reply_markup=markupsub)
    if 'soft_' in call.data:
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar"""
        cur.execute(request)
        records = cur.fetchall()
        for row in records:
            if call.data == f'soft_{row[1]}':
                markupsub = types.InlineKeyboardMarkup(row_width=1)
                btn0 = types.InlineKeyboardButton(text='Добавить в корзину', callback_data=f'buysoft_{row[1]}')
                btn1 = types.InlineKeyboardButton(text='Назад', callback_data='back')
                markupsub.add(btn0, btn1)
                photo = open(f'{row[4]}', 'rb')
                await bot.send_photo(call.message.chat.id, photo=photo, caption=f'<b>Назваие товара:</b> {row[2]}\n\n<b>Цена:</b> <code>{row[3]} ₽</code>\n\n<b>Информация:</b>\n{row[5]}', parse_mode='html', reply_markup=markupsub)

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        admin_id = function.get_admin(message.from_user.id)[0]
        function.update_name_tovar(data['name'], admin_id)
        await state.finish()
        await message.reply("Успешно!", reply_markup=None)
@dp.message_handler(state=Form.sell)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sell'] = message.text
        admin_id = function.get_admin(message.from_user.id)[0]
        function.update_sell_tovar(data['sell'], admin_id)
        await state.finish()
        await message.reply("Успешно!", reply_markup=None)
@dp.message_handler(state=Form.opis)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['opis'] = message.text
        admin_id = function.get_admin(message.from_user.id)[0]
        function.update_opis_tovar(data['opis'], admin_id)
        await state.finish()
        await message.reply("Успешно!", reply_markup=None)
@dp.message_handler(state=Form.photo)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.text
        await state.finish()
        await message.reply("Успешно!", reply_markup=None)

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    checkchisl = random.randint(1000, 50000)
    await message.photo[-1].download(f'img/{message.from_user.id}{checkchisl}.jpg')
    Patch = function.get_add(message.from_user.id)[0]
    function.product(id=f'{message.from_user.id}{checkchisl}', name=0, price=0, pokypki=f'img/{message.from_user.id}{checkchisl}.jpg', info=0, Path=Patch)
    function.update_date_admin(f'{message.from_user.id}{checkchisl}', message.from_user.id)
    # function.update_link_admin(f'img/{message.from_user.id}{checkchisl}.jpg', f'{message.from_user.id}{checkchisl}')
    await message.reply("Успешно!\nТеперь дайте название товару:", reply_markup=None)
    await Form.name1.set()


@dp.message_handler(state=Form.name1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name1'] = message.text
        get_id_tovar = function.get_admin_pokypki(message.from_user.id)[0]
        function.updater_name(data['name1'], get_id_tovar)
        await message.reply("Введите цену:", reply_markup=None)
        print(data['name1'])
        await state.finish()
        await Form.sell1.set()
@dp.message_handler(state=Form.sell1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sell1'] = message.text
        get_id_tovar = function.get_admin_pokypki(message.from_user.id)[0]
        function.updater_sell(data['sell1'], get_id_tovar)
        await message.reply("Введите описание:", reply_markup=None)
        print(data['sell1'])
        await state.finish()
        await Form.opis1.set()
@dp.message_handler(state=Form.opis1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['opis1'] = message.text
        get_id_tovar = function.get_admin_pokypki(message.from_user.id)[0]
        function.update_opis_tovar_adm(data['opis1'], get_id_tovar)
        await state.finish()
        await message.reply("Готово!", reply_markup=None)




@dp.message_handler(state=Form.fio)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fio'] = message.text
        if data['fio'] == 'Отмена':
            await state.finish()
            await message.reply("Отменено!", reply_markup=kb.main_menu)
        else:
            function.fio(message.text, message.from_user.id)
            await state.finish()
            await message.reply("Укажите Ваш номер телефона:", reply_markup=kb.yesno)
            await Form.number.set()
@dp.message_handler(state=Form.number)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        if data['number'] == 'Отмена':
            await state.finish()
            await message.reply("Отменено!", reply_markup=kb.main_menu)
        else:
            function.number(message.text, message.from_user.id)
            await state.finish()
            await message.reply("Доставка на дом, или самовывоз из ресторана?", reply_markup=kb.dostavka)
            await Form.dost.set()
@dp.message_handler(state=Form.dost)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dost'] = message.text
        if data['dost'] == 'Доставка на дом':
            function.dost(message.text, message.from_user.id)
            await state.finish()
            await message.reply("Введите свой адрес", reply_markup=None)
            await Form.addres.set()
            print(message.text)
        elif data['dost'] == 'Самовывоз':
            function.dost(message.text, message.from_user.id)
            await state.finish()
            await Form.comment.set()
            await message.reply("Укажите комментарий:", reply_markup=None)
@dp.message_handler(state=Form.addres)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['addres'] = message.text
        function.addres(message.text, message.from_user.id)
        await state.finish()
        await message.reply("Укажите комментарий:", reply_markup=None)
        await Form.comment.set()
@dp.message_handler(state=Form.comment)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comment'] = message.text
        await state.finish()
        function.comment(message.text, message.from_user.id)
        await message.reply("Укажите количество персон:", reply_markup=None)
        await Form.collvoPers.set()
@dp.message_handler(state=Form.collvoPers)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collvoPers'] = message.text
        function.collvo(message.text, message.from_user.id)
        await state.finish()
        await message.reply("Оплата", reply_markup=kb.oplata)
        await Form.oplata.set()
@dp.message_handler(state=Form.oplata)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['oplata'] = message.text
        if message.text == 'Картой':
            function.pay(message.text, message.from_user.id)
            await state.finish()
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            request = f"""SELECT * FROM corzina WHERE user_id={message.from_user.id}"""
            cur.execute(request)
            records = cur.fetchall()
            l = []
            # C
            for row in records:
                l.append(f'{row[5]} : {row[3]} ₽')
            otvet1 = '\n'.join(map(str,l))
            asd = function.get_checkers_ids(message.from_user.id)
            result = function.obshee_corz(message.from_user.id)[0]



            bildid = random.randint(11111111,9999999999)
            global new_bill
            global bill_id 
            new_bill = p2p.bill(bill_id=bildid, amount=result, lifetime=25)
            print(new_bill)


            function.update_bill_id(bildid, message.from_user.id)
            function.update_new_bill_id(new_bill, message.from_user.id)
            

            markupsub = types.InlineKeyboardMarkup(row_width=1)
            btn0 = types.InlineKeyboardButton(text='Оплатить', url=f'{new_bill.pay_url}')
            btn1 = types.InlineKeyboardButton(text='Проверить', callback_data='check')
            markupsub.add(btn0, btn1)

            await bot.send_message(message.from_user.id, f'''Ваш Заказ:
{otvet1}
Всего: {result} рублей

ФИО заказчика: {function.get_fio(message.from_user.id)[0]}
Номер телефона: {function.get_number(message.from_user.id)[0]}
Доставка или самовывоз: {function.get_dost(message.from_user.id)[0]}
Адрес доставки: {function.get_addres(message.from_user.id)[0]}
Комментарий к заказу: {function.get_comment(message.from_user.id)[0]}
Кол-во персон: {function.get_collvo(message.from_user.id)[0]}
Оплата: {function.get_pay(message.from_user.id)[0]}
''', reply_markup=markupsub)
            await bot.send_message(message.from_user.id, f'Наши контакты:\nАдрес: Оренбургская обл., г. Орск, ул. Краснознамённая, д. 70.\nТелефон: +7 (922) 534-09-09', reply_markup=None)
            await bot.send_message(message.from_user.id, f'Заказ ждёт оплаты!', reply_markup=kb.main_menu)
            cursor.close()
            await state.finish()
            # while True:
            #     if p2p.check(bill_id=new_bill.bill_id).status == 'PAID':
            #         break
            #     else:
            #         print(p2p.check(bill_id=new_bill.bill_id).status)
        if message.text == 'Наличными':
            function.pay(message.text, message.from_user.id)
            await state.finish()
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            request = f"""SELECT * FROM corzina WHERE user_id={message.from_user.id}"""
            cur.execute(request)
            records = cur.fetchall()
            l = []
            # C
            for row in records:
                l.append(f'{row[5]} : {row[3]} ₽')
            otvet1 = '\n'.join(map(str,l))
            asd = function.get_checkers_ids(message.from_user.id)
            result = function.obshee_corz(message.from_user.id)[0]
            await bot.send_message(message.from_user.id, f'''Ваш Заказ:
{otvet1}
Всего: {result} рублей

ФИО заказчика: {function.get_fio(message.from_user.id)[0]}
Номер телефона: {function.get_number(message.from_user.id)[0]}
Доставка или самовывоз: {function.get_dost(message.from_user.id)[0]}
Адрес доставки: {function.get_addres(message.from_user.id)[0]}
Комментарий к заказу: {function.get_comment(message.from_user.id)[0]}
Кол-во персон: {function.get_collvo(message.from_user.id)[0]}
Оплата: {function.get_pay(message.from_user.id)[0]}
''', reply_markup=kb.main_menu)
            cursor.close()
            await bot.send_message(message.from_user.id, f'Наши контакты:\nАдрес: Оренбургская обл., г. Орск, ул. Краснознамённая, д. 70.\nТелефон: +7 (922) 534-09-09', reply_markup=None)
            markupsub1 = types.InlineKeyboardMarkup(row_width=1)
            btn0 = types.InlineKeyboardButton(text='Принять', callback_data=f'yes_{message.from_user.id}')
            btn1 = types.InlineKeyboardButton(text='Отказать', callback_data=f'no_{message.from_user.id}')
            markupsub1.add(btn0, btn1)
            result = function.obshee_corz(message.from_user.id)[0]
            await bot.send_message(-1001832748921, f'''Заказ #1:
{otvet1}
Всего: {result} рублей

ФИО заказчика: {function.get_fio(message.from_user.id)[0]}
Номер телефона: {function.get_number(message.from_user.id)[0]}
Доставка или самовывоз: {function.get_dost(message.from_user.id)[0]}
Адрес доставки: {function.get_addres(message.from_user.id)[0]}
Комментарий к заказу: {function.get_comment(message.from_user.id)[0]}
Кол-во персон: {function.get_collvo(message.from_user.id)[0]}
Оплата: {function.get_pay(message.from_user.id)[0]}
''', reply_markup=markupsub1)
            await state.finish()


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('ОК')
@dp.message_handler(content_types=['text'])
async def text_message(message: types.Message):
    if message.text == 'Контакты':
        await message.reply(f"Адрес: Оренбургская обл., г. Орск, ул. Краснознамённая, д. 70.\nТел: <code>+7 (922) 534-09-09</code>",parse_mode='HTML', reply_markup=None)
# ФИО
# НОМЕР
# ДОСТАВКА/САМОВЫВОЗ
# АДРЕС
# КОММЕНТ
# КОЛЛ-ВО ПЕРСОН
# ОПЛАТА
    if message.text == 'Cделать заказ':
        result = function.obshee_corz(message.from_user.id)[0]
        if result == None:
            await message.reply(f"Ваша корзина пуста", parse_mode='HTML', reply_markup=kb.corz)
        else:
            await message.reply(f"Введите ФИО",parse_mode='HTML', reply_markup=kb.yesno)
            await Form.fio.set()
    if message.text == 'Очистить корзину':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = f"DELETE FROM corzina WHERE user_id={message.from_user.id}"
        cur.execute(request)
        conn.commit()
        # function.corzina(user_id=message.from_user.id, tovar=0, )
        await message.reply(f"Корзина очищена!",parse_mode='HTML', reply_markup=None)
    if message.text == 'Добавить':
        await message.reply(f"Пришлите фото товара",parse_mode='HTML', reply_markup=None)
        # await Form.name1.set()
    if message.text == 'Роллы,':
        name_tovar = 'roll'
        function.update_dopls(name_tovar, message.from_user.id)
        await message.reply(f"Выберите действие в разделе: <b>{message.text}</b>:",parse_mode='HTML', reply_markup=kb.add_admin_kb)
    if message.text == 'Сеты,':
        name_tovar = 'set'
        function.update_dopls(name_tovar, message.from_user.id)
        await message.reply(f"Выберите действие в разделе: <b>{message.text}</b>:",parse_mode='HTML', reply_markup=kb.add_admin_kb)
    if message.text == 'Суши,':
        name_tovar = 'suh'
        function.update_dopls(name_tovar, message.from_user.id)
        await message.reply(f"Выберите действие в разделе: <b>{message.text}</b>:",parse_mode='HTML', reply_markup=kb.add_admin_kb)
    if message.text == 'Лапша,':
        name_tovar = 'lap'
        function.update_dopls(name_tovar, message.from_user.id)
        await message.reply(f"Выберите действие в разделе: <b>{message.text}</b>:",parse_mode='HTML', reply_markup=kb.add_admin_kb)
    if message.text == 'Шаурма,':
        name_tovar = 'shaur'
        function.update_dopls(name_tovar, message.from_user.id)
        await message.reply(f"Выберите действие в разделе: <b>{message.text}</b>:",parse_mode='HTML', reply_markup=kb.add_admin_kb)
    if message.text == 'Супы,':
        name_tovar = 'soup'
        function.update_dopls(name_tovar, message.from_user.id)
        await message.reply(f"Выберите действие в разделе: <b>{message.text}</b>:",parse_mode='HTML', reply_markup=kb.add_admin_kb)


    if message.text == 'Роллы':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='roll'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'soft_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Сеты':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='set'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'soft_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Суши':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='suh'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'soft_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Лапша':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='lap'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'soft_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Шаурма':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='shaur'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'soft_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Супы':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='soup'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'soft_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)



    if message.text == 'Роллы.':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='roll'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'sort_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        # await bot.send_message(message.from_user.id, "Софт:", reply_markup=markupsub)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Сеты.':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='set'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'sort_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Суши.':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='suh'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'sort_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Лапша.':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='lap'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'sort_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Шаурма.':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='shaur'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'sort_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
    if message.text == 'Супы.':
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        request = """SELECT * from tovar WHERE Path='soup'"""
        cur.execute(request)
        records = cur.fetchall()
        markupsub = types.InlineKeyboardMarkup(row_width=1)
        button_list = [types.InlineKeyboardButton(text=row[2], callback_data=f'sort_{row[1]}') for row in records]   
        markupsub.add(*button_list)
        await message.reply(f"Ассортимент в категории <b>{message.text}</b>:",parse_mode='HTML', reply_markup=markupsub)
async def on_startup(_):
    print('Бот Вышел в Онлайн')
if __name__ == '__main__':
    executor.start_polling(dp)