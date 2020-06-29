def build_str():
    temp = []
    for i in range(101):
        temp.append(str(i))

    str_1_100 = ''.join(temp)
    return str_1_100


def test_build_str():
    result = build_str()
    assert result == "01234567891011121314151617181920212223242526272829303132333" \
                     "435363738394041424344454647484950515253545556575859606162636" \
                     "46566676869707172737475767778798081828384858687888990919293949596979899100"