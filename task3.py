
import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'[^\d+]', "", phone_number)

    if phone_number.startswith("+"):
        if not phone_number.startswith("+38"):
            phone_number = "+38" + phone_number.lstrip("+")
    else:
        phone_number = "+38" + phone_number
    return phone_number

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+80997654321"
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print(sanitized_numbers)