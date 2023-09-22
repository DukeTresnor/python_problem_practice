import math



'''
Functions for perfect, abundant, or deficient classification problem -- https://exercism.org/tracks/python/exercises/perfect-numbers
Checking for a prime number -- https://www.programiz.com/python-programming/examples/prime-number
Aliquot Sum -- https://en.wikipedia.org/wiki/Aliquot_sum
'''

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    asum = aliquot_sum(number)
    if asum == number:
        # perfect number
        return "perfect"
    if asum > number:
        # abundant number
        return "abundant"
    if asum < number:
        # deficient number
        return "deficient"


def aliquot_sum(number):
    alisum = 0
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        alisum = 0
    else: #find the factors of number not counting itself
        alisum = 1
        for value in range(2, number-1):
            if (number % value) == 0:
                # number is evenly divisible by value -- add value to the aliquot sum
                alisum += value
    return alisum


'''
Functions for dart game -- https://exercism.org/tracks/python/exercises/darts

'''

def score(x, y):
    # coordinates -- x and y values for cartesian position of dart on the dart board
    # score -- An int that's the amount of points scored
    score = 0
    shot_radius = math.sqrt(x**2 + y**2)
    if shot_radius > 10.0:
        score = 0
    if shot_radius > 5 and shot_radius <= 10:
        score = 1
    if shot_radius > 1 and shot_radius <= 5:
        score = 5
    if shot_radius >= 0 and shot_radius <= 1:
        score = 10
    return score