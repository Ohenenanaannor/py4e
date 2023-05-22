fr = open('./folder/mbox.txt','r')
print(fr)
for line in fr:
    lane = line.rstrip()
    print(lane.upper())
    

  