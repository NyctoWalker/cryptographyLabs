# from Tests.lab_1_tests import *
# from Tests.lab_2_tests import *
# from Tests.lab_3_tests import *

from Labs.lab_4 import *

encoder = BinaryEncryptor(" АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ")
generator = SPNet(encoder)
encryptor = Lab4Temp(generator)

print('[Базовые интерфейсы без подложки]-----------------------------------------')
# sym2bin, isSym, msg2bin
tests = [
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ',
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ0011',
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ1110011011011',
]
print(encryptor.sym2bin("А"))

print('(msg2bin)')
print("ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ: " , len(encryptor.msg2bin(tests[0])), encryptor.msg2bin(tests[0]))
print("ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ0011: " , len(encryptor.msg2bin(tests[1])), encryptor.msg2bin(tests[1]))
print("ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ1110011011011: " , len(encryptor.msg2bin(tests[2])), encryptor.msg2bin(tests[2]))

# bin2msg
tests = [
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ',
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ00111',  # Тут лишняя единичка сравнительно с прошлыми тестами, вроде все отличия
    'ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ1110011011011',
]
print('(bin2msg)')
print("ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ: " , encryptor.bin2msg(encryptor.msg2bin(tests[0])))
print("ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ00111: " , encryptor.bin2msg(encryptor.msg2bin(tests[1])))
print("ГНОЛЛЫ ПИЛИЛИ ПЫЛЕСОС ЛОСОСЕМ1110011011011: " , encryptor.bin2msg(encryptor.msg2bin(tests[2])))

print('\n[Подложка]')
# check_padding, produce_padding, pad_message, unpad_message
# Тесты могут быть неправильно определены, в лабе нет вывода INPUTS_ARRAY
inputtext = open("inp.txt").read().replace('_', ' ')
inputs_array = inputtext.split("\n")
assocdata_array = open("ad.txt").readline()
print(assocdata_array)
inputs_arraylen = []
for i in range(len(inputs_array)):
    inputs_arraylen.append(len(encryptor.msg2bin(inputs_array[i])))
print("inp.txt: ", inputs_arraylen)
tests = [
    ["ВА", "АЛИСА  А", "БОБ    А", "КОТОПОЕЗД"],
    ["ВБ", "АЛИСА АЖ", "БОБ   ОЧ", "ЕГИПТЯНИН"],
    ["В ", "АЛИСА ЯЗ", "БОБ   ЬЬ", "ЩЕГОЛЯНИЕ"],
    ["ВБ", "БОБ   ЬЬ", "АЛИСА ЯЗ", "ЭКЛАМПСИЯ"],
    ["ВБ", "БОБ   ЬЬ", "АЛИСА ЯЗ", "ЕГИПТЯНИН"],
    ["ВБ", "АЛИСА ЯЗ", "БОБ   ЬЬ", "ЕГИПТЯНИН"],
]
TST1 = encryptor.pad_message(inputs_array[0])
print("TST1 check padding: ", encryptor.check_padding(encryptor.msg2bin(TST1)))
print("TST1 unpad message: ", len(encryptor.msg2bin(encryptor.unpad_message(TST1))))
TST2 = encryptor.pad_message(inputs_array[1])
msTST2 = encryptor.msg2bin(TST2)
print("TST2 check padding: ", encryptor.check_padding(msTST2))
print("TST2 unpad message: ", len(encryptor.msg2bin(encryptor.unpad_message(TST2))))
TST3 = encryptor.pad_message(inputs_array[2])
print("TST3 check padding: ", encryptor.check_padding(encryptor.msg2bin(TST3)))
print("TST3 unpad message: ", len(encryptor.msg2bin(encryptor.unpad_message(TST3))))
TST4 = encryptor.pad_message(inputs_array[3])
print("TST4 check padding: ", encryptor.check_padding(encryptor.msg2bin(TST4)))
print("TST4 unpad message: ", len(encryptor.msg2bin(encryptor.unpad_message(TST4))))
TST41 = encryptor.pad_message(TST4)
#Тут должно быть [1, 3, 102]
print("TST41 check padding: ", encryptor.check_padding(encryptor.msg2bin(TST41)))
print("TST41 unpad message: ", len(encryptor.msg2bin(encryptor.unpad_message(TST41))))

TST6 = inputs_array[6]
print(inputs_array[6])
print(encryptor.msg2bin(TST6))
print(len(encryptor.msg2bin(TST6)))

TST61 = encryptor.pad_message(TST6)
TST62 = encryptor.msg2bin(TST61)
print(TST62)
print("TST41 check padding: ", encryptor.check_padding(TST62))
print("TST41 unpad message: ", len(encryptor.msg2bin(encryptor.unpad_message(TST61))))

print('\n[Подготовка пакетов + ксор блоков из 80 бит]')
# prepare_packet, validate_packet, transmit, receive, textor(попробовать уже сделанный ксор)

print(encryptor.getcolmatr(tests, 0))

XTST = encryptor.prepare_packet(encryptor.getcolmatr(tests, 0), "КОЛЕСО", inputs_array[0])
print(XTST[1])
print(encryptor.receive(encryptor.transmit(XTST)))

