# Наш вариант - CTR+CBC-MAC
# 5. Провести комплексное тестирование полученного решения. Предусмотреть этап верификации (корректность реализации
# относительно указаний в приложении) и валидации (корректности функционирования с точки зрения практической задачи)
# модели протокола.
# 6. Продемонстрировать устойчивость/уязвимость протокола или его составных частей к различным атакам, в том числе,
# опирающимся на «шифрооракула». Формально-логически проанализировать алгоритм с точки зрения полученной информации,
# сделать соответствующие выводы об использованной реализации криптографического решения.

# После выполнения пункта задания, соответствующие комментарии удалить.

from Labs.lab_3 import *
import sys


class Lab4Temp:
    def __init__(self, sp_net: SPNet):
        self.sp_net = sp_net
        self.encoder = sp_net.get_encryptor()

    # region Двоичные_представления
    def sym2bin(self, s_in: str):
        if len(s_in) != 1:
            raise ValueError(f'sym2bin: получена строка с длиной {len(s_in)} вместо символа или бита')

        if s_in == '1':
            return 1
        elif s_in == '0':
            return 0
        else:
            return self.encoder.text2array(s_in)

    def is_sym(self, s_in: str):
        return s_in in self.encoder.data_alphabet

    def msg2bin(self, msg_in):
        _m = len(msg_in)
        i, f = 0, 0
        tmp = [' ']*_m*5
        while self.is_sym(msg_in[i]):
            c = self.encoder.from_byte(self.encoder.text_to_byte_string(msg_in[i]))
            for j in range(5):
                p = i*5 + 4 - j
                tmp[p] = '0' if c % 2 == 0 else '1'
                c = c // 2
            if i == _m - 1:
                f=1
                break
            else:
                i += 1
        if f == 0:
            for k in range(i, _m):
                tmp[4*i+k] = self.sym2bin(msg_in[k])
        tmp = [x for x in tmp if x != ' ']
        return tmp

    def bin2msg(self, bin_in):
        _B = len(bin_in)
        b = _B // 5
        q = _B % 5
        out = ""

        if bin_in.count('') > 0:
            p = bin_in.count('')
            k = bin_in.index('')
            print("")
        for i in range(b):
            t = 0
            for j in range(5):
                t = 2*t + int(bin_in[i*5+j])
            num = self.encoder.to_byte(t)
            out += self.encoder.get_letter_by_id(num)
        if q > 0:
            for k in range(1, q+1):
                out += str(bin_in[b*5+k-1])
        return out

    @staticmethod
    def submatrix(M, rowl, rowr, colu, cold):
        mattoreturn = []
        for i in range(rowr - rowl + 1):
            q = M[rowl + i]
            mattoreturn.append(M[rowl + i][0:cold - colu + 1])
        return mattoreturn

    @staticmethod
    def getcolmatr(M, col):
        mattoreturn = []
        for i in range(len(M)):
            mattoreturn.append(M[i][col])
        return mattoreturn
    # endregion

    # region Подложки

    def check_padding(self, bin_msg_in):
        _m = len(bin_msg_in)
        blocks_num = _m // 80
        remainder = _m % 80
        f = 0  # Так как там много выходов, которые пишут f=0, и отдельно f=1 с модификациями
        pad_length = 0  # А вот тут вообще если remainder != 0, этот параметр не задаётся
        numblocks = 0
        if remainder == 0:
            tb = self.submatrix(bin_msg_in, _m-20, _m-1, 0, 0)
            ender = self.submatrix(tb, 17, 19, 0, 0)
            if ender == ['0', '0', '1']:
                NB = self.submatrix(tb, 7, 16, 0, 0)
                PL = self.submatrix(tb, 0, 6, 0, 0)
                for i in range(7):
                    pad_length = 2*pad_length + int(PL[i])
                for i in range(10):
                    numblocks = 2*numblocks + int(NB[i])
                if numblocks == blocks_num and (103 > pad_length >= 23):
                    tb = self.submatrix(bin_msg_in, _m-pad_length, _m-21, 0, 0)
                    starter = tb[0]
                    if starter == 1:
                        f = 1
                        for j in range(1, pad_length):
                            tmp = tb[j]
                            if tmp == 1:
                                f = 0
                                break
        return [f, numblocks, pad_length]

    @staticmethod
    def produce_padding(rem_in, blocks_in):
        b = blocks_in + 1
        if rem_in == 0:
            r = 80
        elif rem_in <= 57:
            r = 80 - rem_in
        else:
            b += 1
            r = 160 - rem_in
        pad = "1"

        for i in range(1, r-20):
            pad += "0"

        rt = r
        pad = list(pad)
        pad += ['']*(r-len(pad))
        for i in range(6, -1, -1):
            l = r-20+i
            pad[r-20+i] = str(rt % 2)
            rt = rt // 2
        for i in range(9, -1, -1):
            pad[r-13+i] = str(b % 2)
            b = b // 2
        pad[r-3], pad[r-2] = "0", "0"
        pad[r-1] = "1"
        return pad

    def pad_message(self, msg_in):
        pad = ""
        bins = self.msg2bin(msg_in)
        _m = len(bins)
        blocks = _m // 80
        rem = _m % 80
        f = self.check_padding(bins)[0] if rem == 0 else 1

        if f == 1:
            pad = self.produce_padding(rem, blocks)
            for i in range(len(pad)):
                bins.append(pad[i])
        return self.bin2msg(bins)

    def unpad_message(self, msg_in):
        bins = self.msg2bin(msg_in)
        _m = len(bins)
        t = self.check_padding(bins)
        if t[0] == 1:
            filler = [0, 0, 0]
            pl = t[1]
            tmp = filler
            return self.bin2msg(tmp)
        else:  # Оно тут просто для наглядности
            return msg_in

    # endregion

    # region Пакеты

    def prepare_packet(self, data_in, iv_in, msg_in):
        # print(f'Prepare packet, вход:{data_in};{iv_in};{msg_in}.')
        iv = self.encoder.add_block(iv_in, '                ')  # 16 пробелов
        # iv = iv_in + '                '  # 16 пробелов
        # iv = '                ' + iv_in  # 16 пробелов
        msg = self.pad_message(msg_in)
        _l = len(self.msg2bin(msg))
        a = ""

        for i in range(5):
            r = self.encoder.to_byte(_l % 32)
            m = self.encoder.get_letter_by_id(r)
            a = m + a  # Не уверен, что именно за num2sym и как в concat влияет порядок
            _l //= 32
        # data[4] = a
        data_in.append(a)
        # print(f'Prepare packet: выход {data_in};{iv};{msg}')
        return [data_in, iv, msg, ""]

    @staticmethod
    def validate_packet(packet_in):
        data, iv, msg, mac = packet_in
        f = 1  # Возможно, его вообще не стоит задавать
        t = data[0][0]
        s = data[0][1]
        ml = len(mac)

        #  Можно объединить в большой if и заменить сразу return 0
        if t != "В":
            f = 0
        elif ml != 16 and (s == "А" or s == "Б"):
            f = 0
        elif ml != 0 and s == " ":
            f = 0
        return f  # Если сверху будет заменено на return 0, тут можно return 1

    def transmit(self, packet_in):
        data, iv, msg, mac = packet_in
        out = data[0] + data[1] + data[2] + data[3] + data[4]
        return self.msg2bin(out + iv + msg + mac)

    def receive(self, stream_in):
        # print(f'[Debug] receive:{stream_in}.')
        p = self.bin2msg(stream_in)
        # print(f'[Debug] p, bin2msg:{p}.')
        _m = len(p)

        _type = p[:2]
        _sender = p[2:10]
        _receiver = p[10:18]
        _session = p[18:27]
        _length = p[27:32]
        _iv = p[32:48]
        _l = 0
        for i in range(5):
            t = _length[i]
            l = self.encoder.from_byte(self.encoder.text2array(t)[0])
            # print(l)
            _l = 32*_l + l
        _l //= 5
        message = p[48:48 + _l]
        mac = p[48 + _l:_m]
        # print(f'[Debug] l,interval:{_l};{48 + _l};{_m}.')
        # print(f'[Debug] Receive, mac:{mac}.')
        return [[_type, _sender, _receiver, _session, _length], _iv, message, mac]

    def textor(self, A1, A2):
        # print(f'Textor:{A1};{A2}.')
        return self.encoder.xor_block(A1, A2)

    @staticmethod
    def combine(strset_in):
        out = ""
        for i in strset_in:
            out += i
        return out

    def blockxor(self, A_in, B_in):
        A = self.encoder.text_to_byte_string(A_in)
        B = self.encoder.text_to_byte_string(B_in)
        C = ""
        for i in range(20):
            C += str((int(A[i]) + int(B[i])) % 2)
        return self.encoder.number_to_block(self.encoder.from_byte(C))
    # endregion

    # region CCM

    def enc_CTR(self, msg_in, iv_in, key_in, r_in):
        m = len(msg_in) // 16
        iv_starter = iv_in[:12]
        iv_ender = "    "  # Предполагая что там 4 символа
        ctr = 0
        out = ""
        for i in range(m):
            iv_ender = self.encoder.number_to_block(ctr)
            iv = iv_starter + iv_ender
            keystream = self.sp_net.fwd_SPNet2(iv, key_in, r_in)
            inp = msg_in[i*16:i*16 + 16]
            out += self.textor(inp, keystream)
            ctr += 1
        return out

    def mac_CBC(self, msg_in, iv_in, key_in, r_in):
        m = len(msg_in) // 16
        ctr = 0
        out = ""
        for i in range(m):
            inp = msg_in[i*16:i*16 + 16]
            tmp = self.textor(iv_in, inp)
            iv_in = self.sp_net.fwd_SPNet2(tmp, key_in, r_in)
            out += iv_in
        return iv_in

    def CCM_frw(self, packet_in, key_in, only_mac, r_in):
        # print(f'[Debug] CCM_frw, вход:{packet_in};{only_mac}.')
        assdata_in, iv_in, msg_in, tmp = packet_in
        data = self.combine(assdata_in)
        _m = len(msg_in)
        mac = self.mac_CBC(data+msg_in, iv_in, key_in, r_in)
        if only_mac == 0:
            msg = self.enc_CTR(msg_in+mac, iv_in, key_in, r_in)
            _msg = msg[0:_m]
            _mac = msg[_m:_m + 16]
        else:
            _msg = msg_in
            _mac = mac
        # print(f'[Debug] CCM_frw, выход(mac):{[assdata_in, iv_in, _msg, _mac]}.')
        return [assdata_in, iv_in, _msg, _mac]

    def CCM_inv(self, packet_in, key_in, only_mac, r_in):
        assdata_in, iv_in, msg_in, mac_in = packet_in
        data = self.combine(assdata_in)
        _m = len(msg_in)
        # print(_m)
        if only_mac == 0:
            msg = self.enc_CTR(msg_in+mac_in, iv_in, key_in, r_in)
            _msg = msg[0:_m]
            _mac = msg[_m:_m + 16]
        else:
            _msg = msg_in
            _mac = mac_in
        mac = self.mac_CBC(data + _msg, iv_in, key_in, r_in)
        # print(f'[Debug]CCM_inv:{_mac};{mac}.')  # На CCM receive _mac нулевой
        _mac = self.textor(_mac, mac)
        return [assdata_in, iv_in, _msg, _mac]

    # Разделить send и receive на два метода
    def CCM(self, ass_data, msg_array, key_in, key_rounds, rcg_rounds, nonce, type):
        mtype, sender, receiver, transmission = ass_data
        # [RCG, rcg_rounds], [[ciph_frw, ciph_inv], cipher_rounds], [sb_frw, sb_inv], _ = cipher_suite
        t1 = receiver + sender
        t2 = mtype + transmission + '     '  # 5 пробелов(скопировал из маткада)
        t3 = self.encoder.add_block((self.encoder.add_block(t1, t2)), nonce)
        # t3 = t1 + t2 + nonce
        keyset = self.sp_net.produce_round_keys(key_in, rcg_rounds)
        out = []

        if type == 'send':
            IV0 = (t3[:8] + t3[12:16] + t3[12:16])
            out = self.CCM_send(msg_array, mtype, IV0,
                                sender, receiver, transmission,
                                keyset, key_rounds)
            # Список списков бит превращаем в список бит
            _old_out = out.copy()
            out = [element for sublist in _old_out for element in sublist]
        elif type == 'receive':
            out = self.CCM_receive(msg_array, mtype,
                                   keyset, key_rounds)
        else:
            raise ValueError('Тип сообщения не соответствует send или receive')

        return out

    def CCM_send(self, msg_array, mtype, IV0,
                 sender, receiver, transmission,
                 keyset, key_rounds):
        out = []
        msg_counter = -1
        msg_sec = mtype
        msg_counter += 1
        IV1 = ('        ' + self.encoder.number_to_block(len(msg_array)) + '    ')  # 8+4 пробелов(маткад)
        IV = self.textor(IV0, IV1)
        # print(msg_array[i])
        tmp_packet = self.prepare_packet([msg_sec, sender, receiver, transmission], IV, msg_array)
        # print('Tmp packet:', tmp_packet)
        if msg_sec == 'В ':
            out.append(self.transmit(tmp_packet))
        elif msg_sec == 'ВА':
            sec_packet = self.CCM_frw(tmp_packet, keyset, 1, key_rounds)
            out.append(self.transmit(sec_packet))
        elif msg_sec == 'ВБ':
            sec_packet = self.CCM_frw(tmp_packet, keyset, 0, key_rounds)
            out.append(self.transmit(sec_packet))
        return out

    def CCM_receive(self, msg_array, mtype, keyset, key_rounds):
        out = []
        last = -1
        # print(msg_array[i], i)
        tmp_packet = self.receive(msg_array)
        # print('Tmp packet:', tmp_packet)
        rdata = tmp_packet[0]
        x1 = tmp_packet[1][12:16]
        x2 = tmp_packet[1][8:12]
        current = self.encoder.block_to_number(self.encoder.xor_block(x1, x2))
        if current > last:
            # out.append(rec_packet)
            if rdata[0] == 'ВБ':
                rec_packet = self.CCM_inv(tmp_packet, keyset, 0, key_rounds)
                rec_packet[2] = self.unpad_message(rec_packet[2])
                if rec_packet[3] == '                ':  # 16 пробелов
                    last = current
                    rec_packet[3] = "OK"
                else:
                    print(f'Receive: вмешательство в сообщение {rec_packet}')
            elif rdata[0] == "ВА" and mtype != "ВБ":
                rec_packet = self.CCM_inv(tmp_packet, keyset, 1, key_rounds)
                rec_packet[2] = self.unpad_message(rec_packet[2])
                if rec_packet[3] == '                ':  # 16 пробелов
                    last = current
                    rec_packet[3] = "OK"
                else:
                    print(f'Receive: вмешательство в сообщение {rec_packet}')
            elif rdata[0] == "В " and mtype == "В ":
                rec_packet = tmp_packet
                rec_packet[2] = self.unpad_message(rec_packet[2])
                if rec_packet[3] == '':
                    last = current
                    rec_packet[3] = "N/A"
            else:
                rec_packet = tmp_packet
            #out.append(rec_packet[2][0])
            out = rec_packet
        # out = ''.join(out.copy())
        return out

    # endregion

    @staticmethod
    def invert(char):
        if char == '0':
            char = '1'
        elif char == '1':
            char = '0'
        else:
            raise ValueError('Invert: на вход не получено бита')
        return char
