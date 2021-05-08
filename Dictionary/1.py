"""
1. Write a Python script to add a key to a dictionary.

Input:
Original Dictionary : {0: 10, 1: 20}

Output:
{0: 10, 1: 20, 2: 30}

"""


input_dict = {0: 10, 1: 20}

print("Original Dictionary: ", input_dict)

input_dict.update({2: 30})
print("\nNew Dictionary: ", input_dict)