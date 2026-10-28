def find_largest(numbers):
    if numbers == []:
        return None
    largest_number = numbers[0]
    for i in numbers:
        if i > largest_number:
            largest_number = i
    return largest_number
print(find_largest([3,41,56,21,76,9]))