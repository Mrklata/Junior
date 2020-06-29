def binary(x):
    temp = x.replace(' ', '')[::-1]
    result = 0
    for i in range(len(temp)):
        if temp[i] == "1":
            result += 2 ** i
    return result


def test_binary():
    result = binary("1001 1100 0101")
    result_nos_spaces = binary('10001000')
    assert result_nos_spaces
    assert type(result) == int and type(result_nos_spaces) == int
    assert result == 2501
    assert result_nos_spaces == 136
