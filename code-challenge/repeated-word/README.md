# Challenge Summary

This challenge asks us to write a function that takes a large string as an arguement and returns the first repeated word that is found.

Take a string and iterate through the words in the string. Return the first instance of a repeated word.
```
$ string = "Once upon a time, there was a brave princess who..."
$ result = repeated_word(string)
$ result
$ 'a'
```
## Whiteboard Process
![Whiteboard Solution]()
![Whiteboard Solution]()

## Approach & Efficiency
The approach here is to get an iterable for all of the words in the string. A list is best suited iterable for storing all of the words from the string. Before storing the words, the original string needs to be cleaned up a bit.

We are using re - Python's regular expression package to substitue any punctuation with a null string. When the string is just words and spaces we can split the string using the String.split method. 

We are returned a list of all of the words and can begin keeping track of what words we have seen and when we hit that first repeated word. Because we have a list of all words, we can iterate through them and append the words to new list. We check that new list for each iteration of the word-list. As soon as there is a match in the new list we return the word.

The efficency here breaks down to is O(N) for time and O(N) for space.

## Solution
* Input ...............	............................................Output
"Once upon a time, there was a brave princess who..." ...........	"a"