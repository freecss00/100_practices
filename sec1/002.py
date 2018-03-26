s1 = 'パトカー'
s2 = 'タクシー'
res = [c1 + c2 for c1, c2 in zip(s1, s2)]
print(''.join(res))