print('\n[CTR]')
# textxor

A1 = "ГОЛОВКА КРУЖИТСЯ"
A2 = "МЫШКА БЫЛА ЛИХОЙ"
B1 = "СИНЕВАТАЯ БОРОДА"
B2 = "ЗЕЛЕНЫЙ КОТОЗМИЙ"

C1 = encryptor.textor(A1, A2)
C2 = encryptor.textor(A1, B2)
print("textor["+A1+","+A2+"] = "+ C1)
print("textor["+A1+","+B2+"] = "+ C2)

C11 = encryptor.textor(C1, A1)
C12 = encryptor.textor(C1, A2)
print("textor["+C1+","+A1+"] = "+ C11)
print("textor["+C1+","+A2+"] = "+ C12)

C21 = encryptor.textor(C2, A1)
C22 = encryptor.textor(C2, A2)
print("textor["+C2+","+A1+"] = "+ C21)
print("textor["+C2+","+A2+"] = "+ C22)

print('\n[CTR]')
# enc_CTR
TST = inputs_array[0]
print("strlen TST = "+ str(len(TST)) + " /16 = " + str(len(TST)/16))
IV1 =  "АЛИСА УМЕЕТ ПЕТЬ"
IV2 =  "БОБ НЕМНОГО ПЬЯН"
IV3 =  "БОБ НЕМНОГО УНЫЛ"

keyset = generator.produce_round_keys("СЕАНСОВЫЙ КЛЮЧИК", 8)
print(keyset)
F_Test1m = encryptor.enc_CTR(TST, IV1, keyset, 6)
print("enc_CTR(IV1) = " + F_Test1m)
print("len(F_Test1m) = " + str(len(F_Test1m)))

I_Test1m = encryptor.enc_CTR(F_Test1m, IV1, keyset, 6)
print("enc_CTR(I_Test1m) = " + I_Test1m)
print("len(I_Test1m) = " + str(len(I_Test1m)))


print('\n[MAC CBC]')
# mac_CBC
keyset = generator.produce_round_keys("СЕАНСОВЫЙ КЛЮЧИК", 8)
print(keyset)
F_Test1 = encryptor.mac_CBC(TST, IV1, keyset, 6)
print("mac_CBC(IV1) = " + F_Test1)
print("len(F_Test1) = " + str(len(F_Test1)))
F_Test2 = encryptor.mac_CBC(TST, IV2, keyset, 6)
print("mac_CBC(IV1) = " + F_Test2)
print("len(F_Test2) = " + str(len(F_Test2)))
F_Test3 = encryptor.mac_CBC(TST, IV3, keyset, 6)
print("mac_CBC(IV1) = " + F_Test3)
print("len(F_Test3) = " + str(len(F_Test3)))



print('\n[CCM]')
# CCM_frw, CCM_inv
print("Проверка blockxor:")
print("КОНЬ и А  Г = " + encryptor.blockxor("КОНЬ", "А  Г"))
print("КААА и АБВГ = " + encryptor.blockxor("КААА", "АБВГ"))
print("КОНЬ и АБВГ = " + encryptor.blockxor("КОНЬ", "АБВГ"))
print("КОНЬ и ЛУНЬ = " + encryptor.blockxor("КОНЬ", "ЛУНЬ"))

IV1 =  "АЛИСА УМЕЕТ ПЕТЬ"
IV2 =  "БОБ НЕМНОГО ПЬЯН"
IV3 =  "БОБ НЕМНОГО УНЫЛ"
AD = ["ВБ", "АЛИСА АЖ","БОБ   ОЧ","ЕГИПТЯНИН","АБВГД"]
PACKET = [AD, IV2, inputs_array[0], ""]
keyset = generator.produce_round_keys("СЕАНСОВЫЙ КЛЮЧИК", 8)
print(AD)
Q_TEST1m = encryptor.CCM_frw(PACKET, keyset, 0, 8)
print("CCM_frw(PACKET) = Q_TEST1m[3] = " + Q_TEST1m[3])
print("CCM_frw(PACKET) = Q_TEST1m[2] = " + Q_TEST1m[2])

Q_TEST1inv = encryptor.CCM_inv(Q_TEST1m, keyset, 0, 8)
print("CCM_frw(Q_TEST1m) = Q_TEST1inv = " + Q_TEST1inv[3])
print("CCM_frw(Q_TEST1m) = Q_TEST1inv = " + Q_TEST1inv[2])
print()

Q_TEST0m = encryptor.CCM_frw(PACKET, keyset, 1, 8)
print("CCM_frw(PACKET) = Q_TEST0m = " + Q_TEST0m[3])
print("CCM_frw(PACKET) = Q_TEST0m = " + Q_TEST0m[2])
print()

Q_TEST0inv = encryptor.CCM_inv(Q_TEST0m, keyset, 1, 8)
print("CCM_frw(Q_TEST0m) = Q_TEST0inv = " + Q_TEST0inv[3])
print("CCM_frw(Q_TEST0m) = Q_TEST0inv = " + Q_TEST0inv[2])
print()
