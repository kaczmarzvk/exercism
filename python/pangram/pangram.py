#97-122 == a-z
letters_values = list(range(97, 123))

def is_pangram(sentence):
    # input letters as no repeat ascii values
    input_letters_ascii = []
    # codification
    sentence = sentence.lower()
    for l in sentence:
        # isalpha == is a letter
        if l.isalpha():
            l_ascii = ord(l)
            if l_ascii not in input_letters_ascii:
                input_letters_ascii.append(l_ascii)
    input_letters_ascii.sort()
    return letters_values == input_letters_ascii

