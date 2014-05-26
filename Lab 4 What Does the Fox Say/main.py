'''
Matthew King
05/20/2014
DPW 1405
Lab 4 What Does the Fox Say
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self): #function that starts everything
    	pass
   	
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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
