import string

def reverse_sentence(sentence):
    return sentence[::-1]

def odd_position_characters(input_string):
    return input_string[1::2]

def starts_with_specific_char(input_string, char):
    return input_string.startswith(char)

def remove_newlines(input_string):
    return input_string.replace('\n', '')

def replace_substring(input_string, old_substring, new_substring):
    return input_string.replace(old_substring, new_substring)

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

def matching_characters(string1, string2):
    return len(set(string1) & set(string2))

def string_to_list(input_string):
    return list(input_string)

def find_domain_name(input_string):
    start = input_string.find('www.') + 4
    end = input_string.find('.com', start)
    return input_string[start:end]

def convert_list_elements_to_int(string_list):
    return [int(item) for item in string_list]

def count_upper_lower_case(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count

def find_vowels(input_string):
    vowels = "aeiouAEIOU"
    return [char for char in input_string if char in vowels]

def reverse_user_input():
    user_input = input("Enter a string: ")
    return user_input[::-1]

def sort_string(input_string):
    return ''.join(sorted(input_string))

def print_upper_lower_case(input_string):
    print("Uppercase:", input_string.upper())
    print("Lowercase:", input_string.lower())

def int_to_string(number):
    return str(number)

user_sentence = input("Enter a sentence: ")

reversed_sentence = reverse_sentence(user_sentence)
print("Reversed sentence:", reversed_sentence)

odd_chars = odd_position_characters(user_sentence)
print("Characters at odd positions:", odd_chars)

specific_char = input("Enter a specific character: ")
starts_with = starts_with_specific_char(user_sentence, specific_char)
print("Starts with '{specific_char}': {starts_with}")

without_newlines = remove_newlines(user_sentence)
print("Without newlines:", without_newlines)

substring_replace = replace_substring(user_sentence, "is", "was")
print("Substring replaced:", substring_replace)

without_punctuation = remove_punctuation(user_sentence)
print("Without punctuation:", without_punctuation)

second_sentence = input("Enter another sentence: ")
matching_chars = matching_characters(user_sentence, second_sentence)
print("Number of matching characters:", matching_chars)

list_from_string = string_to_list(user_sentence)
print("String as a list:", list_from_string)

input_domain = input("Enter a string with a domain (e.g., www.example.com): ")
domain_name = find_domain_name(input_domain)
print("Domain name:", domain_name)

string_list = ['1', '2', '3', '4', '5']
int_list = convert_list_elements_to_int(string_list)
print("List with string elements converted to int:", int_list)

upper_count, lower_count = count_upper_lower_case(user_sentence)
print("Uppercase count:", upper_count)
print("Lowercase count:", lower_count)

vowels_found = find_vowels(user_sentence)
print("Vowels in the string:", vowels_found)

reversed_input = reverse_user_input()
print("Reversed user input:", reversed_input)

sorted_string = sort_string(user_sentence)
print("Sorted string:", sorted_string)

print_upper_lower_case(user_sentence)

number = 42
number_as_string = int_to_string(number)
print("Number as string:", number_as_string)