# Unix command
# paste col1.txt col2.txt
col1 = open('col1.txt').readlines()
col2 = open('col2.txt').readlines()
with open('merged_col.txt', mode='w') as f:
    for c1, c2 in zip(col1, col2):
        f.write('{}\t{}\n'.format(c1.strip(), c2.strip()))

