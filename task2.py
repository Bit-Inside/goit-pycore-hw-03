
import random

def get_numbers_ticket(min, max, quantity):
    if(
        not isinstance(min, int) or
        not isinstance(max, int) or
        not isinstance(quantity, int)
        ):
        return[]
    
    if min >= max or quantity <= 0 or quantity > (max - min + 1):
        return[]
    
    numbers = set()

    while len(numbers) < quantity:
        num  = random.randint(min, max)
        numbers.add (num)

    return sorted(numbers)
    
result = get_numbers_ticket(2, 50, 5)
print(result)