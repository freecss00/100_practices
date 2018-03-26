import re
s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = re.findall(r'\w+', s)
print(' '.join([str(len(word)) for word in words]))
