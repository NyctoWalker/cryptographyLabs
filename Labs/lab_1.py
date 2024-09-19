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


def shift_letter_by_number(data_alphabet, letter, shift_value):
    '''
    Получает смещённый символ алфавита

    :param data_alphabet: Словарь с алфавитом
    :param letter: Буква
    :param shift_value: Смещение
    :return: Символ
    '''
    return get_letter_by_id(data_alphabet, ((data_alphabet[letter] + shift_value) % len(data_alphabet.keys())))


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
        text_to_return += shift_letter_by_number(data_alphabet, l, shift_value)
    return text_to_return


def vidgener_encode(value, key, data_alphabet, j_in):
    lis = ""
    t_k = " "
    for v in range(len(value)):
        t_i = value[v]
        q = (v + j_in) % len(key)
        t_k = add_letters(data_alphabet, t_k, key[q])
        go = add_letters(data_alphabet, t_i, t_k)
        lis += go
    return lis


def vidgener_decode(value, key, data_alphabet, j_in):
    lis = ""
    t_k = " "
    for v in range(len(value)):
        t_i = value[v]
        q = (v + j_in) % len(key)
        t_k = add_letters(data_alphabet, t_k, key[q])
        go = sub_letters(data_alphabet, t_i, t_k)
        lis += go
    return lis

def s_block_encode(data_alphabet, block_text, key, shift):
    if len(block_text) != 4:
        return "Ошибка: длина входного блока должна быть равна 4"
    else:
        ret = ""
        k = len(key)
        t_k = get_letter_by_id(data_alphabet, 0)
        for i in range(4):
            q = (shift + i) % k
            t_k = add_letters(data_alphabet, t_k, key[q])
            ret += add_letters(data_alphabet, block_text[i], t_k)
        return ret


def s_block_decode(data_alphabet, encoded_block_text, key, initial_shift):
    if len(encoded_block_text) != 4:
        return "Ошибка: длина входного блока должна быть равна 4"
    else:
        ret = ""
        k = len(key)
        t_k = get_letter_by_id(data_alphabet, 0)
        for i in range(4):
            q = (initial_shift + i) % k
            t_k = add_letters(data_alphabet, t_k, key[q])
            ret += sub_letters(data_alphabet, encoded_block_text[i], t_k)
        return ret


def fwd_improve_block(data_alphabet, block, key, initial_shift):
    t = key
    while initial_shift > len(t) - 4:
        t = t*2
    key = t[initial_shift:initial_shift+4]
    k = text2array(data_alphabet, key)
    b = text2array(data_alphabet, block)
    q = (k[0] + k[1] + k[2] + k[3])%4
    for i in range(3):
        j = (q+i+1) % 4
        l = (q+i) % 4
        b[j] = (b[j] + b[l]) % 32
    return array2text(data_alphabet, b)

def inv_improve_block(data_alphabet, block, key, initial_shift):
    t = key
    while initial_shift > len(t) - 4:
        t = t*2
    key = t[initial_shift:initial_shift+4]
    k = text2array(data_alphabet, key)
    b = text2array(data_alphabet, block)
    q = (k[0] + k[1] + k[2] + k[3])%4
    for i in range(2, -1, -1):
        j = (q+i+1) % 4
        l = (q+i) % 4
        b[j] = (b[j] - b[l] + 32) % 32
    return array2text(data_alphabet, b)

def s_block_encode_modified(data_alphabet, block, key, initial_shift):
    tmp = s_block_encode(data_alphabet, block, key, initial_shift)
    return fwd_improve_block(data_alphabet, tmp, key, initial_shift)

def s_block_decode_modified(data_alphabet, block, key, initial_shift):
    tmp = s_block_decode(data_alphabet, block, key, initial_shift)
    return inv_improve_block(data_alphabet, tmp, key, initial_shift)