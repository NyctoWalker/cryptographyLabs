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

print('\n[Магические квадраты]')
print(type(lab.get_magic_square(1)))
print(f'''{lab.get_magic_square(1)}\n{lab.get_magic_square(2)}\n{lab.get_magic_square(3)}''')
_in = "АБВГДЕЖЗИЙКЛМНОП"
print(f'''
{lab.frw_magic_square(_in, lab.get_magic_square(1))}
{lab.frw_magic_square(_in, lab.get_magic_square(2))}
{lab.frw_magic_square(_in, lab.get_magic_square(3))}''')
print(f'''
{lab.inv_magic_square(lab.frw_magic_square(_in, lab.get_magic_square(1)), lab.get_magic_square(1))}
{lab.inv_magic_square(lab.frw_magic_square(_in, lab.get_magic_square(2)), lab.get_magic_square(2))}
{lab.inv_magic_square(lab.frw_magic_square(_in, lab.get_magic_square(3)), lab.get_magic_square(3))}''')

print('\n[Двоичные смещения и преобразования]')
_in = "ЗОЛОТАЯ СЕРЕДИНА"
print(encoder.text_to_byte_string(_in))
print(encoder.byte_string_to_text(encoder.text_to_byte_string(_in)))
# Дальше написать binary shift
