# data_alphabet = {}

class Encryptor:
    def __init__(self, alphabet):
        """
        Класс, отвечающий за шифрование.

        :param alphabet: Алфавит.
        """
        self.data_alphabet = self.add_alphabet(alphabet)
    def get_letter_by_id(self, id):
        '''
        Получает символ алфавита по индексу

        :param data_alphabet: Словарь с алфавитом
        :param id: Индекс символа
        :return: Символ
        '''
        for i in self.data_alphabet.keys():
            if id == self.data_alphabet[i]:
                return i


    def shift_letter_by_number(self, letter, shift_value):
        '''
        Получает смещённый символ алфавита

        :param letter: Буква
        :param shift_value: Смещение
        :return: Символ
        '''
        return self.get_letter_by_id(((self.data_alphabet[letter] + shift_value) % len(self.data_alphabet.keys())))


    def add_alphabet(self, text):
        '''
        Нумерует каждый символ и превращает в алфавит

        :param data_alphabet: Словарь для записи алфавита
        :param text: Строка для посимвольного превращения в алфавит
        '''
        data_alphabet = {}
        for i in range(len(text)):
            data_alphabet[text[i]] = i
        return data_alphabet


    def text2array(self, text):
        '''
        Кодирование текста в виде массива индексов алфавита

        :param data_alphabet: Словарь с алфавитом
        :param text: Текст для кодирования
        :return: Массив с индексами символов
        '''
        arr_return = []
        for i in text:
            arr_return.append(self.data_alphabet[i])
        return arr_return


    def array2text(self, array):
        '''
        Декодирует массив индексов алфавита в символы алфавита

        :param data_alphabet: Алфавит
        :param array: Массив для декодирования
        :return: Декодированная строка
        '''
        text_return = ""
        for i in array:
            text_return = text_return + self.get_letter_by_id(i)
        return text_return


    def add_letters(self, letter_a, letter_b):
        '''
        Получает символ из суммы индексов двух букв

        :param data_alphabet: Алфавит
        :param letter_a: Первая буква
        :param letter_b: Вторая буква
        :return: Буква, получаемая в результате сложения
        '''

        let_a_id = self.data_alphabet[letter_a]
        let_b_id = self.data_alphabet[letter_b]
        letter_id = (let_a_id + let_b_id) % len(self.data_alphabet.keys())
        return self.get_letter_by_id(letter_id)


    def sub_letters(self, letter_a, letter_b):
        '''
        Получает символ из вычетания индексов двух букв

        :param data_alphabet: Алфавит
        :param letter_a: Первая буква
        :param letter_b: Вычитаемая, вторая буква
        :return: Буква, получаемая в результате вычитания
        '''

        let_a_id = self.data_alphabet[letter_a]
        let_b_id = self.data_alphabet[letter_b]
        letter_id = (let_a_id - let_b_id + len(self.data_alphabet.keys())) % len(self.data_alphabet.keys())
        return self.get_letter_by_id(letter_id)


    def caesar_encode(self, text_to_cypher, key):
        '''
        Кодирование шифром Цезаря

        :param data_alphabet: Алфавит
        :param text_to_cypher: Зашифровываемый текст
        :param key: Ключ, от которого будет использован первый символ
        :return: Шифротекст
        '''
        caesar_key = key[0]
        text_to_return = ""
        for l in text_to_cypher:
            text_to_return += self.add_letters(l, caesar_key)
        return text_to_return


    def caesar_decode(self, text_to_decypher, key):
        '''
        Расшифровывает шифротекст, созданный с применением шифра Цезаря

        :param data_alphabet: Алфавит
        :param text_to_decypher: Шифротекст
        :param key: Ключ, от которого будет использован первый символ
        :return: Декодированный текст
        '''
        caesar_key = key[0]
        text_to_return = ""
        for l in text_to_decypher:
            text_to_return += self.sub_letters(l, caesar_key)
        return text_to_return


    def shift_alphabet(self, text_to_shift, shift_value):
        '''
        Смещает весь текст на заданное количество позиций

        :param data_alphabet: Алфавит
        :param text_to_shift: Строка для смещения по алфавиту
        :param shift_value: Значение смещения
        :return: Строка, соответствующая смещённому алфавиту
        '''
        text_to_return = ""
        for l in text_to_shift:
            text_to_return += self.shift_letter_by_number(l, shift_value)
        return text_to_return


    def vidgener_encode(self, value, key, j_in):
        '''
        Зашифровывает текст при помощи шифра Виженера

        :param value: Зашифровываемый текст
        :param key: Ключ
        :param j_in: Смещение
        :return: Шифротекст
        '''
        lis = ""
        t_k = " "
        for v in range(len(value)):
            t_i = value[v]
            q = (v + j_in) % len(key)
            t_k = self.add_letters(t_k, key[q])
            go = self.add_letters(t_i, t_k)
            lis += go
        return lis


    def vidgener_decode(self, value, key, j_in):
        """
        Расшифровывает текст, закодированный при помощи шифра Виженера

        :param value: Шифротекст
        :param key: Ключ
        :param data_alphabet: Алфавит
        :param j_in: Смещение
        :return: Расшифрованная строка
        """
        lis = ""
        t_k = " "
        for v in range(len(value)):
            t_i = value[v]
            q = (v + j_in) % len(key)
            t_k = self.add_letters(t_k, key[q])
            go = self.sub_letters(t_i, t_k)
            lis += go
        return lis


    def s_block_encode(self, block_text, key, shift):
        """
        Кодирует S-блоки по 4 символа

        :param data_alphabet: Алфавит
        :param block_text: Блок текста
        :param key: Ключ
        :param shift: Смещение
        :return: Закодированный блок
        """
        if len(block_text) != 4:
            return "Ошибка: длина входного блока должна быть равна 4"
        else:
            ret = ""
            k = len(key)
            t_k = self.get_letter_by_id(0)
            for i in range(4):
                q = (shift + i) % k
                t_k = self.add_letters(t_k, key[q])
                ret += self.add_letters(block_text[i], t_k)
            return ret


    def s_block_decode(self, encoded_block_text, key, initial_shift):
        """
        Расшифровывает s-блок размером 4 символа

        :param data_alphabet: Алфавит
        :param encoded_block_text: Шифротекст
        :param key: Ключ
        :param initial_shift: Изначальное смещение, второй ключ
        :return: Расшифрованный текст
        """
        if len(encoded_block_text) != 4:
            return "Ошибка: длина входного блока должна быть равна 4"
        else:
            ret = ""
            k = len(key)
            t_k = self.get_letter_by_id(0)
            for i in range(4):
                q = (initial_shift + i) % k
                t_k = self.add_letters(t_k, key[q])
                ret += self.sub_letters(encoded_block_text[i], t_k)
            return ret


    def fwd_improve_block(self, block, key, initial_shift):
        t = key
        while initial_shift > len(t) - 4:
            t = t*2
        key = t[initial_shift:initial_shift+4]
        k = self.text2array(key)
        b = self.text2array(block)
        q = (k[0] + k[1] + k[2] + k[3])%4
        for i in range(3):
            j = (q+i+1) % 4
            l = (q+i) % 4
            b[j] = (b[j] + b[l]) % len(self.data_alphabet)
        return self.array2text(b)


    def inv_improve_block(self, block, key, initial_shift):
        t = key
        while initial_shift > len(t) - 4:
            t = t*2
        key = t[initial_shift:initial_shift+4]
        k = self.text2array(key)
        b = self.text2array(block)
        q = (k[0] + k[1] + k[2] + k[3])%4
        for i in range(2, -1, -1):
            j = (q+i+1) % 4
            l = (q+i) % 4
            b[j] = (b[j] - b[l] + len(self.data_alphabet)) % len(self.data_alphabet)
        return self.array2text(b)


    def s_block_encode_modified(self, block, key, initial_shift):
        tmp = self.s_block_encode(block, key, initial_shift)
        return self.fwd_improve_block(tmp, key, initial_shift)


    def s_block_decode_modified(self, block, key, initial_shift):
        tmp = self.s_block_decode(block, key, initial_shift)
        return self.inv_improve_block(tmp, key, initial_shift)
