# CS 362-400 Group 53
import math


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
        num_str = conv_frac(num_str[1:])
    elif percount == 1 and num_str[-1] == '.':
        num_str = conv_whole(num_str[:-1]) + 0.0

    # split str at decimal point position if nums on both sides of decimal pt
    elif percount == 1:
        wholeNum = conv_whole(num_str[:charpos])
        fracNum = conv_frac(num_str[charpos + 1:])
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


# Function 2 Author: Ben Depew
# Main function definition
def my_datetime(num_sec):
    num_days = calc_days(num_sec)
    num_years, num_days = calc_years(num_days)
    month, day, year = calculate_date(num_years, num_days)
    date = convert_to_string(month, day, year)
    return date


# Calculate days from seconds
def calc_days(num_sec):
    num_days = 0
    sec_in_day = 86400
    while num_sec >= sec_in_day:
        num_sec -= sec_in_day
        num_days += 1
    return num_days


# Calculate number of 400 year cycles to simplify by
def calc_years(num_days):
    days_in_400years = 146097
    num_years = 0

    while num_days >= days_in_400years:
        num_days -= days_in_400years
        num_years += 400

    return num_years, num_days


# Calculate month, day, year
def calculate_date(num_years, num_days):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_leapyear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    current_year = 1970 + num_years
    current_month = 1
    current_day = 1

    while num_days:
        calendar = days_in_month
        if current_year % 400 == 0:
            calendar = days_in_month_leapyear
        elif current_year % 100 == 0:
            calendar = days_in_month
        elif current_year % 4 == 0:
            calendar = days_in_month_leapyear
        if current_day == calendar[current_month - 1]:
            current_month += 1
            if current_month == 13:
                current_month = 1
                current_year += 1
            current_day = 0
        current_day += 1
        num_days -= 1
    return current_month, current_day, current_year


# Convert month day and year to the right string output
def convert_to_string(month, day, year):
    date = str(month) + "-"
    if month < 10:
        date = "0" + date
    if day < 10:
        date = date + "0"
    date = date + str(day) + "-" + str(year)
    return date


# Author: Andrew Yemtsev, Christine Pham
# Function that convert number into a hex letter
def conv_endian(num, endian="big"):
    num = math.trunc(num)

    sign = ''
    if num < 0:
        sign = '-'
        num *= -1

    converted = make_hex(num)

    # tack on 0 if hex has uneven length
    if len(converted) % 2 != 0:
        converted = '0' + converted

    # split hex number into pairs
    converted = [converted[i:i + 2] for i in range(0, len(converted), 2)]

    if endian == 'big':
        return sign + " ".join(converted)
    elif endian == 'little':
        converted.reverse()
        return sign + " ".join(converted)
    return None


# helper function to convert integer into hexadecimal
def make_hex(num):
    hex_val = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
               6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
               11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    hex_str = ''
    while num != 0:
        num_floor, rem = divmod(num, 16)
        hex_str += hex_val[rem]
        num = num_floor

    return hex_str[::-1]
