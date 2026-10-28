def list_sum(numbers):
    if numbers == []:
        return None
    count = 0
    for i in numbers:
        if i in numbers:
            count += i
    return count
print(list_sum([2,4,6,8]))