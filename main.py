# from Tests.lab_1_tests import *
# from Tests.lab_2_tests import *
from Labs.lab_2 import *
from Labs.lab_3 import *

encoder = BinaryEncryptor(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")
lab = Lab3TempClass(encoder)

print('[Блочный xor и сложение строк]')
print(encoder.xor_block('АГАТ', 'ТАГА'))
print(encoder.xor_block("КОЛЕНЬКА", "МТВ ТЛЕН"))
print(encoder.xor_block("ТОРТ ХОЧЕТ ГОРКУ", "МТВ ВСЕ ЕЩЕ ТЛЕН"))
print(encoder.add_block("ТОРТ ХОЧЕТ ГОРКУ", "МТВ ВСЕ ЕЩЕ ТЛЕН"))  # Сложение текста
print(encoder.xor_block("ЮЬСТВГИЧ ИЕГЬЭМЩ", "МТВ ВСЕ ЕЩЕ ТЛЕН"))  # Обратный xor

print('\n[LCG-сет]')
print(lab.make_lcg_set())

print('\n[Генерация раундовых ключей]')
key = 'ПОЛИМАТ ТЕХНОБОГ'
print(len(key))
print(lab.produce_round_keys(key, 5))
