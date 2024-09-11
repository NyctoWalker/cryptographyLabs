from Labs import lab_1 as shift

alphabet = {}

shift.add_alphabet(alphabet, " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")
print(alphabet)
text_as_arr = shift.text2array(alphabet, "ВСЕМ ПРИВЕТ")
print(text_as_arr)
print(shift.array2text(alphabet, text_as_arr))
print(shift.add_letters(alphabet, "Я", "Ж"))
print(shift.sub_letters(alphabet, "А", "Ж"))
