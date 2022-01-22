#Виселица
import random

print('Приветсвую тебя мой дорогой друг. Давай сыграем','\n')

my_message = ['саша','дима']
d = random.choice(my_message)
zhizn = len(d)
vvod = ""
otvet = ""

while zhizn != 0:
    guest_word = input('введите букву:')
    for i in guest_word:
        if i not in d:
            zhizn -= 1
            print('не правильная буква,осталось',zhizn,'попытки','\n')

        if i in d:
            print('буква есть в слове','\n')
            otvet += i
            print(otvet)

    if otvet == d:
        print('ты выиграл,правильный ответ:',otvet)
        break

    if zhizn == 0:
        print('ты проиграл,правильное слово:',d)
