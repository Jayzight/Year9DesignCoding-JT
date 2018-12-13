#A loop is a programming structure that can repeat a section of code
#A loop can run the same code exactly over and over or
#with some thought it can generate a pattern

#There are two broad catagories of loops
#Conditional Loops (While): These loop as long as a condition is true

#Counted Loops (For): These loop using a counter to keep track of how many the loop has run.

#You can use any loop in any situation, but usually from a design perspective there is a better loop in terms of coding

#If you know in advance how many times a loop should run a COUNTED LOOP
#is usually the better choice

#If you don't know how many times a loop should run a CONDITIONAL LOOP is
#usually better

print("************************************************")
#Taking Inputs
word = ''
while len(word) < 6:
	word = input("Please input a word larger than 5 letters:")
	print(word.isalpha())
	if (len(word) < 6):
		print ("Yo, MORE THAN 5 LETTERS")

	if (word.isalpha() == False):
		

print(word+" is a really long word")