from Labs.lab_3 import *
import random

alphabet_string = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ"
encoder = BinaryEncryptor(alphabet_string)
lab = SPNet(encoder)


def main():
    # methods_testing()
    # keys_statistical_testing(p_block_rounds = 1)
    # __in = '                '
    keys_period_testing(num_rounds = 500, p_block_rounds = 1, __in = '                ')
    pass


# region SymbolCount
def count_symbols(s: str):
    counts = {}
    overall = 0
    for char in s:
        counts[char] = counts[char]+1 if char in counts else 1
        overall += 1
    return [[char, count] for char, count in sorted(counts.items(), key=lambda item: item[1], reverse=True)], overall


def print_string_results(s: str):
    result, overall_count = count_symbols(s)
    print(f"Информация о символах строки '{s}'")
    for symbol, count in result:
        print(f"{symbol} {count} {count / overall_count * 100:.1f}%")
    print(f"Всего символов: {overall_count}\n")


def print_tuple_results(s: count_symbols(s='')):
    result, overall_count = s
    print(f"Информация о символах кортежа '{s}'")
    for symbol, count in result:
        print(f"{symbol} {count} {count / overall_count * 100:.1f}%")
    print(f"Всего символов: {overall_count}\n")


def modify_and_count(s1: count_symbols(s=''), s2: str):
    res, overall = s1
    res = dict(res)
    for char in s2:
        res[char] = res[char]+1 if char in res else 1
        overall += 1
    return [[char, count] for char, count in sorted(res.items(), key = lambda item: item[1], reverse = True)], overall


def generate_random_input(rnd_seed: int = 42):
    random.seed = rnd_seed
    out = ""
    for i in range(16):
        out += alphabet_string[random.randint(0, 31)]
    return out
# endregion


# region Testing
def methods_testing():
    s = "ABBC"
    s_modified = "AACC1"
    print('--------------------[Подсчёт единых строк]--------------------')
    print_string_results(s)
    print_string_results('')
    print(count_symbols(''))

    print('\n--------------------[Проверка работы с кортежами]--------------------')
    print_tuple_results(count_symbols(s_modified))
    print_string_results(s + s_modified)
    print(count_symbols(s + s_modified))
    print(count_symbols(s + s_modified)[0], '\n', count_symbols(s + s_modified)[1])

    print('\n--------------------[Модификация строк]--------------------')
    s_tuple = count_symbols(s)
    print(modify_and_count(s_tuple, s_modified))
    print_tuple_results(modify_and_count(s_tuple, s_modified))


def keys_statistical_testing(p_block_rounds: int = 0):
    """
    Тесты для проверки равноценности символов при изменении единого символа ключа или входа
    Изменяет последний, 16-й символ пустого ключа последовательно на каждый символ алфавита

    :param p_block_rounds: Количество раундов для p-блоков
    """
    _in = "                "  # 16 символов
    _key = "               "  # 15 символов
    s = count_symbols('')

    print(f'''Алфавит: "{alphabet_string}"''')
    print(f'''Вход: "{_in}"''')

    for _l in alphabet_string:
        _k = _key + _l
        s_out = lab.fwd_SPNet(_in, _k, p_block_rounds)
        s = modify_and_count(s, s_out)
    print_tuple_results(s)


def keys_period_testing(num_rounds: int = 10,
                        p_block_rounds: int = 0,
                        __in: str = 'rnd'):
    """
    Тесты для большого количества последовательно применяемых ключей

    :param num_rounds: Количество репликаций
    :param p_block_rounds: Количество раундов p-блоков
    :param __in: Входная строка, принимает строки из 16 символов или генерирует случайную при значении 'rnd'
    :return:
    """
    _in = generate_random_input() if __in == 'rnd' else __in
    _key = "                "  # 16 символов
    out = lab.fwd_SPNet(_in, _key, p_block_rounds)
    s = count_symbols(out)

    print(f'''Алфавит: "{alphabet_string}"''')
    print(f'''Вход: "{_in}"''')

    for i in range(num_rounds):
        out = lab.fwd_SPNet(out, _key, p_block_rounds)
        s = modify_and_count(s, out)
    print_tuple_results(s)
# endregion


if __name__ == '__main__':
    main()
