from Labs.lab_2 import *

# Вариант - SP-сеть
# 2. Блоки перестановки: P-блок для SP-сети с доп. условиями из задания к лабораторной
# 3. Раундовая функция для SP-сети при помощи S и P-блоков
# 4. Интерфейс с использованием раундовой функции для блочного шифрования - 16 символов вход, ключ, выход
# 5. Составить набор тестов и протестировать диффузию и запутанность. Сделать небольшие выводы.
# По мере выполнения пунктов задания соответствующие пункты выше, после тестирования, удалять
# Использовать методы из второй лабораторной, во временном классе ниже писать только новые необходимые методы
# После работы нужно выдернуть класс второй лабораторной и сделать полноценный класс


class Lab3TempClass:
    def __init__(self, encryptor: BinaryEncryptor):
        self.encryptor = encryptor

    @staticmethod
    def make_lcg_set():
        return [[723482, 8677, 983609], [252564, 9109, 961193], [357630, 8971, 948209]]

    def produce_round_keys(self, key_in, num_in):
        _iter, tmp, out = [], [], []
        set = self.make_lcg_set()

        tmp = self.encryptor.wrap_CHCLCGM_next('up', -1, key_in, set)
        out.append(tmp[0])
        if num_in > 1:
            for i in range(1, num_in):
                tmp = self.encryptor.wrap_CHCLCGM_next('down', tmp[1], -1, set)
                out.append(tmp[0])
        return out

    @staticmethod
    def get_magic_square(num: int):
        match num:
            case 1:
                return ([16, 3, 2, 13],
                        [5, 10, 11, 8],
                        [9, 6, 7, 12],
                        [4, 15, 14, 1])
            case 2:
                return ([7, 14, 4, 9],
                        [12, 1, 15, 6],
                        [13, 8, 10, 3],
                        [2, 11, 5, 16])
            case _:
                return ([4, 14, 15, 1],
                        [9, 7, 6, 12],
                        [5, 11, 10, 8],
                        [16, 2, 3, 13])

    @staticmethod
    def frw_magic_square(block_in: str, msqr_in: get_magic_square(num=-1)):
        if len(block_in) != 16:
            raise ValueError('Длина блока текста должна равняться 16 символам')
        out = ""
        for i in range(4):
            for j in range(4):
                out += block_in[msqr_in[i][j] - 1]
        return out

    @staticmethod
    def inv_magic_square(block_in: str, msqr_in: get_magic_square(num=-1)):
        if len(block_in) != 16:
            raise ValueError('Длина блока текста должна равняться 16 символам')
        tmp: list = [" "]*16
        d = list(block_in)
        for i in range(4):
            for j in range(4):
                tmp[msqr_in[i][j] - 1] = d[4*i+j]
        return ''.join(tmp)
