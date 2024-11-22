from Labs.lab_2 import *

# 5. Составить набор тестов и протестировать диффузию и запутанность. Сделать небольшие выводы.


class SPNet:

    def __init__(self, encryptor: BinaryEncryptor):
        self.encryptor = encryptor

    def get_encryptor(self):
        return self.encryptor

    @staticmethod
    def make_lcg_set():
        return [[723482, 8677, 983609], [252564, 9109, 961193], [357630, 8971, 948209]]

    def produce_round_keys(self, key_in, num_in):
        _iter, tmp, out = [], [], []
        set = self.make_lcg_set()

        tmp = self.encryptor.wrap_CHCLCGM_next('up', -1, key_in, set)
        out.append(tmp[0])
        if num_in > 1:
            for i in range(1, num_in):
                tmp = self.encryptor.wrap_CHCLCGM_next('down', tmp[1], -1, set)
                out.append(tmp[0])
        return out

    @staticmethod
    def get_magic_square(num: int):
        match num:
            case 1:
                return ([16, 3, 2, 13],
                        [5, 10, 11, 8],
                        [9, 6, 7, 12],
                        [4, 15, 14, 1])
            case 2:
                return ([7, 14, 4, 9],
                        [12, 1, 15, 6],
                        [13, 8, 10, 3],
                        [2, 11, 5, 16])
            case _:
                return ([4, 14, 15, 1],
                        [9, 7, 6, 12],
                        [5, 11, 10, 8],
                        [16, 2, 3, 13])

    @staticmethod
    def frw_magic_square(block_in: str, msqr_in: get_magic_square(num=-1)):
        if len(block_in) != 16:
            raise ValueError('Длина блока текста должна равняться 16 символам')
        out = ""
        for i in range(4):
            for j in range(4):
                out += block_in[msqr_in[i][j] - 1]
        return out

    @staticmethod
    def inv_magic_square(block_in: str, msqr_in: get_magic_square(num=-1)):
        if len(block_in) != 16:
            raise ValueError('Длина блока текста должна равняться 16 символам')
        tmp: list = [" "]*16
        d = list(block_in)
        for i in range(4):
            for j in range(4):
                tmp[msqr_in[i][j] - 1] = d[4*i+j]
        return ''.join(tmp)

    def fwd_MS(self, block, matrix):
        d = block
        m = matrix
        out = ""
        for i in range(4):
            for j in range(4):
                out = out + d[m[i][j]-1]
        return out

    def inv_MS(self, block, matrix):
        d = self.encryptor.text2array(block)
        m = matrix
        tmp = [0]*16
        for i in range(4):
            for j in range(4):
                tmp[m[i][j] - 1] = d[4*i+j]
        return self.encryptor.array2text(tmp)

    def fwd_P_round(self, block, r_in):
        M = [
             self.get_magic_square(1),
             self.get_magic_square(2),
             self.get_magic_square(3)
            ]
        r = r_in % 3
        j = 4*(r_in % 4)+2
        tmp = self.fwd_MS(block, M[r])
        T = self.encryptor.bin_shift(self.encryptor.LB2B(tmp), j)
        return self.encryptor.BL2B(T)

    def inv_P_round(self, block, r_in):
        M = [
             self.get_magic_square(1),
             self.get_magic_square(2),
             self.get_magic_square(3)
            ]
        r = r_in % 3
        j = -(4*(r_in % 4)+2)
        T = self.encryptor.bin_shift(self.encryptor.LB2B(block), j)
        return self.inv_MS(self.encryptor.BL2B(T), M[r])

    def fwd_SP_round(self, block, key, r):
        inter = ""
        for i in range(4):
            T = block[i*4:i*4+4]
            inter = inter + self.encryptor.s_block_encode_modified(T, key, i*4)
        tmp = self.fwd_P_round(inter, r)
        return self.encryptor.xor_block(tmp, key)

    def inv_SP_round(self, block, key, r):
        out = ""
        tmp = self.encryptor.xor_block(block, key)
        inter = self.inv_P_round(tmp, r)
        for i in range(4):
            T = inter[i*4:i*4+4]
            out = out + self.encryptor.s_block_decode_modified(T, key, i*4)
        return out

    def fwd_SPNet(self, block, key, r):
        key_set = self.produce_round_keys(key, r)
        block = block
        for i in range(r):
            block = self.fwd_SP_round(block, key_set[i], i)
        return block

    def inv_SPNet(self, block, key, r):
        key_set = self.produce_round_keys(key, r)
        block = block
        for i in range(r-1, -1, -1):
            block = self.inv_SP_round(block, key_set[i], i)
        return block

    def fwd_SPNet2(self, block, key_set, r):
        block = block
        for i in range(r):
            block = self.fwd_SP_round(block, key_set[i], i)
        return block

    def inv_SPNet2(self, block, key_set, r):
        block = block
        for i in range(r-1, -1, -1):
            block = self.inv_SP_round(block, key_set[i], i)
        return block





