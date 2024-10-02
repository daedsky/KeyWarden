import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate(length: int = 8,letters: bool = True, _digits: bool = True, symbols: bool = True):

    # the minimum length of password must be 4 letters
    # at least any of these should be true
    if not any([letters, _digits, symbols]) or length < 4:
        return

    # "<" and ">" can cause issues in some sites so better to be safe.
    _symbols = punctuation.replace('<', '').replace('>', '')

    # the letters that we can use in our password
    eligible_letters = ''

    # the password to return
    pswd = ''

    # add at least one letter of the the specified type
    if letters:
        # if we can use letters
        pswd += random.choice(ascii_lowercase)
        pswd += random.choice(ascii_uppercase)
        eligible_letters += ascii_uppercase
        eligible_letters += ascii_lowercase
    if _digits:
        # if we can use digits
        pswd += random.choice(digits)
        eligible_letters += digits
    if symbols:
        # if we can use symbols
        pswd += random.choice(_symbols)
        eligible_letters += _symbols


    for x in range(length-len(pswd)):
        random.shuffle(eligible_letters.split())
        pswd += random.choice(eligible_letters)

    return pswd

if __name__ == "__main__":
    print(generate(80))
