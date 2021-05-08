"""
Find the average of all contiguous subarrays of size 'K' in the given array.

Input:
Array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5

Output: 
For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6-1)/5 => 2.2
For the next 5 numbers (subarray from index 1-5), the average is: (3+2+6-1+4)/5 => 2.8
For the next 5 numbers (subarray from index 2-6), the average is: (2+6-1+4+1)/5 => 2.4
For the next 5 numbers (subarray from index 2-6), the average is: (6-1+4+1+8)/5 => 3.6
For the next 5 numbers (subarray from index 2-6), the average is: (-1+4+1+8+2)/5 => 2.8

The final output containing the averages of all contiguous subarrays of size 5:
[2.2, 2.8, 2.4, 3.6, 2.8]

"""

def avg_contiguous_subarray(in_array, K):
    avg = []
    for i in range(K):
        avg.append(sum(in_array[i:i+K])/K)
    return avg


in_array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = int(input("Enter the size of contiguous subarrays: "))

if K > len(in_array):
    print("Length of input array = " + str(len(in_array)) + " is smaller than contiguous subarrays = " + str(K))
else:
    print(avg_contiguous_subarray(in_array, K))
