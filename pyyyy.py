import random

def get_numbers_ticket(min, max, quantity):
 
    if (1 <= min <= max <= 1000) or (1 <= quantity <= max - min + 1):
        return []

    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min, max))

    sorted_numbers = sorted(list(numbers_set))
    return sorted_numbers

min_number = 1
max_number = 49
quantity_to_select = 6
result = get_numbers_ticket(min_number, max_number, quantity_to_select)
print(result)


