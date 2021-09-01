import string
import random
import math
# Try to get the value from the settings module


def generate_url():
    alpha_characters = string.ascii_letters
    number_characters = string.digits
    all_characters = alpha_characters + number_characters
    final_string = ""
    for i in range(0, 7):
        rand_int = math.floor(random.random() * len(all_characters))
        final_string += all_characters[rand_int]
        i = i + 1
    return final_string

