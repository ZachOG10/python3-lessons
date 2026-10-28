def find_smallest(numbers):
    if numbers == []:
        return None
    smallest_number = numbers[0]
    for i in numbers:
        if i < smallest_number:
            smallest_number = i
    return smallest_number
print(find_smallest([8,3,12,1,7]))