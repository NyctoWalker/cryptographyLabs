from Labs import lab_1 as shift

alphabet = {}

shift.add_alphabet(alphabet, " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")

print('[Проверки]')
print(shift.caesar_encode(alphabet, "ПОЛДЕНЬ", "О")) # Должно получиться ТСОЗИРЯ
