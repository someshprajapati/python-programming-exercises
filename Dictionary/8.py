"""
Write a Python program to remove a key from a dictionary.

"""

input_dict = {'a':1, 'b':2, 'c':3, 'd':4}

print("Original Dictionary: ", input_dict)

def updated_dict(input_dict, rm_key):
    if rm_key in input_dict: 
        del input_dict[rm_key]
    return input_dict

rm_key = input("Enter the Key which you want to remove from a dictionary: ")

print("\nUpdated Dictionary: ", updated_dict(input_dict, rm_key))