# Наш вариант - CTR+CBC-MAC
# 1. Реализовать алгоритм наложения (снятия) подложки на сообщение, а также конвейер обработки отправляемых и
# принимаемых сообщений.
# 2. Предусмотреть интерфейсы для использования тестов. Тесты, которые используются  в приложении, опираются на данные,
# включённые в текстовые файлы.
# 3. Реализовать криптографическую основу протокола. Наш вариант - подход MAC then Encrypt с применением режимов
# CTR и CBC.
# 4. Реализовать программный компонент отвечающий за сессию протокола. Убедиться, что в рамках приёма и передачи
# сообщений не производится значимого объёма необязательных вычислений (отсутствует повторный пересчёт известных значений).
# 5. Провести комплексное тестирование полученного решения. Предусмотреть этап верификации (корректность реализации
# относительно указаний в приложении) и валидации (корректности функционирования с точки зрения практической задачи)
# модели протокола.
# 6. Продемонстрировать устойчивость/уязвимость протокола или его составных частей к различным атакам, в том числе,
# опирающимся на «шифрооракула». Формально-логически проанализировать алгоритм с точки зрения полученной информации,
# сделать соответствующие выводы об использованной реализации криптографического решения.

# После выполнения пункта задания, соответствующие комментарии удалить.

from Labs.lab_3 import *
import sys


class Lab4Temp:
    def __init__(self, sp_net: SPNet):
        self.sp_net = SPNet
        self.encoder = sp_net.get_encryptor()

    #region Двоичные_представления
    # Скорее всего это написано неправильно, см. документацию по str2vec для маткада
    def sym2bin(self, s_in: str):
        if len(s_in) != 1:
            raise ValueError(f'sym2bin: получена строка с длиной {len(s_in)} вместо символа или бита')

        if s_in == '1':
            return 1
        elif s_in == '0':
            return 0
        else:
            return self.encoder.to_byte(self.encoder.block_to_number(s_in))  # Под замену, непонятно что в примере подразумевалось

    def is_sym(self, s_in: str):
        return s_in in self.encoder.data_alphabet

    def msg2bin(self, msg_in):
        _m = len(msg_in)
        i, f = 0, 0
        tmp = [' '*_m]
        while self.is_sym(msg_in[i]):
            c = self.encoder.block_to_number(msg_in[i])
            for j in range(5):
                tmp[i*5 + 4 - j] = '0' if c % 2 == 0 else '1'
                c = c // 2
            if i == _m-1:
                f=1
                break
            else:
                i += 1
        if f == 0:
            for k in range(i, _m):
                tmp[4*i+k] = self.sym2bin(msg_in[k])
        return self.encoder.array2text(tmp)

    def bin2msg(self, bin_in):
        _B = len(bin_in)
        b = _B // 5
        q = _B % 5
        out = ""
        for i in range(b):
            t = 0
            for j in range(5):
                t = 2*t + int(bin_in[i*5+j])
            out += self.encoder.number_to_block(t)
        if q > 0:
            for k in range(1, q+1):
                out += self.encoder.number_to_block(bin_in[b*5+k-1])
        return out
    # endregion

    # region Подложки

    def check_padding(self, bin_msg_in):
        _m = len(bin_msg_in)
        blocks_num = _m // 80
        remainder = _m % 80
        if remainder == 0:
            # Я сдаюсь, не смог разобраться что берётся в submatrix
            pass

    def produce_padding(self):
        pass

    def pad_message(self):
        pass

    def unpad_message(self):
        pass

    # endregion

    # region Пакеты

    def prepare_packet(self):
        pass

    def validate_packet(self):
        pass

    def transmit(self):
        pass

    def receive(self):
        pass

    # Возможно, не нужно реализовывать
    def textor(self):
        pass

    # endregion

    # region CCM

    def enc_CTR(self):
        pass

    def mac_CBC(self):
        pass

    def CCM_frw(self):
        pass

    def CCM_inv(self):
        pass

    # endregion
