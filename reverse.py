import sys
import random

string_to_be_reversed = sys.argv[1:]

def reverse_string(string_to_be_reversed):
    string_to_be_reversed.reverse()
    string_to_be_reversed = " ".join(string_to_be_reversed)
    print(string_to_be_reversed)


reverse_string(string_to_be_reversed)
