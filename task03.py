'''Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?'''

'''С использованием биномиального распределения 
Количество сочетаний из 144 по 70
умножаем на вероятность одного выпадения орла в степени количества предполагаемых выпадений (0.5 в степени 70)
умножаем на вероятность одного невыпадения орла в степени количества предполагаемых неудач (0.5 в степени 74)
Получим вероятность выпадения орла 70 раз в 144 экспериментах 0.063'''

from math import factorial as fac

P = fac(144) * (0.5 ** 70) * (0.5 ** (144 - 70)) / (fac(70) * fac(144 - 70))
print(P)
