'''
Matthew King
05/20/2014
DPW 1405
Lab 4 What Does the Fox Say
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self): #function that starts everything
    	p = Page() #assigning the Page class to a variable

    	k = Kinkajou() #assigning the Kinkajou class to a variable 

    	e = Eel() #assigning the Eel class to a variable

    	f = Frog() #assigning the Frog class to a variable

        if self.request.GET: #if a request is sent
        	pass
        else: #if a request is not sent
        	title = 'What Does the Amazon Say?' #change the page title
        	p.page_head = p.page_head.format(**locals()) #format variables in head tag
        	p.page_nav = p.page_nav.format(**locals()) #format variables in navigation tag
        	self.response.write(p.page_head + p.page_nav + p.page_close) #write the HTML code on the page

class Page(object): #Page class to write the HTML code
	def __init__(self):
		#HTML head tag
		self.page_head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>{title}</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" />
	</head>
	<body>'''
		#HTML navigation tag
		self.page_nav = '''<ul>
			<li><a href="?name={k.name}&phylum={k.phylum}&clss={k.clss}&order={k.order}&family={k.family}&genus={k.genus}&url={k.url}&avg={k.avg}&habitat={k.habitat}&geoloc={k.geoloc}&sound={k.sound}">Kinkajou</a></li>
			<li><a href="?name={e.name}&phylum={e.phylum}&clss={e.clss}&order={e.order}&family={e.family}&genus={e.genus}&url={e.url}&avg={e.avg}&habitat={e.habitat}&geoloc={e.geoloc}&sound={e.sound}">Eel</a></li>
			<li><a href="?name={f.name}&phylum={f.phylum}&clss={f.clss}&order={f.order}&family={f.family}&genus={f.genus}&url={f.url}&avg={f.avg}&habitat={f.habitat}&geoloc={f.geoloc}&sound={f.sound}">Frog</a></li>
		</ul>'''
		#HTML closing tag
		self.page_close = '''</body>
</html>'''

class Animal(object): #Animal Abstract class for various other Amazon animals 
	def __init__(self): 
		self.name = ''
		self.phylum = ''
		self.clss = ''
		self.order = ''
		self.family = ''
		self.genus = ''
		self.url = ''
		self.avg = ''
		self.habitat = ''
		self.geoloc = ''

class Kinkajou(Animal): #Kinkajou constructor class using the animal Abstract class
	def __init__(self):
		super(Animal, self).__init__() #constructor for super class
		self.name = 'Kinkajou'
		self.phylum = 'Chordata'
		self.clss = 'Mammalia'
		self.order = 'Carnivora'
		self.family = 'Procyonidae'
		self.genus = 'Potos'
		self.url = 'images/kinkajou.jpg'
		self.avg = '23 years'
		self.habitat = 'Forest'
		self.geoloc = 'Amazon'
		self.__sounds = []
		self.sound =''

class Eel(Animal): #Eel constructor class using the animal Abstract class
	def __init__(self):
		super(Animal, self).__init__() #constructor for super class
		self.name = 'Electric Eel'
		self.phylum = 'Chordata'
		self.clss = 'Actinopterygii'
		self.order = 'gymnotiformes'
		self.family = 'gymnotidae'
		self.genus = 'electrophorus'
		self.url = 'images/eel.jpg'
		self.avg = '15 years'
		self.habitat = 'River'
		self.geoloc = 'Amazon'
		self.__sounds = []
		self.sound =''

class Frog(Animal): #Frog constructor class using the animal Abstract class
	def __init__(self):
		super(Animal, self).__init__() #constructor for super class
		self.name = 'Poison Dart Frog'
		self.phylum = 'Chordata'
		self.clss = 'Amphibia'
		self.order = 'Anura'
		self.family = 'Dendrobatidae'
		self.genus = 'Dendrobates'
		self.url = 'images/frog.jpg'
		self.avg = '3 to 15 years'
		self.habitat = 'Tropical Forests'
		self.geoloc = 'Amazon'
		self.__sounds = []
		self.sound =''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
