# Структура для хранения алфавита (5-битовые числа, индексы 0-31)
# Функция для зашифровывания символа
# Посимвольное преобразование блока текста
# Написать полиалфавитные преобразования
# Обёртка для блоков по 4 символа, проверить работу S-Блоков
# Усиление S-блоков

dataalphabet = {}

def getletterbyid(id):
    for i in dataalphabet.keys():
        if id == dataalphabet[i]:
            return i

def addalphabet(text):
    for i in range(len(text)):
        dataalphabet[text[i]] = i

def text2array(text):
    arrreturn = []
    for i in text:
        arrreturn.append(dataalphabet[i])
    return arrreturn

def array2text(array):
    textreturn = ""
    for i in array:
        textreturn = textreturn + getletterbyid(i)
    return textreturn

def add_letters(letter_a, letter_b):
    letaid = dataalphabet[letter_a]
    letbid = dataalphabet[letter_b]
    letterid = (letaid + letbid) % len(dataalphabet.keys())
    return getletterbyid(letterid)

def sub_letters(letter_a, letter_b):
    letaid = dataalphabet[letter_a]
    letbid = dataalphabet[letter_b]
    letterid = (letaid - letbid + len(dataalphabet.keys())) % len(dataalphabet.keys())
    return getletterbyid(letterid)

addalphabet(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")
print(dataalphabet)
textasarr = text2array("ВСЕМ ПРИВЕТ")
print(textasarr)
print(array2text(textasarr))
print(add_letters("Я", "Ж"))
print(sub_letters("А", "Ж"))