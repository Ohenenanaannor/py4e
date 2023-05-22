import re
hand = open('./folder/spss.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('UPTIME TOTALS FOR ATM ([0-9]+)', line)
    #cat = re.findall('Online \d+ \d+ ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    #if len(cat) != 1 : continue
    #print(cat)
    print (stuff)

