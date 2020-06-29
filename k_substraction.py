def unique_pairs(k, lst):
    pairs = []

    lst.sort()

    elem1 = 0
    elem2 = 0

    while elem2 < len(lst):
        if lst[elem2] - lst[elem1] == k:
            pairs.append([lst[elem2], lst[elem1]])
            elem1 += 1
            elem2 += 1

        elif lst[elem2] - lst[elem1] > k:
            elem1 += 1
        else:
            elem2 += 1
    return pairs


print(unique_pairs(2, [4, 2, 3, 1, 5]))


def test_unique_pair():
    result = unique_pairs(2, [4, 2, 3, 1, 5])
    assert result == [[3, 1], [4, 2], [5, 3]]
