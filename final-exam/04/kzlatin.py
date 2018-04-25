
alphabet = {
    'ғ': 'ǵ'
}

def convert(text):
    l = []
    for letter in text:
        lletter = alphabet.get(letter, letter)
        l.append(lletter)
    return "".join(l)
