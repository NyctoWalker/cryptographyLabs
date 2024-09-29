# 1. Бинарные преобразования и блоки 20 бит в инт и обратно
# 1. (наверное можно до 32-64 бит, просто для 32-битного алфавита каждый символ 5 бит, а блоки по 4 символа)
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
        alphabetlen = len(text)
        alphabetdimension = 1

        while alphabetlen > 2**alphabetdimension:
            alphabetdimension+=1


        for i in range(len(text)):
            num = self.to_byte(i)
            data_alphabet[text[i]] = "0"*(alphabetdimension-len(num)) + num
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

    def get_letter_by_id(self, id):
        """
        Получает символ алфавита по индексу

        :param data_alphabet: Словарь с алфавитом
        :param id: Индекс символа
        :return: Символ
        """
        for i in self.data_alphabet.keys():
            if id == self.data_alphabet[i]:
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
        newsymbol = ""
        for i in range(len(let_a_id)):
            num = int(let_a_id[len(let_a_id) - 1 - i]) + int(let_b_id[len(let_b_id) - 1 - i]) + numb
            if (num > 1):
                numb = 1
                num = num - 2
            newsymbol = str(num) + newsymbol
        return self.get_letter_by_id(newsymbol)

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
        newsymbol = ""
        for i in range(len(let_a_id)):
            num = int(let_a_id[len(let_a_id) -1 -i]) - int(let_b_id[len(let_b_id) -1 -i]) - numb
            if(num < 0):
                numb = 1
                num = num + 2
            newsymbol = str(num) + newsymbol
        return self.get_letter_by_id(newsymbol)

    def xor_letters(self, letter_a, letter_b):
        let_a_id = self.data_alphabet[letter_a]
        let_b_id = self.data_alphabet[letter_b]

        newsymbol = ""
        for i in range(len(let_a_id)):
            num = 0
            if(let_b_id[i] != let_a_id[i]):
                num = 1
            newsymbol = newsymbol + str(num)

        return self.get_letter_by_id(newsymbol)

    def block_to_number(self, blockin):
        out = ""
        if(len(blockin) == 4):
            tmp = self.text2array(blockin)
            for i in range(4):
                out = out + tmp[i]
            return self.from_byte(out)
        else:
            return "input error"

    def delete_zeros(self, symbol):
        out = 0
        for i in range(len(symbol)):
            if(symbol[i] != "0"):
                break
            out = out + 1
        return symbol[out:]


    def to_byte(self, num):
        codedsymbol = ""
        n = num
        while n > 0:
            codedsymbol = str(n % 2) + codedsymbol
            n = n // 2
        return codedsymbol

    def from_byte(self, symbol):
        num = 0
        for i in range(len(symbol)):
            cur = len(symbol)-1-i
            sym = symbol[i]
            num = num + (2**cur)*int(sym)
        return num