import re
import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
res = []
for w in s.split(' '):
    if len(w) >= 4:
        shuffled = w[0] + ''.join(random.sample(w[1:-1], len(w) - 2)) + w[-1]
        res.append(shuffled)
    else:
        res.append(w)

print(' '.join(res))
