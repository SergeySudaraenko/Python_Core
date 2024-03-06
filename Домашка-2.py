
import random

def get_numbers_ticket(min_num, max_num, quantity):
   
    if min_num < 1 or max_num > 1000 or quantity < 0 or quantity > (max_num - min_num + 1):
        return []

    
    numbers_set = set()
    while len(numbers_set) < quantity:
        random_number = random.randint(min_num, max_num)
        numbers_set.add(random_number)

    
    return sorted(list(numbers_set))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)