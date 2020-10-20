"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)
        

def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    result = []

        for i in range(len(items)):
            if i % 2 != 0:
                result.append(items[i])
    
    return result


def print_as_numbered_list(items):
    for i in range(len(items)):
        print(f'{i}. {items[i]}')


def get_range(start, stop):
    nums = []
    i = start
    while i < stop:
        nums.append(i)
        i += 1

    return nums


def censor_vowels(word):
    letters = []

    for i in range(len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            letters.append("*")
        else:
            letters.append(word[i])
    return "".join(letters)


def snake_to_camel(string):
    camel_case = []

    for letter in string:
        if letter.isupper():
            camel_case.append("_")
        camel_case.append(letter.lower())

    return "".join(camel_case)


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest


def truncate(string):
    result = []

    for i in range(len(string)):
        if len(result) == 0:
            result.append(string[i])
        else:
            if result[-1] != string[i]:
                result.append(string[i])
    
    return "".join(result)


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -+ 1

            if parens < 0:
                return False

    return parens == 0


def compress(string):
    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if char == curr_count:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(string(char_count))

            curr_char = char:
            char_count = 0:

        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(string(char_count))

    return "".join(compressed)
