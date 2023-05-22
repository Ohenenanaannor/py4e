fname = input('enter file: ')
if len(fname) < 1: fname = './folder/clown.txt'
hand = open (fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print (lin)
    wds = lin.split()
    #print (wds)
    for w in wds:
  #      if w in di:
   #         di[w] = di[w] +1
   #         print('**Existing**')
    #    else:
   #         di[w] = 1
   #         print('**New**')

   #           or
        di[w] = di.get(w,0) + 1
   #     print(w, di[w])   

#print(di)

# now we want to find the most common word
theword= None
largest = -1
for k,v in di.items() :
    print (k,v)
    if v > largest :
        largest = v
        theword = k
     
print('done',largest)
print(theword, largest)



