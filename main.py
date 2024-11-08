# from Tests.lab_1_tests import *
# from Tests.lab_2_tests import *
# from Tests.lab_3_tests import *

from Labs.lab_4 import *

encoder = BinaryEncryptor(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")
generator = SPNet(encoder)
encryptor = Lab4Temp(generator)

print('[Базовые интерфейсы без подложки]')
# sym2bin, isSym, msg2bin
tests = [
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ',
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ0011',
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ1110011011011',
]

# bin2msg
tests = [
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ',
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ00111',  # Тут лишняя единичка сравнительно с прошлыми тестами, вроде все отличия
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ1110011011011',
]

print('\n[Подложка]')
# check_padding, produce_padding, pad_message, unpad_message
# Тесты могут быть неправильно определены, в лабе нет вывода INPUTS_ARRAY
tests = [
    "ВА", "АЛИСА  А", "БОБ    А", "КОТОПОЕЗД",
    "ВБ", "АЛИСА АЖ", "БОБ   ОЧ", "ЕГИПТЯНИН",
    "В_", "АЛИСА ЯЗ", "БОБ   ЬЬ", "ЩЕГОЛЯНИЕ",
    "ВБ", "БОБ   ЬЬ", "АЛИСА ЯЗ", "ЭКЛАМПСИЯ",
    "ВБ", "БОБ   ЬЬ", "АЛИСА ЯЗ", "ЕГИПТЯНИН",
    "ВБ", "АЛИСА ЯЗ", "БОБ   ЬЬ", "ЕГИПТЯНИН",
]


print('\n[Подготовка пакетов + ксор блоков из 80 бит]')
# prepare_packet, validate_packet, transmit, receive, textor(попробовать уже сделанный ксор)

print('\n[CTR]')
# enc_CTR

print('\n[MAC CBC]')
# mac_CBC

print('\n[CCM]')
# CCM_frw, CCM_inv
