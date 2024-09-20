from Labs import lab_1 as shift

alphabet = {}

print('[Алфавит]')
shift.add_alphabet(alphabet, " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")
print(alphabet)

print('\n[Работа с алфавитом]')
text_as_arr = shift.text2array(alphabet, "ВСЕМ ПРИВЕТ")
print(text_as_arr)
print(shift.array2text(alphabet, text_as_arr))
print(shift.add_letters(alphabet, "Я", "Ж"))
print(shift.sub_letters(alphabet, "Е", "Ж"))

print('\n[Цезарь]')
print(shift.caesar_encode(alphabet, "ПОЛДЕНЬ", "ВЕРСАЛЬ")) # Должно получиться ТСОЗИРЯ
print(shift.caesar_decode(alphabet, shift.caesar_encode(alphabet, "ПОЛДЕНЬ", "ВЕРСАЛЬ"), "ВЕРСАЛЬ")) # Должно получиться ПОЛДЕНЬ
print(shift.caesar_encode(alphabet, "СЫЗРАНЬ", "А")) # Должно получиться ТЬИСБОЭ
print(shift.caesar_encode(alphabet, "ОЛОЛО КРИНЖ", "Х")) # Должно получиться ДБДБДХАЖЯГЭ

print('\n[Смещение алфавита]')
print(shift.shift_alphabet(alphabet, " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ", 1))
print(shift.shift_alphabet(alphabet, " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ", -1))
print(shift.shift_alphabet(alphabet, "ПОЛДЕНЬ", 3)) # Должно получиться ТСОЗИРЯ

print('\n[Виженер]')
print(shift.vidgener_encode("ОЛОЛО КРИНЖ", "ПАНТЕОН", alphabet, 0)) # Должно получиться ЯЭНЮЖЖ ХОБН
print(shift.vidgener_decode(shift.vidgener_encode("ОЛОЛО КРИНЖ", "ПАНТЕОН", alphabet, 1), "ПАНТЕОН", alphabet, 1)) # Должно получиться ОЛОЛО КРИНЖ

print('\n[S-блоки]')
print(shift.s_block_encode(alphabet, "БЛО", "ЗВЕЗДНАЯ НОЧЬ", 11)) # Ошибка
print(shift.s_block_encode(alphabet, "БЛОК", "ЗВЕЗДНАЯ НОЧЬ", 11)) # Должно получиться Щ КЙ
# Должно получиться БЛОК
print(shift.s_block_decode(alphabet, shift.s_block_encode(alphabet, "БЛОК", "ЗВЕЗДНАЯ НОЧЬ", 11), "ЗВЕЗДНАЯ НОЧЬ", 11))

print('\n[Усиленные S-блоки]')
print(shift.fwd_improve_block(alphabet, "АТОЛ", "ГОРАЦИО", 2))
print(shift.fwd_improve_block(alphabet, "АТОЛ", "ГОРАЦИО", 3))

print(shift.inv_improve_block(alphabet, shift.fwd_improve_block(alphabet, "АТОЛ", "ГОРАЦИО", 2), "ГОРАЦИО", 2))
print(shift.inv_improve_block(alphabet, shift.fwd_improve_block(alphabet, "АТОЛ", "ГОРАЦИО", 3), "ГОРАЦИО", 3))
