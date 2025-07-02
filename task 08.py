def multiply_numbers(inputs = None):
    if inputs is None:
        return None
    
    text = str(inputs)
    result = 1
    count = 0
    for char in text:
        if char.isdigit():
            num = int(char)
            result *= num
            count += 1

    if count == 0:
        return None

    return result
print(multiply_numbers(123))
print(multiply_numbers('sssdd34'))
print(multiply_numbers([5,6,4]))
print(multiply_numbers(2.3))
print(multiply_numbers())


