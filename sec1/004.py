import re
s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
words = re.findall(r'\w+', s)
word_map = {}
for i, w in enumerate(words):
    key = w[0] if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19] else w[:2]
    word_map[key] = i+1

print(sorted(word_map.items(), key=lambda x: x[1]))
