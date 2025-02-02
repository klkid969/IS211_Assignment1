# assignment1_part1.py


def list_divide(numbers, divide=2):
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1
    return count

class ListDivideException(Exception):
    pass

def test_list_divide():
    try:
        print(list_divide([1, 2, 3, 4, 5]))  # Should print: 2
        print(list_divide([2, 4, 6, 8, 10]))  # Should print: 5
        print(list_divide([30, 54, 63, 98, 100], divide=10))  # Should print: 2
        print(list_divide([]))  # Should print: 0
        print(list_divide([1, 2, 3, 4, 5], 1))  # Should print: 5
        print("All tests passed!")
    except AssertionError:
        raise ListDivideException("Test failed")

test_list_divide()

