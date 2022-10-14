import sqlite3

conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()

def corzina(user_id: int, tovar: int, sum: int, id_tovar: int, name_tovar: str,):
    cursor.execute('INSERT or IGNORE INTO corzina (user_id, tovar, sum, id_tovar, name_tovar) VALUES (?, ?, ?, ?, ?)', (user_id, tovar, sum, id_tovar, name_tovar))
    conn.commit()

def product(id: int, name: str, price: int, pokypki: str, info: str, Path: str,):
    cursor.execute('INSERT or IGNORE INTO tovar (id, name, price, pokypki, info, Path) VALUES (?, ?, ?, ?, ?, ?)', (id, name, price, pokypki, info, Path))
    conn.commit()

def db_table_val(user_id: int, username: str, pokypki: int, date: str, corz: str, admin: int, dopstl: str, fio: str, number: str, dost: str, addres: str, comment: str, collvo: str, pay: str, bill_id: int, new_bill_id: str,):
    cursor.execute('INSERT or IGNORE INTO users (user_id, username, pokypki, date, corz, admin, dopstl, fio, number, dost, addres, comment, collvo, pay, bill_id, new_bill_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, username, pokypki, date, corz, admin, dopstl, fio, number, dost, addres, comment, collvo, pay, bill_id, new_bill_id))
    conn.commit()
#ЗАКАЗ
def fio(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET fio='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def number(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET number='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def dost(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET dost='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def addres(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET addres='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def comment(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET comment='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def collvo(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET collvo='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def pay(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET pay='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def get_fio(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT fio FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()
def get_number(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT number FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()
def get_dost(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT dost FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()
def get_addres(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT addres FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()
def get_comment(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT comment FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()
def get_collvo(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT collvo FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()
def get_pay(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT pay FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

#КОРЗИНА
def obshee_corz(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT SUM(sum) FROM corzina WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()


def delete_corz(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"DELETE FROM corzina WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_checkers_ids(id):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute(
            f"SELECT sum FROM corzina WHERE user_id={id}")
        rows = cur.fetchall()
        l = []
        for row in rows:
            for x in row:
                l.append(x)
        return l


def get_corzina_all(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT name_tovar AND sum FROM corzina WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchall()

def get_corzina(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT name_tovar FROM corzina WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_sum_corzina(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT sum FROM corzina WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchall()


def get_new_bill(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT new_bill_id FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()
def update_new_bill_id(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET new_bill_id='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def update_bill_id(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET bill_id={balance} WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def get_bill_id(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT bill_id FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchall()


def update_corzina_name(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE corzina SET name_tovar=name_tovar + '{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_corzina_sum(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE corzina SET sum=sum + {balance} WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()


def get_sum_tovar(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT price FROM tovar WHERE id={id}"
    cur.execute(request)
    return cur.fetchone()
def get_date(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT date FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def delete(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"DELETE FROM tovar WHERE id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_admin(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT admin FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_tovar_name(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT name FROM tovar WHERE id={id}"
    cur.execute(request)
    return cur.fetchone()
def update_sell_admin(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET price={balance} WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_name_tovar_adm(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET name='{balance}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_sell_tovar_adm(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET price={balance} WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_opis_tovar_adm(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET info='{balance}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def updater_sell(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET price={balance} WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def updater_name(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET name='{balance}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()




def update_link_admin(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET pokypki={balance} WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def update_date_admin(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET pokypki={balance} WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def get_add(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT dopstl FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()
def get_admin_pokypki(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT pokypki FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def update_dopls(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET dopstl='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_name_new(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET name='{balance}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def update_add(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET dopstl='{balance}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def update_name_tovar(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET name='{balance}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def update_sell_tovar(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET price={balance} WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()
def update_opis_tovar(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET info='{balance}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_corz(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET corz='{balance}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_admin(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET admin={balance} WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def get_corz(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT corz FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_id(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT user_id FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_balance(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT balance FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_pokipkki(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT pokypki FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()


def get_price(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT price FROM tovar WHERE id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_pod(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT pod FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_free(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT free3 FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_timepod(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT timepod FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_coll_tovar():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT SUM(pokypki) FROM tovar"
    cur.execute(request)
    return cur.fetchone()

def get_tovar():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT id FROM tovar"
    cur.execute(request)
    return cur.fetchall()

def get_checkers_id():
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute(
            f"SELECT name FROM tovar")
        rows = cur.fetchall()
        l = []
        for row in rows:
            for x in row:
                l.append(x)
        return l

def update_balance(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET balance=balance+{balance} WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_balanceminus(balance, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET balance=balance-{balance} WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()


def update_name(name, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET name='{name}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_opis(info, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET info='{info}' WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_price(price, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET price={price} WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_timesub(time, id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET timesub='{time}' WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_buy(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE users SET pokypki=pokypki + 1 WHERE user_id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def update_buy_product(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"UPDATE tovar SET pokypki=pokypki + 1 WHERE id={id}"
    cur.execute(request)
    conn.commit()
    return cur.fetchone()

def get_pokypki(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT pokypki FROM users WHERE user_id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_src(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT Path FROM tovar WHERE id={id}"
    cur.execute(request)
    return cur.fetchone()

def get_nameadmin(id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    request = f"SELECT name FROM tovar WHERE id={id}"
    cur.execute(request)
    return cur.fetchone()