from repeated_word import __version__
import pytest
from repeated_word.repeated_word import repeated_word



def test_version():
    assert __version__ == '0.1.0'



def test_simple_string():
    string = "Once upon a time, there was a brave princess who.."
    lst = repeated_word(string)
    assert lst[0] == 'a'

def test_no_repeats():
    string = "The rain in spain falls mainly on a plain."
    lst = repeated_word(string)
    assert lst[0] == 'No repeating words found'

def test_capitalization():
    string = "Cat dog cat dog."
    lst = repeated_word(string)
    assert lst[0] == 'cat'

def test_longer_string():
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."	
    lst = repeated_word(string)
    assert lst[0] == 'it'

def test_punctuation():
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    lst = repeated_word(string)
    assert lst[0] == 'summer'

def test_all_word_counts_no_repeats():
    string = "The rain in spain falls mainly on a plain."
    lst = repeated_word(string)
    assert lst[1] == {'the':1,'rain':1,'in':1,'spain':1,'falls':1,'mainly':1,'on':1,'a':1,'plain':1}

def test_all_word_counts():
    string = 'Cat cat cat cat, dog dog dog, bird bird, fish.'
    lst = repeated_word(string)
    assert lst[1] == {'cat':4,'dog':3,'bird':2,'fish':1}

def test_sorted_list():
    string = 'Cat cat cat cat, dog dog dog, bird bird, fish.'
    lst = repeated_word(string)
    assert lst[2] == [(4, 'cat'), (3,'dog'), (2,'bird'), (1,'fish')]