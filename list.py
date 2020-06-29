def remove_empty_str(x):
    x_no_empty_str = list(filter(lambda a: a != '', x))
    return x_no_empty_str


def test_remove_empty_str():
    result = remove_empty_str(["", "", "ew", "22", 32, "", "elo"])
    assert result == ["ew", "22", 32, "elo"]
