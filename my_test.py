import pytest as pytest


def int_multiplication(val_1, val_2):
    return val_1 * val_2


def get_val_by_index(list_with_val, index):
    return list_with_val[index]


def add_val_to_set(my_set, my_val):
    my_set.add(my_val)
    return my_set


@pytest.mark.parametrize(
    "val_1, val_2, expected",
    [(1, 2, 2),
     (-1, 2, -2),
     (-1, -2, 2),
     (0, 0, 0)])
def test_positive_int_multiplication(val_1, val_2, expected):
    assert int_multiplication(val_1, val_2) == expected


@pytest.mark.parametrize("val_1, val_2, expected",
                         [pytest.param(1, 1.0001, 1, marks=pytest.mark.xfail(
                          reason="Negative test. Result is 1.0001, expected = 1"))])
def test_negative_int_multiplication(val_1, val_2, expected):
    assert int_multiplication(val_1, val_2) == expected


@pytest.mark.parametrize("list_with_val, index, expected",
                         [(["one", "two", "three"], 0, "one"),
                          (["one", "two", "three"], 2, "three"),
                          (["one", "two", "three"], -1, "three"),
                          (["one", "two", "three"], 1, "two")])
def test_positive_get_val_by_index(list_with_val, index, expected):
    assert get_val_by_index(list_with_val, index) == expected


def test_negative_get_val_by_index(list_with_val=["one", "two", "three"], index=3):
    try:
        assert get_val_by_index(list_with_val, index)
    except IndexError:
        pass


@pytest.mark.parametrize(
    "my_set, my_val, expected",
    [(set(), "", 1),
     (set(), None, 1),
     (set(), False, 1),
     (set(), 1, 1),
     (set(), (1, 2), 1),
     (set(), "one", 1),
     ({"1"}, "1", 1),
     ({1, 2}, "3", 3)])
def test_positive_expected_set_len(my_set, my_val, expected):
    assert len(add_val_to_set(my_set, my_val)) == expected


@pytest.mark.parametrize("my_set, my_val, expected",
                         [pytest.param(set("two"), "two", 2, marks=pytest.mark.xfail(
                          reason="Negative test. len(set('two') == 4, expected = 2"))])
def test_negative_expected_set_len(my_set, my_val, expected):
    assert len(add_val_to_set(my_set, my_val)) == expected


