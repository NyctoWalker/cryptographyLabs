from Labs.lab_1 import *


shift = Encryptor(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")

print('[Алфавит]')
print(shift.data_alphabet)

print('\n[Работа с алфавитом]')
text_as_arr = shift.text2array("ВСЕМ ПРИВЕТ")
print(text_as_arr)
print(shift.array2text(text_as_arr))
print(shift.add_letters("Я", "Ж"))
print(shift.sub_letters("Е", "Ж"))

print('\n[Цезарь]')
print(shift.caesar_encode("ПОЛДЕНЬ", "ВЕРСАЛЬ")) # Должно получиться ТСОЗИРЯ
print(shift.caesar_decode( shift.caesar_encode("ПОЛДЕНЬ", "ВЕРСАЛЬ"), "ВЕРСАЛЬ")) # Должно получиться ПОЛДЕНЬ
print(shift.caesar_encode("СЫЗРАНЬ", "А")) # Должно получиться ТЬИСБОЭ
print(shift.caesar_encode( "ОЛОЛО КРИНЖ", "Х")) # Должно получиться ДБДБДХАЖЯГЭ

print('\n[Смещение алфавита]')
print(shift.shift_alphabet(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ", 1))
print(shift.shift_alphabet(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ", -1))
print(shift.shift_alphabet("ПОЛДЕНЬ", 3)) # Должно получиться ТСОЗИРЯ

print('\n[Виженер]')
print(shift.vidgener_encode("ОЛОЛО КРИНЖ", "ПАНТЕОН", 0)) # Должно получиться ЯЭНЮЖЖ ХОБН
print(shift.vidgener_decode(shift.vidgener_encode("ОЛОЛО КРИНЖ", "ПАНТЕОН", 1), "ПАНТЕОН", 1)) # Должно получиться ОЛОЛО КРИНЖ

print('\n[S-блоки]')
print(shift.s_block_encode("БЛО", "ЗВЕЗДНАЯ НОЧЬ", 11)) # Ошибка
print(shift.s_block_encode("БЛОК", "ЗВЕЗДНАЯ НОЧЬ", 11)) # Должно получиться Щ КЙ
print(shift.s_block_encode("РОКТ", "А  А", 0))
# Должно получиться БЛОК
print(shift.s_block_decode(shift.s_block_encode("БЛОК", "ЗВЕЗДНАЯ НОЧЬ", 11), "ЗВЕЗДНАЯ НОЧЬ", 11))

print('\n[Усиленные S-блоки]')
print(shift.fwd_improve_block("АТОЛ", "ГОРАЦИО", 2))
print(shift.fwd_improve_block("АТОЛ", "ГОРАЦИО", 3))

print(shift.inv_improve_block(shift.fwd_improve_block("АТОЛ", "ГОРАЦИО", 2), "ГОРАЦИО", 2))
print(shift.inv_improve_block(shift.fwd_improve_block("АТОЛ", "ГОРАЦИО", 3), "ГОРАЦИО", 3))
