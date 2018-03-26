# Unix command
# cat hightemp.txt | cut -f1,2
lines = open('hightemp.txt').readlines()

with open('col1.txt', mode='w') as f:
    f.writelines([line.split()[0] + '\n' for line in lines])
with open('col2.txt', mode='w') as f:
    f.writelines([line.split()[1] + '\n' for line in lines])
