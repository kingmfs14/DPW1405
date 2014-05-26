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
