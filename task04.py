'''В первом ящике находится 10 мячей, из которых 7 - белые.
Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча.'''

'''Какова вероятность того, что все мячи белые?'''
'''Перемножаем вероятности выпадения каждого последующего события
Из первого ящика 7 из 10 и 6 из 9
Из вторго ящика 9 из 11 и 8 из 10
Вероятность выпадения 4х белых мячей 0.305'''

P = (7 / 10) * (6 / 9) * (9 / 11) * (8 / 10)
print(P)

'''Какова вероятность того, что ровно два мяча белые? '''
'''1. два шара из перового и ни одного из второго (7 / 10) * (6 / 9) * (2 / 11) * (1 / 10)
ИЛИ 2. два шара из второго и ни одного из первого (9 / 11) * (8 / 10) * (3 / 10) * (2 / 9)
ИЛИ 3. первый из первого и первый из второго (7 / 10) * (9 / 11) * (3 / 9) * (2 / 10)
ИЛИ 4. второй из первого и второй из второго (3 / 10) * (7 / 9) * (2 / 11) * (9 / 10)
ИЛИ 5. первый из первого и второй из второго (7 / 10) * (3 / 9) * (2 / 11) * (9 / 10)
ИЛИ 6. второй из первого и первый из второго (3 / 10) * (7 / 9) * (9 / 11) * (2 / 10)
Вероятности суммируем, так как достаточно выполнения одного из них
Получаем 0.205'''

P = (7 / 10) * (6 / 9) * (2 / 11) * (1 / 10) + (9 / 11) * (8 / 10) * (3 / 10) * (2 / 9) + (7 / 10) * (9 / 11) * (
        3 / 9) * (2 / 10) + (3 / 10) * (7 / 9) * (2 / 11) * (9 / 10) + (7 / 10) * (3 / 9) * (2 / 11) * (9 / 10) + (
            3 / 10) * (7 / 9) * (9 / 11) * (2 / 10)
print(P)

'''Какова вероятность того, что хотя бы один мяч белый? = 0.9988'''
'''Необходимо из всего (1) вычесть  вероятность, что все черные (3 / 10) * (2 / 9) * (2 / 11) * (1 / 10)'''

P = 1 - (3 / 10) * (2 / 9) * (2 / 11) * (1 / 10)
print(P)