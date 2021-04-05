#2/9/2021
#Debra Sparr
#Assignment 4 - string methods

import re
import functools

RE = r'[^\w\s]'

def string_methods():
    """ Counts the number of words in a sentence entered by the user """
    try :
        users_string = input("Please enter a sentence to get the number of words and average word length : \n")
        # Remove punctuation from string
        users_string = re.sub(RE, '', users_string)
        # Split string into list
        words_list = users_string.split()
        # Grab the number of elements in the words list
        num_of_words = len(words_list)
        # determine the number of characters in the word list
        character_counter = functools.reduce( lambda x, y :  len(y) + x, words_list, 0)
        # Calculate average by dividing total number of non-punctuation characters by the number of elements in the words list, then round
        avg_word_length = round(character_counter/num_of_words)
        print(f"Number of words : {num_of_words} \nAverage word length : {avg_word_length}")

    except ZeroDivisionError:
        print("You must enter something!")


if __name__ == '__main__' :
    string_methods()