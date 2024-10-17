from Labs.lab_3 import *

encoder = BinaryEncryptor(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")
lab = SPNet(encoder)

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
in_bl = 'АБВГДЕЖЗИЙКЛМНОП'
MS1, MS2, MS3 = lab.get_magic_square(1), lab.get_magic_square(2), lab.get_magic_square(3)
print('---MS1:')
print("FWD: ", lab.fwd_MS(in_bl, MS1))
print("INV: ", lab.inv_MS(lab.fwd_MS(in_bl, MS1), MS1))
print('\n---MS2:')
print("FWD: ", lab.fwd_MS(in_bl, MS2))
print("INV: ", lab.inv_MS(lab.fwd_MS(in_bl, MS2), MS2))
print('\n---MS3:')
print("FWD: ", lab.fwd_MS(in_bl, MS3))
print("INV: ", lab.inv_MS(lab.fwd_MS(in_bl, MS3), MS3))

print('\n[Двоичные представления]')
_in = "ЗОЛОТАЯ СЕРЕДИНА"
print(encoder.text_to_byte_string(_in), len(encoder.text_to_byte_string(_in)))
print(encoder.byte_string_to_text(encoder.text_to_byte_string(_in)))
TST = encoder.LB2B("ЗОЛОТАЯ СЕРЕДИНА")
print(TST)
print(encoder.BL2B(TST))

print('\n[Binary-Shift]')
IN1 = encoder.to_true_byte(encoder.block_to_number("ГОЛД"))
IN2 = encoder.to_true_byte(encoder.block_to_number("ЯРУС"))
out1 = encoder.bin_shift(IN1, 1)
lout1 = encoder.bin_shift(out1, -1)
out2 = encoder.bin_shift(IN2, 1)
lout2 = encoder.bin_shift(out2, -1)
print(IN1, " --- ", "ГОЛД")
print(out1, " --- ", encoder.number_to_block(encoder.from_byte(out1)))
print(lout1, " --- ", encoder.number_to_block(encoder.from_byte(lout1)))
print(IN2, " --- ", "ЯРУС")
print(out2, " --- ", encoder.number_to_block(encoder.from_byte(out2)))
print(lout2, " --- ", encoder.number_to_block(encoder.from_byte(lout2)))

print('\n[Прямой и обратный P-блок]')
PS = "ЗОЛОТАЯ СЕРЕДИНА"
PS2 = 'АБВГДЕЖЗИЙКЛМНОП'
print(lab.fwd_P_round(PS, 1), " --- ", lab.inv_P_round(lab.fwd_P_round(PS, 1), 1))
print(lab.fwd_P_round(PS, 2), " --- ", lab.inv_P_round(lab.fwd_P_round(PS, 2), 2))
print(lab.fwd_P_round(PS, 4), " --- ", lab.inv_P_round(lab.fwd_P_round(PS, 4), 4))

print(lab.fwd_P_round(PS2, 1), " --- ", lab.inv_P_round(lab.fwd_P_round(PS2, 1), 1))
print(lab.fwd_P_round(PS2, 2), " --- ", lab.inv_P_round(lab.fwd_P_round(PS2, 2), 2))
print(lab.fwd_P_round(PS2, 4), " --- ", lab.inv_P_round(lab.fwd_P_round(PS2, 4), 4))

print('\n[Прямая и обратная SP-сеть]')
in1 = "КОРЫСТЬ СЛОНА ЭХ"
in2 = "КОРЫСТЬ СЛОН  ЭХ"
key = "МТВ ВСЕ ЕЩЕ ТЛЕН"
out1c = lab.fwd_SP_round(in1, key, 0)
out2c = lab.fwd_SP_round(in2, key, 0)
lout1c = lab.inv_SP_round(out1c, key, 0)
lout2c = lab.inv_SP_round(out2c, key, 0)

print(out1c, " --- ", lout1c)
print(out2c, " --- ", lout2c)

print('\n[Изменения с последовательно применямыми ключами]')
in1 = "КОРЫСТЬ СЛОНА ЭХ"
in2 = "КОРЫСТЬ СЛОН  ЭХ"
in3 = "КОРЫСТЬ СЛННА ЭХ"
in4 = "КОРЫСТЬ СЛНН  ЭХ"
key = "МТВ ВСЕ ЕЩЕ ТЛЕН"

out1c, out2c, out3c, out4c = [], [], [], []
lout1c, lout2c, lout3c, lout4c = [], [], [], []

out1c.append(lab.fwd_SP_round(in1, key, 0))
out2c.append(lab.fwd_SP_round(in2, key, 0))
out3c.append(lab.fwd_SP_round(in3, key, 0))
out4c.append(lab.fwd_SP_round(in4, key, 0))

lout1c.append(lab.inv_SP_round(out1c[0], key, 0))
lout2c.append(lab.inv_SP_round(out2c[0], key, 0))
lout3c.append(lab.inv_SP_round(out3c[0], key, 0))
lout4c.append(lab.inv_SP_round(out4c[0], key, 0))

for i in range(1, 8):
    out1c.append(lab.fwd_SP_round(out1c[i-1], key, i))
    out2c.append(lab.fwd_SP_round(out2c[i-1], key, i))
    out3c.append(lab.fwd_SP_round(out3c[i-1], key, i))
    out4c.append(lab.fwd_SP_round(out4c[i-1], key, i))
    lout1c.append(lab.inv_SP_round(out1c[i], key, i))
    lout2c.append(lab.inv_SP_round(out2c[i], key, i))
    lout3c.append(lab.inv_SP_round(out3c[i], key, i))
    lout4c.append(lab.inv_SP_round(out4c[i], key, i))

print("out1 = ", " --- ", out1c)
print("out2 = ", " --- ", out2c)
print("out3 = ", " --- ", out3c)
print("out4 = ", " --- ", out4c)

print("lout1 = ", " --- ", lout1c)
print("lout2 = ", " --- ", lout2c)
print("lout3 = ", " --- ", lout3c)
print("lout4 = ", " --- ", lout4c)

print('\n[SPNet]')
in1 = "КОРЫСТЬ СЛОНА ЭХ"
in2 = "ЛЕРА КЛОНКА КОНЯ"
key = "МТВ ВСЕ ЕЩЕ ТЛЕН"
out1cf = lab.fwd_SPNet(in1, key, 8)
print(out1cf, " --- ", lab.inv_SPNet(out1cf, key, 8))
out2cf = lab.fwd_SPNet(in2, key, 8)
print(out2cf, " --- ", lab.inv_SPNet(out2cf, key, 8))
print(lab.produce_round_keys(key, 8))

in1 = "АААААААААААААААА"
in2 = "ААААААААААААААА "
key1 = "АААААААААААААААА"
key2 = "                "
out11cf = lab.fwd_SPNet(in1, key1, 8)
print(out11cf, " --- ", lab.inv_SPNet(out11cf, key1, 8))
out21cf = lab.fwd_SPNet(in2, key1, 8)
print(out21cf, " --- ", lab.inv_SPNet(out21cf, key1, 8))
out21cf = lab.fwd_SPNet(in1, key2, 8)
print(out21cf, " --- ", lab.inv_SPNet(out21cf, key2, 8))
out22cf = lab.fwd_SPNet(in2, key2, 8)
print(out22cf, " --- ", lab.inv_SPNet(out22cf, key2, 8))

