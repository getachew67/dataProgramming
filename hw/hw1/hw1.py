def funky_sum(a, b, mix):
    """
    Returns a mixture between a and b.

    If mix is 0, returns a. If mix is 1, returns b. Otherwise returns a linear
    interpolation between them. If mix is outside the range of 0 and 1, it is
    capped at those numbers.
    """
    if mix < 0:
        return a
    elif mix > 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def count_divisible_digits(n, m):
    """
    Returns the number of digits of n that can be divided by m.

    If m is 0, returns 0. digit 0 is divisible by any number.
    """
    if m == 0:
        return 0
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        if (n % 10) % m == 0:
            count += 1
        n = n // 10
    return count


def is_relatively_prime(n, m):
    """
    Returns a boolean value if n and m are relatively prime to each other or
    not.

    If n and m are relatively prime to each other, returns True. Otherwise
    returns False. Assume n and m are at least 1.
    """
    factors_n = []
    factors_m = []
    for i in range(1, n+1):
        if n % i == 0:
            factors_n.append(i)
    for j in range(1, m+1):
        if m % j == 0:
            factors_m.append(j)
    for i in range(1, len(factors_n)):
        for j in range(1, len(factors_m)):
            if factors_n[i] == factors_m[j]:
                return False
    return True


def travel(s, x, y):
    """
    Returns a new position.

    Returns a string of new position after following directions indicated
    by the given s starting from the given x and y.
    From s, character 'N' indicates increasing the y-coordinate, 'E' indicates
    increasing the x-coordinate, 'S' indicates decreasing the y-coordinate,
    and 'W' indicates decreasing the x-coordinate (Ignore letter-casing).
    Otherwise, the character is ignored.
    """
    s = s.upper()
    for c in s:
        if c == 'N':
            y += 1
        elif c == 'E':
            x += 1
        elif c == 'S':
            y -= 1
        elif c == 'W':
            x -= 1
    return '(' + str(x) + ', ' + str(y) + ')'


def swip_swap(source, c1, c2):
    """
    Returns a swapped string

    Returns a string source with all occurrences of c1 and c2 swapped.
    Assume that the c1 and c2 are single characters.
    """
    string = []
    output = ''
    for i in range(len(source)):
        string.append(source[i])
        if string[i] == c1:
            string[i] = c2
        elif string[i] == c2:
            string[i] = c1
    for c in string:
        output += c
    return output


def compress(s):
    """
    Returns a new string that each character is followed by its count with
    any adjacent duplicate characters are removed.

    Assume the given string s only contains letters.
    """
    if s == '':
        return ''
    string = ''
    count = 1
    i = 0
    while i+1 < len(s):
        if s[i] != s[i+1]:
            string = string + s[i] + str(count)
            count = 1
            i += 1
        else:
            count += 1
            i += 1
    string = string + s[i] + str(count)
    return string


def longest_line_length(file_name):
    """
    Returns the length of the longest line in the given file.

    The length of the line is the number of characters including whitespace.
    If the file is empty, returns None.
    Assume the file exists for the given file name.
    """
    max = 0
    with open(file_name) as file:
        if len(file.read()) == 0:
            return None
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            length = len(line)
            if max < length:
                max = length
    return max


def longest_word(file_name):
    """
    Returns the longest word in the given file with the corresponding line
    number.

    If there exist ties for longest word, returns the one that appears earlier.
    If the file is empty or none of words in the file, returns None.
    Assume that the file_name exists
    """
    with open(file_name) as file:
        if len(file.read()) == 0:
            return None
    with open(file_name) as file:
        lines = file.readlines()
        length = 0
        max = length
        num = 0
        line_num = 0
        temp = ''
        for line in lines:
            num += 1
            words = line.split()
            for word in words:
                if max < len(word):
                    max = len(word)
                    if temp != word:
                        temp = word
                        line_num = num
    return str(line_num) + ': ' + temp


def mode_digit(n):
    """
    Returns the most frequently appeared digist in the given number.

    If there exist ties for the most frequent digits, returns the greater
    value.
    """
    if n < 0:
        n = -n
    elif n == 0:
        return 0
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    index = 0
    while n > 0:
        digit = n % 10
        count[digit] += 1
        n = n // 10
    max = count[0]
    for i in range(10):
        if max <= count[i]:
            max = count[i]
            index = i
    return index
