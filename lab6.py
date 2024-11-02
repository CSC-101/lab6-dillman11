import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(books:list[data.Book]) -> list[data.Book]:
    for i in range(len(books)-1):
        small_index = i
        for j in range(i+1, len(books)):
            if books[j].title.lower() < books[small_index].title.lower():
                small_index = j
        if small_index != i:
            temp = books[i]
            books[i] = books[small_index]
            books[small_index] = temp
    return books

# Part 2
def swap_case(word:str) -> str:
    swapped_word = ""
    for letter in word:
        if letter.isalpha():
            if letter.islower():
                swapped_word += letter.upper()
            else:
                swapped_word += letter.lower()
        else:
            swapped_word += letter
    return swapped_word

# Part 3
def str_translate(word:str, old:str, new:str) -> str:
    new_word = ""
    for letter in word:
        if letter == old:
            letter = new
        new_word += letter
    return new_word


# Part 4
def histogram(word:str) -> dict:
    letter_dict = {}
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] =1
    return letter_dict
