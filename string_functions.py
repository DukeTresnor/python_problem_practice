'''
Functions for Hamming distance between two DNA's -- https://exercism.org/tracks/python/exercises/hamming
enumerate for python -- https://blog.enterprisedna.co/python-for-loop-index/#:~:text=To%20access%20the%20index%20of,the%20item%20from%20the%20iterable.
'''


def calc_hamming_distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    combined_strand = strand_a + strand_b
    print(combined_strand)
    hamming_distance = 0
    print(f"Length of strand_b: {len(strand_a)}")
    print(f"Length of strand_b: {len(strand_b)}")
    print(combined_strand[len(strand_a)])
    for index, letter in enumerate(strand_a):
        print(f"Index: {index} has letter: {letter} -- what is second: {strand_b[index]}")
        if letter != strand_b[index]:
            hamming_distance += 1
    return hamming_distance
        

'''
Functions for reverse string -- https://exercism.org/tracks/python/exercises/scrabble-score

'''

def my_reverse(input_string):
    #return ''.join([i for i in reversed(string)])
    return input_string[::-1]