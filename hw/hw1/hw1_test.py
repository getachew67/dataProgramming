import math

import hw1


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If expected or recieved are floats,
    will do an approximate check.
    """
    # You don't need to understand how this function works
    # just look at its documentation!
    if type(expected) == 'float' or type(received) == 'float':
        match = math.isclose(expected, received)
    else:
        match = expected == received

    assert match, f'Failed: Expected {expected}, but received {received}'


def test_funky_sum():
    """
    Tests the function funky_sum
    """
    print('Testing funky_sum')

    # Notice that we have to start the function calls with "hw1." since
    # they live in another file

    # Cases from the made up "spec" for this problem
    assert_equals(1, hw1.funky_sum(1, 2, 0))
    assert_equals(2, hw1.funky_sum(1, 2, 1))
    assert_equals(1.5, hw1.funky_sum(1, 2, 0.5))
    assert_equals(1.33, hw1.funky_sum(1, 2, 0.33))

    # edge cases to test the 0 check
    assert_equals(1, hw1.funky_sum(1, 2, -1))
    assert_equals(1, hw1.funky_sum(1, 2, -0.1))
    assert_equals(1.01, hw1.funky_sum(1, 2, 0.01))

    # edge cases to test the 1 check
    assert_equals(2, hw1.funky_sum(1, 2, 2))
    assert_equals(2, hw1.funky_sum(1, 2, 2.1))
    assert_equals(1.99, hw1.funky_sum(1, 2, 0.99))


def test_count_divisible_digits():
    """
    Test the function count_divisible_digits
    """
    print('Testing count_divisible_digits')

    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 5))
    assert_equals(6, hw1.count_divisible_digits(398510, 1))
    assert_equals(3, hw1.count_divisible_digits(-203509, 2))


def test_is_relatively_prime():
    """
    Test the function is_relatively_prime
    """
    print('Testing is_relatively_prime')

    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(4, 24))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    assert_equals(True, hw1.is_relatively_prime(1, 1))
    assert_equals(False, hw1.is_relatively_prime(6, 8))


def test_travel():
    """
    Test the function travel
    """
    print('Testing travel')

    assert_equals('(-1, 4)', hw1.travel('NW!ewnW', 1, 2))
    assert_equals('(3, 4)', hw1.travel('!io', 3, 4))
    assert_equals('(3, 6)', hw1.travel('eweeNS', 1, 6))


def test_swip_swap():
    """
    Test the function swip_swap
    """
    print('Testing swip_swap')

    assert_equals('offbar', hw1.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw1.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw1.swip_swap('foobar', 'z', 'c'))
    assert_equals('aaaaa', hw1.swip_swap('iiiii', 'i', 'a'))
    assert_equals('pepepe', hw1.swip_swap('epepep', 'e', 'p'))


def test_compress():
    """
    Test the function compress
    """
    print('Testing compress')

    assert_equals('a3', hw1.compress('aaa'))
    assert_equals('', hw1.compress(''))
    assert_equals('a1b1c1d1e3f1g3', hw1.compress('abcdeeefggg'))
    assert_equals('c2o2m1p1r2e1', hw1.compress('ccoomprre'))


def test_longest_line_length():
    """
    Test the function longest_line_length
    """
    print('Testing longest_line_length')

    assert_equals(13, hw1.longest_line_length('poem.txt'))
    assert_equals(None, hw1.longest_line_length('empty.txt'))
    assert_equals(42, hw1.longest_line_length('poem2.txt'))


def test_longest_word():
    """
    Test the function longest_word
    """
    print('Testing longest_word')

    assert_equals('3: shells', hw1.longest_word('poem.txt'))
    assert_equals('19: confession', hw1.longest_word('poem2.txt'))
    assert_equals(None, hw1.longest_word('empty.txt'))


def test_mode_digit():
    """
    Test the function mode_digit
    """
    print('Testing mode_digit')

    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    assert_equals(8, hw1.mode_digit(12345678))
    assert_equals(9, hw1.mode_digit(-99943338))


def main():
    test_funky_sum()
    # Make sure you add the calls to all of your other functions here!
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_swip_swap()
    test_compress()
    test_longest_line_length()
    test_longest_word()
    test_mode_digit()


if __name__ == '__main__':
    main()
