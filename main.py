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
print(shift.sub_letters("Е", "Ж"))

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
print('(374003):')
print(shift.to_byte(374003))
print(shift.from_byte('01011011010011110011'))

print("\n[Цезарь]")
print(shift.oneside_caesar('КРУТ', 'РОЗА', 6))
print(shift.s_block_encode('БЛОК', 'ЗВЕЗДНАЯ НОЧЬ', 11))
print(shift.fwd_improve_block('АТОЛ', 'ГОРАЦИО', 2)) #ЬООЫ
print(shift.s_block_encode_modified('КРУТ', 'РОЗА', 0)) #ДРМИ

print("\n[LCG coefs]")
print(shift.make_coef([8677, 739], [11, 89], 20))
print(shift.make_coef([7927, 151], [3, 113], 20))

print(shift.count_bits(1231))
print(shift.count_bits(723482))

print(shift.compose_num(723482, 1231, 10))

print("\n[LCG]")
LCG_set = [723482, 8677, 983609]
out1 = []
out1txt = []
out1.append(shift.LCG_Next(shift.block_to_number("ЛУЛУ"), [723482, 8677, 983609]))
out1txt.append(shift.number_to_block(out1[0]))
print(out1[0])
for i in range(1, 10):
    out1.append(shift.LCG_Next(out1[i-1], [723482, 8677, 983609]))
    out1txt.append(shift.number_to_block(out1[i]))
print(out1txt)


print("\n[LCG-SEED]")
seed1 = ["АПЧХ","Ч ОК","ШУРА"]
seed2 = shift.make_seed("КОЛА")
print("SEED2:")
print(seed2)
s1 = shift.seed_to_numbers(seed1)
s2 = shift.seed_to_numbers(seed2)
print(s1, s2)
set = [[723482, 8677, 983609],[252564, 9109, 961193],[357630, 8971, 948209]]
#seed1
out1 = []
t_out = []
out1.append(shift.HCLGG(s1, set))
t_out.append(shift.number_to_block(out1[0][0]))
for i in range(1, 10):
    out1.append(shift.HCLGG(out1[i-1][1], set))
    t_out.append(shift.number_to_block(out1[i][0]))
print("S1")
print(t_out)
#seed2
out2 = []
t_out2 = []
out2.append(shift.HCLGG(s2, set))
t_out2.append(shift.number_to_block(out2[0][0]))
for i in range(1, 10):
    out2.append(shift.HCLGG(out2[i-1][1], set))
    t_out2.append(shift.number_to_block(out2[i][0]))
print("S2")
print(t_out2)


print("\n[LCG-ЦЕЗАРЬ]")

outceas = []
intern = []
a, b = shift.wrap_CHCLCG_next("up", -1, seed1, set) # О КАКОМ SEED ИДЕТ РЕЧЬ, ЧТО ЭТО
outceas.append(a)
intern.append(b)
for i in range(1, 9):
    a, b = shift.wrap_CHCLCG_next("down", intern[i-1], -1, set)
    outceas.append(a)
    intern.append(b)
print(outceas)
print(intern)