# Функция для зашифровывания символа(сделано для зашифровывания текста)
# Посимвольное преобразование блока текста
# Написать полиалфавитные преобразования
# Обёртка для блоков по 4 символа, проверить работу S-Блоков
# Усиление S-блоков

# data_alphabet = {}


def get_letter_by_id(data_alphabet, id):
    '''
    Получает символ алфавита по индексу

    :param data_alphabet: Словарь с алфавитом
    :param id: Индекс символа
    :return: Символ
    '''
    for i in data_alphabet.keys():
        if id == data_alphabet[i]:
            return i


def add_alphabet(data_alphabet, text):
    '''
    Нумерует каждый символ и превращает в алфавит

    :param data_alphabet: Словарь для записи алфавита
    :param text: Строка для посимвольного превращения в алфавит
    '''
    for i in range(len(text)):
        data_alphabet[text[i]] = i


def text2array(data_alphabet, text):
    '''
    Кодирование текста в виде массива индексов алфавита

    :param data_alphabet: Словарь с алфавитом
    :param text: Текст для кодирования
    :return: Массив с индексами символов
    '''
    arr_return = []
    for i in text:
        arr_return.append(data_alphabet[i])
    return arr_return


def array2text(data_alphabet, array):
    '''
    Декодирует массив индексов алфавита в символы алфавита

    :param data_alphabet: Алфавит
    :param array: Массив для декодирования
    :return: Декодированная строка
    '''
    text_return = ""
    for i in array:
        text_return = text_return + get_letter_by_id(data_alphabet, i)
    return text_return


def add_letters(data_alphabet, letter_a, letter_b):
    '''
    Получает символ из суммы индексов двух букв

    :param data_alphabet: Алфавит
    :param letter_a: Первая буква
    :param letter_b: Вторая буква
    :return: Буква, получаемая в результате сложения
    '''

    let_a_id = data_alphabet[letter_a]
    let_b_id = data_alphabet[letter_b]
    letter_id = (let_a_id + let_b_id) % len(data_alphabet.keys())
    return get_letter_by_id(data_alphabet, letter_id)


def sub_letters(data_alphabet, letter_a, letter_b):
    '''
    Получает символ из вычетания индексов двух букв

    :param data_alphabet: Алфавит
    :param letter_a: Первая буква
    :param letter_b: Вычитаемая, вторая буква
    :return: Буква, получаемая в результате вычитания
    '''

    let_a_id = data_alphabet[letter_a]
    let_b_id = data_alphabet[letter_b]
    letter_id = (let_a_id - let_b_id + len(data_alphabet.keys())) % len(data_alphabet.keys())
    return get_letter_by_id(data_alphabet, letter_id)


def caesar_encode(data_alphabet, text_to_cypher, key):
    caesar_key = key[0]
    text_to_return = ""
    for l in text_to_cypher:
        text_to_return += add_letters(data_alphabet, l, caesar_key)
    return text_to_return


def caesar_decode(data_alphabet, text_to_decypher, key):
    caesar_key = key[0]
    text_to_return = ""
    for l in text_to_decypher:
        text_to_return += sub_letters(data_alphabet, l, caesar_key)
    return text_to_return


def shift_alphabet(data_alphabet, text_to_shift, shift_value):
    text_to_return = ""
    for l in text_to_shift:
        text_to_return += get_letter_by_id(data_alphabet, ((data_alphabet[l] + shift_value) % len(data_alphabet.keys())))
    return text_to_return
