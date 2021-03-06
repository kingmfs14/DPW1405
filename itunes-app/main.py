 
import webapp2
from album import AlbumModel
from album import AlbumView

class MainHandler(webapp2.RequestHandler):
	def get(self):
		f = FormPage()
		f.inputs = [['term', 'text', 'Album Keyword']] #form inputs
		title = 'iTunes Album Search Application' #home page title

		if self.request.GET: #only if the user searches
			title = 'Showing results for "' + self.request.GET['term'] +'"'
			term = 'term=' #creates paramaters needed for API
			am = AlbumModel() #creates our model
			term += self.request.GET['term'] #grabs term and adds it parameter
			am.term = term.replace(' ', '+') #sends term from the URL to our model
			am.callApi() #tells it to connect to the API

			av = AlbumView() #creates our view
			av.wdos = am.dos #takes data objects from model class and give them to view

			f._body = '<h2>Showing results for "' + self.request.GET['term'] +'"</h2>' #creates heading for page
			f._body += av.content #adds information from album file to page

		p = f.print_out() #call print_out function
		p = p.format(**locals()) #create dynamic content
		self.response.write(p) #write information in HTML format

class Page(object): #borrowing stuff from the object class ABSTRACT CLASS
	def __init__(self): #constructor
		self._head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>{title}</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" />
	</head>
	<body>'''
		#create a navigation to specify search request type
		self._body = ''
		self._close = '''</body>
</html>'''	
	
	def print_out(self):
		return self._head + self._body + self._close

class FormPage(Page):	
	def __init__(self):
		#constructor for the super class
		#Page.__init__()
		super(FormPage, self).__init__()
		self.__inputs = []
		self._body = '''<h1>What Album are you Looking for?</h1>
		<form method="GET">''' #start of form 

	@property
	def inputs(self):
		pass

	@inputs.setter
	def inputs(self, arr):
		#change my private inputs variable
		self.__inputs = arr
		#adding text input
		for item in arr:
			self._body += '<input type="' + item[1] + '" name="' + item[0]
			#if there is a third item... add it in...
			try:
				self._body += '" placeholder="' + item[2] + '" /> <br>'
			#otherwise... end the tag
			except:
				self._body += '" /> <br>'

		self._body += '</form>' #ending of form

	def print_out(self):
		return self._head + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
