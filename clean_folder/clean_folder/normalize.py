import re
# import string

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str: 
    # TRANS = str.maketrans("", "", string.punctuation.replace('.', ''))
    # translate_name = name.split('.')
    # translate_name[0] = re.sub(r'\W', '_', translate_name[0].translate(TRANS))
    # new_name = ('.'.join(translate_name))
    # return new_name
    translate_name = re.sub(r'[^\w.]', '_', name.translate(TRANS))
    return 