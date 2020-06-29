def unique_lst(lst):
    copies = [set(lst)]
    for i in copies:
        lst.remove(i)

    unique = set(copies) - set(lst)
    unique = list(unique)

    return unique


def test_unique_lst():
    unique_result = unique_lst([1, 2, 3, 'elo', 'elo', 5, 6, 7, 8, 8, 8])

    assert unique_result == [1, 2, 3, 5, 6, 7]
