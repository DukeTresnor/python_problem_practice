import number_functions
import string_functions


#number = 2023
#result = number_functions.classify(number)
#print(result)


astring = "AGCTC"
bstring = "AGCTV"

hamming_distance = string_functions.calc_hamming_distance(astring, bstring)

print(hamming_distance)