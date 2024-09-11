from Labs import lab_1 as shift

alphabet = {}

shift.add_alphabet(alphabet, " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")
print(alphabet)

text_as_arr = shift.text2array(alphabet, "ВСЕМ ПРИВЕТ")
print(text_as_arr)
print(shift.array2text(alphabet, text_as_arr))
print(shift.add_letters(alphabet, "Я", "Ж"))
print(shift.sub_letters(alphabet, "А", "Ж"))

print(shift.caesar_encode(alphabet, "ПОЛДЕНЬ", "ВЕРСАЛЬ")) # Должно получиться ТСОЗИРЯ
print(shift.caesar_decode(alphabet, shift.caesar_encode(alphabet, "ПОЛДЕНЬ", "ВЕРСАЛЬ"), "ВЕРСАЛЬ")) # Должно получиться ПОЛДЕНЬ
print(shift.caesar_encode(alphabet, "СЫЗРАНЬ", "А")) # Должно получиться ТЬИСБОЭ

print(shift.shift_alphabet(alphabet, " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ", 1))
print(shift.shift_alphabet(alphabet, " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ", -1))
print(shift.shift_alphabet(alphabet, "ПОЛДЕНЬ", 3)) # Должно получиться ТСОЗИРЯ
