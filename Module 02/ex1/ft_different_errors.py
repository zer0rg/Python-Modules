def test_value_error():
    try:
        print("Testing ValueError...")
        int("not_a_number")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")


def test_zero_division_error():
    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")


def test_file_not_found_error():
    """Test FileNotFoundError handling"""
        print("Testing FileNotFoundError...")
        f = open("missing.txt", "r")
        f.read()
        f.close()
    except FileNotFoundError:
        f.close()
        print("Caught FileNotFoundError: No such file 'missing.txt'")


def test_key_error():
    """Test KeyError handling"""
        print("Testing KeyError...")
        garden = {"roses": 5, "tulips": 3}
        garden["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")


def test_multiple_errors():
    """Test handling multiple error types"""
    
    test_cases = [
        lambda: int("invalid"),
        lambda: 10 / 0,
        lambda: [1, 2][10],
    ]

    for test in test_cases:
        try:
            test()
        except (ValueError, ZeroDivisionError, IndexError):
            print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_value_error()
    test_zero_division_error()
    test_file_not_found_error()
    test_key_error()
    test_multiple_errors()
    print("\nAll error types tested successfully!")
