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
    	k.sounds = ['kit kit kit kow', 'buzz buzz buzz bozz', 'webt webt webt wob'] #creating a sound array with all animal sounds

    	e = Eel() #assigning the Eel class to a variable
    	e.sounds = ['kit kit kit kow', 'buzz buzz buzz bozz', 'webt webt webt wob'] #creating a sound array with all animal sounds

    	f = Frog() #assigning the Frog class to a variable
    	f.sounds = ['kit kit kit kow', 'buzz buzz buzz bozz', 'webt webt webt wob'] #creating a sound array with all animal sounds

        if self.request.GET: #if a request is sent
        	name = self.request.GET['name'] #get the name variable from object clicked
        	title = name + "'s Information" #set the name vairable in the title object
	        phylum = self.request.GET['phylum'] #get the phylum variable from object clicked
	    	clss = self.request.GET['clss'] #get the class variable from object clicked
	    	order = self.request.GET['order'] #get the order variable from object clicked
	    	family = self.request.GET['family'] #get the family variable from object clicked
	    	genus = self.request.GET['genus'] #get the genus variable from object clicked
	    	url = self.request.GET['url'] #get the url variable from object clicked
	    	avg = self.request.GET['avg'] #get the average life span variable from object clicked
	    	habitat = self.request.GET['habitat'] #get the habitat variable from object clicked
	    	geoloc = self.request.GET['geoloc'] #get the geolocation variable from object clicked
	    	sound = self.request.GET['sound'] #get the sound variable from object clicked
        	p.page_head = p.page_head.format(**locals()) #format variables in head tag
	        p.display_info = p.display_info.format(**locals()) #format variables in information tag
	        self.response.write(p.page_head + p.display_info + p.page_close) #write the HTML code on the page
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
		#HTML body information tag
		self.display_info = '''<table id='wrapper'>
			<tr>
				<td>		
					<table>
						<tr>
							<th>Phylum:</th>
							<th>Class:<th>
						</tr>
						<tr>
							<td>{phylum}</td>
							<td>{clss}<td>
						</tr>
						<tr>
							<th>Order:</th>
							<th>Family:<th>
						</tr>
						<tr>
							<td>{order}</td>
							<td>{family}<td>
						</tr>
						<tr>
							<th>Genus:</th>
							<th>Average Lifespan:<th>
						</tr>
						<tr>
							<td>{genus}</td>
							<td>{avg}<td>
						</tr>
						<tr>
							<th>Habitat:</th>
							<th>Geolocation:<th>
						</tr>
						<tr>
							<td>{habitat}</td>
							<td>{geoloc}<td>
						</tr>
						<tr>
							<th>Sound:</th>
							<th><th>
						</tr>
						<tr>
							<td>{sound}</td>
							<td><td>
						</tr>
					</table>
				</td>
				<td>
					<img src={url} width="300" />
				</td>
			</tr>
		</table>
		<a href='?'>Go Back</a>'''
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

	@property
	def sounds(self):
		pass

	@sounds.setter
	def sounds(self, arr):
		self.__sounds = arr
		self.sound += arr[0]

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

	@property
	def sounds(self):
		pass

	@sounds.setter
	def sounds(self, arr):
		self.__sounds = arr
		self.sound += arr[1]

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

	@property
	def sounds(self):
		pass

	@sounds.setter
	def sounds(self, arr):
		self.__sounds = arr
		self.sound += arr[2]

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
