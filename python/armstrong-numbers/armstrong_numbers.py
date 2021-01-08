def is_armstrong_number(number):
    num_as_string = str(number)
    result = 0
    for n in num_as_string:
        num = int(n)
        result += (num ** len(num_as_string))
    return True if number == result else False



