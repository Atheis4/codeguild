sentence = input('Veni, vidi, vici! What would you like to translate?\n> ')

to_be_translated = sentence.split()

pig_sentence = []
vowels = 'aeiouAEIOU'
punctuation = '.!,;:'

for word in to_be_translated:

    word = word.lower()

    if word[0] in vowels and word[-1] in punctuation:
        piggy = ''.join(word[:-1] + 'yay' + word[-1])
    elif word[0] in vowels:
        piggy = ''.join(word + 'yay')
    elif word[-1] in punctuation:
        piggy = ''.join(word[1:-1] + word[0] + 'ay' + word[-1])
    else:
        piggy = ''.join(word[1:] + ''.join(word[:1].lower() + 'ay'))

    pig_sentence.append(piggy)

translated = ' '.join(pig_sentence)

print(translated.capitalize())
