from Labs.lab_3 import *

alphabet_string = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ"
encoder = BinaryEncryptor(alphabet_string)
lab = SPNet(encoder)


def main():
    # methods_testing()
    # keys_statistical_testing()
    # keys_period_testing(num_rounds = 1000)
    pass


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


def keys_statistical_testing():
    """
    Тесты для проверки равноценности символов при изменении единого символа ключа или входа
    """
    _in = "                "
    _key = "               "  # Ключ из 15 символов
    s = count_symbols('')
    for l in alphabet_string:
        _k = _key + l
        s_out = lab.fwd_SP_round(_in, _k, 0)
        s = modify_and_count(s, s_out)
    print_tuple_results(s)


def keys_period_testing(num_rounds: int = 10):
    """
    Тесты для большого количества последовательно применяемых ключей
    """
    _in = "КОРЫСТЬ СЛОНА ЭХ"
    _key = "МТВ ВСЕ ЕЩЕ ТЛЕН"
    out = lab.fwd_SP_round(_in, _key, 0)
    s = count_symbols(out)
    for i in range(num_rounds):
        out = lab.fwd_SP_round(out, _key, 0)
        s = modify_and_count(s, out)
    print_tuple_results(s)



if __name__ == '__main__':
    main()
