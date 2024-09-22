from Labs.lab_1 import *

# Английский алфавит без Q, Z, J, X, P - 22 символа
shift = Encryptor("ABCDEFGHIKLMNORSTUVWY ")

print('[Алфавит]')
print(shift.data_alphabet)

print('\n[Работа с алфавитом]')
text_as_arr = shift.text2array("HELLO THERE")
print(text_as_arr)
print(shift.array2text(text_as_arr))
print(shift.add_letters("B", "C"))
print(shift.sub_letters("Y", "C"))

print('\n[Цезарь]')
print(shift.caesar_encode("MIDNIGHT", "CYFER"))
print(shift.caesar_decode( shift.caesar_encode("MIDNIGHT", "CYFER"), "CYFER")) # Должно получиться MIDNIGHT
print(shift.caesar_encode("OLOLO CRINGE", "A"))
print(shift.caesar_encode( "OLOLO CRINGE", "B"))

print('\n[Смещение алфавита]')
print(shift.shift_alphabet("ABCDEFGHIKLMNORSTUVWY ", 1))
print(shift.shift_alphabet("ABCDEFGHIKLMNORSTUVWY ", -1))
print(shift.shift_alphabet("MIDNIGHT", 3))

print('\n[Виженер]')
print(shift.vidgener_encode("OLOLO CRINGE", "BANTHEON", 0))
print(shift.vidgener_decode(shift.vidgener_encode("OLOLO CRINGE", "BANTHEON", 1), "BANTHEON", 1)) # Должно получиться OLOLO CRINGE

print('\n[S-блоки]')
print(shift.s_block_encode("FOU", "STARRY NIGHT", 11)) # Ошибка
print(shift.s_block_encode("FOUR", "STARRY NIGHT", 11))
# Должно получиться FOUR
print(shift.s_block_decode(shift.s_block_encode("FOUR", "STARRY NIGHT", 11), "STARRY NIGHT", 11))

print('\n[Усиленные S-блоки]')
print(shift.fwd_improve_block("ATOL", "GORATIO", 2))
print(shift.fwd_improve_block("ATOL", "GORATIO", 3))

print(shift.inv_improve_block(shift.fwd_improve_block("ATOL", "GORATIO", 2), "GORATIO", 2))
print(shift.inv_improve_block(shift.fwd_improve_block("ATOL", "GORATIO", 3), "GORATIO", 3))
