"""
2. Write a Python script to sort (ascending and descending) a dictionary by value.

Input:
Original Dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

Output:
Dictionary in ascending order by value  :  {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

"""


input_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print("Original Dictionary: ", input_dict)

print("\nDictionary in ascending order by value: ", {k: v for k, v in sorted(input_dict.items(), key=lambda item: item[1])})

print("\nDictionary in descending order by value: ", {k: v for k, v in sorted(input_dict.items(), key=lambda item: item[1], reverse=True)})

