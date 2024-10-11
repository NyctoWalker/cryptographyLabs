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
        self.data_alphabet, self.dimension = self.add_alphabet(alphabet)

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
            coded_symbol = ""
            n = i
            while n > 0:
                coded_symbol = str(n % 2) + coded_symbol
                n = n // 2
            data_alphabet[text[i]] = "0"*(alphabet_dimension - len(coded_symbol)) + coded_symbol
        return data_alphabet, alphabet_dimension

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

    def byte_to_byte_array(self, _bytes: str):
        out: list(str) = []
        for i in range(self.dimension-1):
            out.append(_bytes[i*self.dimension:i*self.dimension + self.dimension])
        return out

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

    def number_to_block(self, number):
        bin = self.to_byte(number)
        out = ""
        if(len(bin) < 20):
            bin = "0"*(20 - len(bin)) + bin
        for i in range(4):
            out += self.array2text([bin[i*5:i*5+5]])
        return out

    #недоделано-----------------------------------------------------------------------------------------------------
    def caesar_encode(self, text_to_cypher, key):
        """
        Кодирование шифром Цезаря

        :param data_alphabet: Алфавит
        :param text_to_cypher: Зашифровываемый текст
        :param key: Ключ, от которого будет использован первый символ
        :return: Шифротекст
        """
        caesar_key = key[0]
        text_to_return = ""
        for l in text_to_cypher:
            text_to_return += self.add_letters(l, caesar_key)
        return text_to_return

    def shift_letter_by_number(self, letter, shift_value):
        return self.get_letter_by_id(((self.data_alphabet[letter] + shift_value) % len(self.data_alphabet.keys())))

    def shift_alphabet(self, text_to_shift, shift_value):
        text_to_return = ""
        for l in text_to_shift:
            text_to_return += self.shift_letter_by_number(l, shift_value)
        return text_to_return

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
            t_k = self.get_letter_by_id('00000')
            for i in range(4):
                q = (shift + i) % k
                t_k = self.add_letters(t_k, key[q])
                ret += self.add_letters(block_text[i], t_k)
            return ret

    def fwd_improve_block(self, block, key, initial_shift):
        t = key
        while initial_shift > len(t) - 4:
            t = t*2
        key = t[initial_shift:initial_shift+4]
        k = self.text2array(key)
        b = self.text2array(block)
        q = (self.from_byte(k[0]) + self.from_byte(k[1]) + self.from_byte(k[2]) + self.from_byte(k[3])) % 4
        for i in range(3):
            j = (q+i+1) % 4
            l = (q+i) % 4
            #_b = self.from_byte(b[l]) if type(b[l]) == str else b[l]
            b[j] = self.to_byte((self.from_byte(b[j]) + self.from_byte(b[l])) % len(self.data_alphabet))
        return self.array2text(b)

    def s_block_encode_modified(self, block, key, initial_shift):
        tmp = self.s_block_encode(block, key, initial_shift)
        return self.fwd_improve_block(tmp, key, initial_shift)

    def oneside_caesar(self, block: str, const, n):
        c = len(const)
        C = "ТПУ"+const+const[0:4]
        tmp = ""
        key: str = C[3:7]
        out = []
        for i in range(n):
            q = (i*4) % c + 3
            tmp = self.s_block_encode_modified(block, key, 0)
            s = self.block_to_number(tmp) % 4
            new_key = ""
            for j in range(4):
                new_key += self.add_letters(tmp[j], C[q-s+j])
            key = new_key
            out.append(tmp)
        return tmp
        #return tmp, out

    @staticmethod
    def make_coef(bpr, spr, pow):
        ss = min(spr)
        bs = min(bpr)
        bb = max(bpr)
        sb = max(spr)
        maximum = 2**pow - 1
        tmp = bs*ss
        a = ss * bs * sb + 1
        c = bb
        for i in range(pow):
            if tmp*ss >= maximum:
                break
            else:
                tmp = tmp*ss
        m = tmp
        if (a < m) or (c < m):
            out = [a, c, m]
        else:
            out = "wrong"
        return out

    def make_seed(self, block):
        str1 = "ПЕРВЫЙ ГЕНЕРАТОР"
        str2 = "ВТОРОЙ ГЕНЕРАТОР"
        str3 = "ТРЕТИЙ ГЕНЕРАТОР"
        out = []
        out.append(self.oneside_caesar(block, str1, 10))
        out.append(self.oneside_caesar(block, str2, 10))
        out.append(self.oneside_caesar(block, str3, 10))
        return out

    def seed_to_numbers(self, arrayseed):
        out = []
        for i in range(3):
            out.append(self.block_to_number(arrayseed[i]))
        return out
    def LCG_Next(self, state, coefs):
        a = coefs
        return (a[0]*state+a[1]) % a[2]

    def HCLGG(self, state, set):
        first = self.LCG_Next(state[0], set[0])
        second = self.LCG_Next(state[1], set[1])
        control = self.LCG_Next(state[2], set[2])
        n = self.count_bits(control)
        if control % 2 == 0:
            out = self.compose_num(first, second, n)
        else:
            out = self.compose_num(second, first, n)
        state_out = [first, second, control]
        return [out, state_out]

    def wrap_CHCLCG_next(self, init_flag, state_in, seed, set):
        out = ""
        stream = ""
        check = False
        state = []
        if init_flag == "up":
            for i in range(4):
                state.append(self.seed_to_numbers(self.make_seed(seed[i*4:i*4+4])))
            check = True
        elif(init_flag == "down"):
            state = state_in
            check = True
        if check:
            for j in range(4):
                tmp = 0
                sign = 1
                for i in range(4):
                    T = self.HCLGG(state[i], set)
                    state[i] = T[1]
                    tmp = (1048576 + sign*T[0]+tmp) % 1048576
                    sign = -sign
                stream = stream + self.number_to_block(tmp)
            out = [stream, state]
        return out
    @staticmethod
    def count_bits(num):
        rem = num
        out = 0
        for i in range(20):
            tmp = rem % 2
            rem = rem//2
            out = out + tmp
        return out

    def compose_num(self, num1, num2, cont):
        tmp = []
        if(cont > 0) and (cont < 20):
            arr1 = self.to_byte(num1)
            arr2 = self.to_byte(num2)
            if len(arr1) < len(arr2):
                arr1 = self.to_len(arr1, len(arr2))
            elif len(arr1) > len(arr2):
                arr2 = self.to_len(arr2, len(arr1))
            if(len(arr1)<20):
                arr1 = "0"*(20 - len(arr1)) + arr1
            if (len(arr2) < 20):
                arr2 = "0" * (20 - len(arr2)) + arr2
            for i in range(cont):
                tmp.append(arr1[i])
            for i in range(cont, 20):
                tmp.append(arr2[i])
            out = self.from_byte(tmp)
        elif cont == 0:
            out = num1
        else:
            out = num2
        return out

    @staticmethod
    def delete_zeros(symbol):
        out = 0
        for i in range(len(symbol)):
            if symbol[i] != "0":
                break
            out = out + 1
        return symbol[out:]

    @staticmethod
    def to_len(symbol, length):
        out_len = length - len(symbol)
        return "0"*out_len + symbol

    def to_byte(self, num):
        coded_symbol = ""
        n = num
        while n > 0:
            coded_symbol = str(n % 2) + coded_symbol
            n = n // 2
        return '0' * (self.dimension - len(coded_symbol)) + coded_symbol

    @staticmethod
    def from_byte(symbol):
        num = 0
        for i in range(len(symbol)):
            cur = len(symbol)-1-i
            sym = symbol[i]
            num = num + (2**cur)*int(sym)
        return num

    def from_byte_block(self, block: str):
        out: str = ""
        for l in block:
            out += self.from_byte(l)
        return out
