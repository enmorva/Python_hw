def multiply_list(elements: list[int], multiplier: int = 2) -> list[int]:
    result = []
    for item in elements:
        result.append(item * multiplier)
    return result

def multiply_list_lambda(elements: list[int], multiplier: int = 2) -> list[int]:
    return list(map(lambda x: x * multiplier, elements))

numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))       
print(multiply_list(numbers, 3))     
print(multiply_list_lambda(numbers))
