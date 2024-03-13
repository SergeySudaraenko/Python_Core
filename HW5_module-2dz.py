import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    matches = re.finditer(pattern, text)

    for match in matches:
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total_sum = sum(numbers_generator)

    return total_sum

text = "Income: 100.5 Expenses: 20.3 Profit: 80.2"
result = sum_profit(text, generator_numbers)
print(f"Total Profit: {result}")