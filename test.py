from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMethods
import random
QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6ImlwdjFqai0wMCIsInVzZXJfaWQiOiI3OTE3OTAzODIzNiIsInNlY3JldCI6ImEzOTU0Y2RkN2M2ZDJiODk4NWI1OGI3ZTE4NzNjNGU2M2I0MzZlZTdjMjA3NTg4Y2JjYjY4MjFjNTlkZDJkNzYifX0="

p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)

# Выставим счет на сумму 228 рублей который будет работать 45 минут
new_bill = p2p.bill(bill_id=random.randint(11111111, 999999999), amount=228, lifetime=45)

print(new_bill.bill_id, new_bill.pay_url)
print(new_bill)

# Проверим статус выставленного счета
while True:
    if p2p.check(bill_id=new_bill.bill_id).status == 'PAID':
        break
    else:
        print(p2p.check(bill_id=new_bill.bill_id).status)

# Потеряли ссылку на оплату счета? Не пробле