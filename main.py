
def get_multiplied_digits(numbers):
    str_numbers = str(numbers)
    if len(str_numbers) > 1:
        first = int(str_numbers[0])
        return first * get_multiplied_digits(int(str_numbers[1:]))
    else:
        return int(str_numbers)
result = get_multiplied_digits(40203)
print(result)


