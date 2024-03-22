# Function to count the number of vowels in a string
def countvowels(string):
    string = string.lower()
    vowel_count = 0
    vowels = "aeiou"
    for char in string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count


input_string = input("Please enter a string: ")

vowelcount = countvowels(input_string)
print(f"Number of vowels in the string: {vowelcount}")
