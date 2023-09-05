#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0 in range(0,10)]

#a sentence list with "!"appended at the end of each sentence
def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]