

def tuple_checker(a, b):

    unique_a = set(a) - set(b)
    unique_b = set(b) - set(a)

    if a == b:
        return 'tuples are equal'
    if unique_b != unique_a:
        return f'tuples are not equal and the unique values are a: {unique_a}, b: {unique_b}'
    else:
        return 'tuples are not equal but have the same values'


def test_tuple():
    same_tuples = tuple_checker((1, 2, 3), (1, 2, 3))
    same_values_tuple = tuple_checker((1, 2, 3), (3, 2, 1))
    different_tuples = tuple_checker((1, 2, 3), (2, 3, 5, 7, 5, 4))

    assert same_tuples == "tuples are equal"
    assert same_values_tuple == "tuples are not equal but have the same values"
    assert different_tuples == "tuples are not equal and the unique values are a: {1}, b: {4, 5, 7}"

