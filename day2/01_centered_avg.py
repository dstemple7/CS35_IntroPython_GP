# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array.

# what do we do if smallest or largest is duplicated
# - we only consider 1 of smallest and 1 of largest to be valid

# what data type are we expecting to return?
# int / float?
# return an int

# centered_average([1, 2, 3, 4, 100]) → 3 >>> [2, 3, 4, 100] -> [2, 3, 4] -> 2 + 3 + 4 => 9 / 3 => 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5 >>> [1, 5, 5, 10, 8, 7] -> [1, 5, 5, 8, 7] -> 1 + 5 + 5 + 8 + 7 => 26 / 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3 >>> [-4, -2, -4, -2, 0] -> [-4, -2, -4, -2]  => -4 + -2 + -4 + -2 => -12 / 4 => -3

# centered_average([1, 2, 3, 4, 100]) -> 3 >>> [1, 2, 3, 4, 100] -> 1 + 2 + 3 + 4 + 100 => 110 => 110 - max => 10 - min => 9 / 3 => 3
# max = 100
# min = 1

"""
1. take numbers from list and add them together after extrapolating the smallest and lasrgest numbers in to their own variables
2. take the sum of the numbers and minus the max of the list
3. take what's left and minus the min of the list

get the smallest value from the list
get the largest value from the list

make a sum / counter variable and set it to zero
loop over each number in our list and sum up all of the numbers

use the algorithm (sum = sum - largest - smallest)

apply the algorithm of sum divided by the length of our list minus two

"""

import statistics


def centered_avg(ints):
    largest = max(ints)
    smallest = min(ints)

    sum = 0
    for num in ints:
        sum += num

    sum = sum - largest - smallest

    return sum // (len(ints) - 2)


print(centered_avg([1, 2, 3, 4, 100]))  # expecting a 3
print(centered_avg([1, 1, 5, 5, 10, 8, 7]))  # expecting a 5
print(centered_avg([-10, -4, -2, -4, -2, 0]))  # expecting a -3


def centered_avg2(ints):
    ints.sort() # problem is this is expecting a sorted list so need to first sort it
    return int(statistics.mean(ints[1:-1])) #wrap this in int so that it gives an integer and not a floating point number / e.g. 2 vs. 2.25


print(centered_avg2([1, 2, 3, 4, 100]))  # expecting a 3
print(centered_avg2([1, 1, 5, 5, 10, 8, 7]))  # expecting a 5
print(centered_avg2([-10, -4, -2, -4, -2, 0]))  # expecting a -3
print(centered_avg2([1, 3, 2, 7, 9, 0]))  # expecting a 3

# Tom ran with code to test how long it takes to do this and built in solution, i.e. centered_avg2, is 30-40x slower than custom solution, i.e. centered_avg

