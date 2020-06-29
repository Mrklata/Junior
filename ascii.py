def str_to_dec(x):
    temp = []
    for i in x:
        temp.append(str(ord(i)))

    temp = ''.join(temp)

    return int(temp)


def test_str_to_dec():
    result = str_to_dec('asd')

    assert result == 97115100
