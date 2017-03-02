try:
    sampleFile = open('lol.txt', 'r')
except IOError:
    raise IOError('Filename does not exist')
#sampleFile = open ('random.txt', 'r')
line1 = sampleFile.readline().strip()
print line1
for i in sampleFile:
    i = i.strip()
    print i
