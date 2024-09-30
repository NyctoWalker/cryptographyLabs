# 2. Односторонняя функция через S-Блоки - 4 символа(20 бит), константа, кол-во раундов. На выходе 4 символа, 20 бит.
# 3. Простой конгруэнтный генератор
# 4. Усиление конгруэнтного генератора(см. лабу)
# 5. Интерфейс для распараллеливания 4 генераторов(?)
# 6. Исключение слабых и эквивалентных ключей


class Encryptor2:
    def __init__(self, alphabet):
        """
        Класс, отвечающий за шифрование.

        :param alphabet: Алфавит.
        """
        self.data_alphabet = self.add_alphabet(alphabet)

    def add_alphabet(self, text):
        """
        Нумерует каждый символ и превращает в алфавит

        :param data_alphabet: Словарь для записи алфавита
        :param text: Строка для посимвольного превращения в алфавит
        """
        data_alphabet = {}
        alphabet_len = len(text)
        alphabet_dimension = 1

        while alphabet_len > 2**alphabet_dimension:
            alphabet_dimension += 1

        for i in range(alphabet_len):
            num = self.to_byte(i)
            data_alphabet[text[i]] = "0"*(alphabet_dimension - len(num)) + num
        return data_alphabet

    def text2array(self, text):
        """
        Кодирование текста в виде массива индексов алфавита

        :param data_alphabet: Словарь с алфавитом
        :param text: Текст для кодирования
        :return: Массив с индексами символов
        """

        arr_return = []
        for i in text:
            arr_return.append(self.data_alphabet[i])
        return arr_return

    def array2text(self, array):
        """
        Декодирует массив индексов алфавита в символы алфавита

        :param data_alphabet: Алфавит
        :param array: Массив для декодирования
        :return: Декодированная строка
        """

        text_return = ""
        for i in array:
            text_return = text_return + self.get_letter_by_id(i)
        return text_return

    def get_letter_by_id(self, letter_id):
        """
        Получает символ алфавита по индексу

        :param data_alphabet: Словарь с алфавитом
        :param letter_id: Индекс символа
        :return: Символ
        """

        for i in self.data_alphabet.keys():
            if letter_id == self.data_alphabet[i]:
                return i

    def add_letters(self, letter_a, letter_b):
        """
        Получает символ из суммы индексов двух букв

        :param data_alphabet: Алфавит
        :param letter_a: Первая буква
        :param letter_b: Вторая буква
        :return: Буква, получаемая в результате сложения
        """

        let_a_id = self.data_alphabet[letter_a]
        let_b_id = self.data_alphabet[letter_b]

        numb = 0
        new_symbol = ""
        for i in range(len(let_a_id)):
            num = int(let_a_id[len(let_a_id) - 1 - i]) + int(let_b_id[len(let_b_id) - 1 - i]) + numb
            if num > 1:
                numb = 1
                num = num - 2
            new_symbol = str(num) + new_symbol
        return self.get_letter_by_id(new_symbol)

    def sub_letters(self, letter_a, letter_b):
        """
        Получает символ из вычетания индексов двух букв

        :param data_alphabet: Алфавит
        :param letter_a: Первая буква
        :param letter_b: Вычитаемая, вторая буква
        :return: Буква, получаемая в результате вычитания
        """

        let_a_id = self.data_alphabet[letter_a]
        let_b_id = self.data_alphabet[letter_b]

        numb = 0
        new_symbol = ""
        for i in range(len(let_a_id)):
            num = int(let_a_id[len(let_a_id) -1 -i]) - int(let_b_id[len(let_b_id) -1 -i]) - numb
            if num < 0:
                numb = 1
                num = num + 2
            new_symbol = str(num) + new_symbol
        return self.get_letter_by_id(new_symbol)

    def xor_letters(self, letter_a, letter_b):
        let_a_id = self.data_alphabet[letter_a]
        let_b_id = self.data_alphabet[letter_b]

        new_symbol = ""
        for i in range(len(let_a_id)):
            num = 0
            if let_b_id[i] != let_a_id[i]:
                num = 1
            new_symbol = new_symbol + str(num)

        return self.get_letter_by_id(new_symbol)

    def block_to_number(self, block_in):
        """
        Кодирует блок из 4 символов в численное значение по двоичному представлению

        :param block_in: Блок символов алфавита
        :return: Численное значение по двоичному представлению
        """

        out = ""
        if len(block_in) == 4:
            tmp = self.text2array(block_in)
            for i in range(4):
                out = out + tmp[i]
            return self.from_byte(out)
        else:
            return f"input error: ожидалось 4 символа, получено {len(block_in)}"

    @staticmethod
    def delete_zeros(symbol):
        out = 0
        for i in range(len(symbol)):
            if symbol[i] != "0":
                break
            out = out + 1
        return symbol[out:]

    @staticmethod
    def to_byte(num):
        coded_symbol = ""
        n = num
        while n > 0:
            coded_symbol = str(n % 2) + coded_symbol
            n = n // 2
        return coded_symbol

    @staticmethod
    def from_byte(symbol):
        num = 0
        for i in range(len(symbol)):
            cur = len(symbol)-1-i
            sym = symbol[i]
            num = num + (2**cur)*int(sym)
        return num
