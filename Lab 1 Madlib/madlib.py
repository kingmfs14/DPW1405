#SETTING UP THE INPUT VARIABLES---------------------------------

person = raw_input('enter your name   ')
name = raw_input("enter a person's name   ")
adv = raw_input('enter an adverb  ')
body = raw_input('enter a body part   ')
memNum = raw_input("enter a number between 0 and 5   ")
adjNum = raw_input('enter a number between 1 and 10   ')

#SETTING THE FAMILY MEMBER ROLES---------------------------------

num = int(memNum)
if num > 3:
	mem1 = 'grandma'
	mem2 = 'grandson'
elif num < 3:
	mem1 = 'mom'
	mem2 = 'son'
else:
	mem1 = 'sis'
	mem2 = 'bro'

#SETTING ALL THE ADJECTIVES UP IN MADLIB------------------------

adj1Array = ['lovely', 'horrible', 'bad', 'nice', 'good', 'difficult', 'meaningful', 'hard', 'wonderful', 'delightful', 'splendid']
adj2Array = ['nice', 'mean', 'awful', 'tall', 'heroic', 'lean', 'honest', 'fit', 'obedient', 'cheerful', 'talkative']
adj3Array = ['wonderful', 'salty', 'terrible', 'healthy', 'diverse', 'bland', 'radical', 'burnt', 'fruity', 'greasy', 'hot']
adj4Array = ['close', 'distant', 'good', 'helpful', 'energetic', 'fast', 'easy', 'zealous', 'great', 'silly', 'jolly']
adj5Array = ['large', 'tall', 'short', 'fat', 'skinny', 'ugly', 'young', 'old', 'lazy', 'shy', 'small']

def adjectives(num):
	adj1 = adj1Array[num]
	adj2 = adj2Array[num]
	adj3 = adj3Array[num]
	adj4 = adj4Array[num]
	adj5 = adj5Array[num]
	return adj1, adj2, adj3, adj4, adj5

num = int(adjNum)
adj1, adj2, adj3, adj4, adj5 = adjectives(num);

#SETTING THE MADLIB TO PRINT THE MESSAGE-------------------------
message = """
Dear {mem1},
I am having a {adj1} time at camp. The counselor is {adj2} and the food is {adj3}. I met {name} and we became {adj4} friends. Unfortunately, {name} is {adj5} and I {ed} my {body} so we couldn't go {ing} like everyone else. I need more {plural} and a {noun} sharpener, so please {adv} {verb1} more when you {verb2} back.
Your {mem2},
{person}
"""

message = message.format(**locals())
print message