import re

def repeated_word(string):
    """
    Accepts a string as an arguement. 
    Returns a list: [first_repeated_word, dictionary_of_all_words, sorted_list_of_most_frequent_words]
    """
    string = re.sub(r'[^\w\s]', '', string)
    all_words = {}
    first_matching_word = ''
    most_frequent_words = []

    # Modify your function to return a count of each of the words in the provided string
    for word in string.split():
        word = word.lower()
        try:
            all_words[word] += 1
            first_matching_word = first_matching_word or word
        except:
            all_words[word] = 1

    # Modify your function to return a list of the words most frequently used in the provided string
    for key in all_words:
        most_frequent_words.append((all_words[key], key))
    most_frequent_words.sort(reverse=True)

    # check if any words matched
    if first_matching_word:
        return [first_matching_word, all_words, most_frequent_words]
    return ["No repeating words found", all_words, most_frequent_words]