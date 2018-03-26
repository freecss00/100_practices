import re
from enum import Enum

CHAR = 1
WORD = 2


def n_gram(n, string, unit=WORD):
    if unit == WORD:
        seq = re.findall(r'\w+', string)
    elif unit == CHAR:
        seq = re.findall(r'\w', string)

    delm = ' ' if unit == WORD else ''
    res = [delm.join(seq[i:i+n]) for i in range(len(seq) - n + 1)]
    return res


if __name__ == '__main__':
    s = 'I am an NLPer'
    word_bi_gram = n_gram(2, s, WORD)
    char_bi_gram = n_gram(2, s, CHAR)

    print(word_bi_gram)
    print(char_bi_gram)
