from main import func


def test_func():
    assert func(1, 2, 3) == 27
    assert func(2, 2, 2) == 16
    assert func(3, 2, 4) == 625


if __name__ == "__main_file__":
    test_func()
