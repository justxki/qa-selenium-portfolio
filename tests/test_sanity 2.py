import pytest

cases = [
    (10, 5, 2, None),
    (10, 0, None, ZeroDivisionError),
    (20, 4, 5, None),
    (0, 10, 0, None),
    (10, "5", None, TypeError),
    (10, 5.7, 1.7543859649, None),
    (10, True, 10.0, None),
    (10, False, None, ZeroDivisionError),
    (10, [], None, TypeError),
]

@pytest.mark.parametrize("a, b, expected_result, expected_error", cases)
def test_divide_all_cases(a, b, expected_result, expected_error):
    if expected_error == None:
        assert a / b == pytest.approx(expected_result)
    else:
        with pytest.raises(expected_error):
            a / b


def test_undefined_variable_raises():
    with pytest.raises(NameError) as e:
        undefined_variable

    assert "undefined_variable" in str(e.value)