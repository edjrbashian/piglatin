#English to pig-latin translator
#Edward Djrbashian

#define suffix
pyg = 'ay'

#ask used for word
original = raw_input('Enter a word:')

#define first letter of string
first = original[0]

if len(original) > 0 and original.isalpha():
#check if vowel or consonant
    if first == ('a' or 'e' or 'i' or 'o' or 'u'):
        new_word= original + pyg
        print(new_word)
    else:
        new_word=original[1:] +first + pyg
        print new_word
else:
    print 'empty'

