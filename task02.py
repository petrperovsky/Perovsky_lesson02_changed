'''Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
Какова вероятность, что ни одна из них не перегорит в первый день?
Какова вероятность, что перегорят ровно две?'''

'''Использую распределение Пуассона 
(достаточно большое количество испытаний c низкой вероятностью наступления события).
На 5000 тысч лампочек должно в среднем перегореть 2.
Вероятность, что не перегорит ни одна (т.е. 0): (2^0 / 0!) * e ^-2 = 0.13.
Вероятность, что перегорит 2 лампочки : (2^2 / 2!) * e ^-2 =  0.27'''

from math import factorial as fac
from math import e as e

P_none = (2 ** 0) / (fac(0)) * (e ** -2)
print(P_none)

P_2 = (2 ** 2) / (fac(2)) * (e ** -2)
print(P_2)
