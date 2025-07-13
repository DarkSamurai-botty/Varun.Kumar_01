word = input("Enter a word ")

reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word

vowel_count = 0
for letter in word:
    if letter in "aeiouAEIOU":
        vowel_count += 1

print("Reversed word:", reversed_word)
print("Number of vowels:", vowel_count)
