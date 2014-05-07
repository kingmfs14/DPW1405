#one lined comments
'''
Doc strings for 
multiline comments
'''

first_name = 'kermit'
last_name = 'de frog'
#print first_name

#response = raw_input('enter your name   ')
#print 'Hello there, ', response

birth_year = 1988
current_year = 2014
age = current_year - birth_year
#print 'You are ' + str(age) + ' years old'

budget = 50

if budget>100:
	brand = 'nike'
	print 'Yay! we can buy cool ' + brand + ' shoes!'
elif budget>70:
	print 'We can at least get some generic sneakers.'
else:
	#works inside of loops, functions, and conditional statements
	pass

characters = ['leia', 'luke', 'chewy', 'lando']
characters.append('obi won')
#print characters[0]

movies = dict() #create dictionary object
movies = {'star wars': 'darth vader', 'silence of the lambs': 'hannibal'}
#print movies['star wars']

#while loop--------
'''
i = 0
while i<9:
	print 'the count is', i
	i += 1
'''

#for loop--------
'''
for i in range(0,9):
	print 'the count is', i
	i += 1
'''

#for each loop ------
rappers =['tupac', 'nas', 'biggie']
for r in rappers:
	#print 'one of the best rappers is ' + r
	pass

#function------

x = 2

def calcArea(h, w):
	area = h*w
	return area + x

a = calcArea(20, 40);
#print 'my area is ' + str(a) + 'sqft'

weight = 200
height = 63
message = '''
your height is {height} and your weight is {weight}
'''
message = message.format(**locals())
#print message


title = 'contact us'
body = 'you can contact us at contact@us.com'
message = '''
<!DOCTYPE HTML>
	<head>
		<title>{title}</title>
	</head>
	<body>
		{body}
	</body>
</html>
'''
message = message.format(**locals())
print message








