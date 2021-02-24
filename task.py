# CS 362-400 Group 53

# Function 1 Author: Christine Pham
def conv_num(num_str):
    """function that takes a string of numbers and converts it to int/float.
    conv_num processes the string and calls the appropriate converting func."""
    negSign, charPos, perCount = 1, -1, 0

    # check if parameter is a string
    if not isinstance(num_str, str):
        return None

    # check if a value is being passed
    if len(num_str) == 0:
        return None

    # check for negative sign & remove
    if num_str == '-':
        return None
    elif num_str[0] == '-':
        negSign = -1
        num_str = num_str[1:]

    # if number is a hexadecimal, strip '0x' and process
    if num_str[:2] == '0x':
        num_str = num_str[2:]

        num_str = conv_hex(num_str)
        if not num_str:
            return None

        return num_str * negSign

    # count num of periods in string. if 2+ periods rtn None
    valid_digits = '0987654321.'
    for i, ch in enumerate(num_str):
        if ch == '.':
            perCount += 1
            charPos = i
        if perCount > 1 or ch not in valid_digits:
            return None

    num_str = process_intfloat(num_str, perCount, charPos)

    return num_str * negSign


def process_intfloat(num_str, percount, charpos):
    """strips string of decimals and sends to correct converting function"""
    # sort thru decimal num placed at start/end of string
    if percount == 1 and num_str[0] == '.':
        num_str = num_str[1:]
        num_str = conv_frac(num_str)
    elif percount == 1 and num_str[-1] == '.':
        num_str = num_str[:-1]
        num_str = conv_whole(num_str) + 0.0

    # split str at decimal point position if nums on both sides of decimal pt
    elif percount == 1:
        wholeNum = num_str[:charpos]
        fracNum = num_str[charpos + 1:]
        wholeNum = conv_whole(wholeNum)
        fracNum = conv_frac(fracNum)
        num_str = wholeNum + fracNum + 0.0

    # if string passed is not float, don't convert to float
    elif percount == 0:
        num_str = conv_whole(num_str)

    return num_str


def conv_whole(num):
    """converts whole number portion of passed string num. returns an int"""
    place, converted = 1, 0
    nums = {'0': 0, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
            '2': 2, '1': 1}

    num = num[::-1]
    for digit in num:
        converted += nums[digit] * place
        place *= 10
    return converted


def conv_frac(num):
    """converts the fractional portion of string num. returns a float"""
    place, converted = 10, 0
    nums = {'0': 0, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
            '2': 2, '1': 1}

    for digit in num:
        converted += nums[digit] / place
        place *= 10
    return converted


def conv_hex(num):
    """converts a valid hex number string. returns an int"""
    converted = 0
    hexdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
               'f': 15, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    num = num[::-1]
    for i, value in enumerate(num):
        if value not in hexdict:
            return None
        converted += hexdict[value] * (16 ** i)
    return converted
