import random

file = open("dictionary.txt","r")
tempd= file.read()
wordlist = tempd.split("\n")
wordlist.sort()
print(wordlist)
rand = random.randint(0,len(wordlist)-1) #0 <= rand <= len(tempd) - 1
print(rand)
wordanddef = wordlist[rand]
print(wordanddef)

#Find the *
locstar = wordanddef.index("*")
solution = []
solution.append(wordanddef[0:locstar])
solution.append(wordanddef[locstar + 1:])
word = 
print(