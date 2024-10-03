# Файл для тестирования лабораторной в процессе работы
from Labs.lab_2 import *

shift = Encryptor2(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")

print('[Алфавит]')
print(shift.data_alphabet)

print('\n[Работа с алфавитом]')
text_as_arr = shift.text2array("ВСЕМ ПРИВЕТ")
print(text_as_arr)
print(shift.array2text(text_as_arr))
print(shift.add_letters("Я", "Ж"))
print(shift.sub_letters("Я", "Ж"))

print('\n[Проверяем блоки]')
print(shift.block_to_number("АБВГ"))
print(shift.block_to_number(" ЯЗЬ"))
print(shift.block_to_number("ЯЯЯЯ"))
print(shift.block_to_number("ЯЯЯЯЯ"))
print(shift.block_to_number("ЯЯЯ"))

print('\n[Двоичный вид чисел]')
print('(34916):')
print(shift.to_byte(34916))
print(shift.from_byte('00001000100001100100')) # Возможно delete_zeros нужно убрать, не очень понятный пример
print(shift.from_byte(shift.to_byte(34916)))
print('(32028):')
print(shift.to_byte(32028))
print(shift.from_byte('111110100011100'))
print('(1048575):')
print(shift.to_byte(1048575))
print(shift.from_byte('11111111111111111111'))

print("\n[Цезарь]")
print(shift.oneside_caesar('ВАСЯ', 'АААА', 1))

print("\n[LCG]")
print(shift.make_coef([8677, 739], [11, 89], 20))
print(shift.make_coef([7927, 151], [3, 113], 20))

print(shift.count_bits(1231))
print(shift.count_bits(723482))

print(shift.compose_num(723482, 1231, 10))


