def primes_generator(n):
    primes = [2]
    x = 3
    while x <= n:
        if all(x % prime for prime in primes):
            primes.append(x)
        else:
            x += 1
    return primes


def test_primes_generator():
    result = primes_generator(1000)
    ten_primes = primes_generator(10)
    bol_result = True
    for i in result:
        if all(i % prime for prime in result):
            bol_result = False
    assert len(ten_primes) == 4
    assert ten_primes == [2, 3, 5, 7]
    assert len(result) == 168
    assert bol_result
