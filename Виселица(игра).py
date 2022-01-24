#Виселица
import random

words = ['саша','дмитрий','алексей','анатолий']
zhizni = 3
secret_word = random.choice(words)
s = "_" * len(secret_word)
r = "*" * len(secret_word)
print('Загадано слово:',r)

# Основной цикл

while zhizni != 0:
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", s,'\n')
    guest_letter = input('введите букву:')
    if guest_letter in secret_word:         # проверка буквы в загад.слове
        print("Буква есть в слове")
        otvet = ''
        for i in range(len(secret_word)):   #
            if guest_letter == secret_word[i]:
                otvet += guest_letter
            else:
                otvet += s[i]
        s = otvet
    else:
        zhizni -= 1
        print("Буквы нет в слове,Осталось",zhizni,"жизней",'\n')

    if zhizni == 0:
        print('Ты проиграл,загаданоое слово :',secret_word)
