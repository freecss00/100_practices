# Unix command
# cat hightemp.txt | tr '\t' ' '
s = open('hightemp.txt').read()
replaced = s.replace('\t', ' ')
print(replaced)
