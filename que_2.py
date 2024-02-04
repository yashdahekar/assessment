"""2.  Write a program that takes a string as input, and counts the frequency of each word in the string, there might  be repeated characters in the string. Your task is to find the highest frequency and returns the length of the  highest-frequency word. """

def lenght_of_highest_frequency_word(string):
    words = string.split()
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    
    max_freq = max(word_frequency.values())#highest frequency

    max_word_length = max(len(word) for word, freq in word_frequency.items() if freq == max_freq)# finding lenght 

    return max_word_length

# Test cases
example_string = [
    "Write a program that takes a string as input, and counts the frequency of each word in the string, there might  be repeated characters in the string. Your task is to find the highest frequency and returns the length of the  highest-frequency word.",
    "Explanation - From the given string we can note that the most frequent words are “write” and “from” and  the maximum value of both the values is “write” and its corresponding length is 5 "
]

for test_case in example_string:
    print(lenght_of_highest_frequency_word(test_case))
