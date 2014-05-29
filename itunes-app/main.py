 
import webapp2
import urllib2 #python classes and code needed to request info, receive, and open
import json

class MainHandler(webapp2.RequestHandler):
	def get(self):
		p = FormPage()
		p.inputs = [['term', 'text', 'Song Name or Artist'],['Submit', 'submit']]
		self.response.write(p.print_out())

		if self.request.GET:
			#get info from API
			term = 'term='
			term += self.request.GET['term']
			term = term.replace(' ', '+')
			limit = '&limit=200'
			url = 'https://itunes.apple.com/search?' + term + limit
			#assemble the request
			request = urllib2.Request(url)
			#use urllib2 to create and object to get the url
			opener = urllib2.build_opener()
			#use the url to get a result - request info from API
			result = opener.open(request)

			print result

			#parsing with JSON
			# jsondoc = json.load(result)
			# print jsondoc

			# results = jsondoc['results']
			# name = results[0]['artistName']
			# cd = results[0]['collectionName']

			# self.response.write("You're Artist Name: "+name+'<br> Their first album: '+cd)

class Page(object): #borrowing stuff from the object class ABSTRACT CLASS
	def __init__(self): #constructor
		self._head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title></title>
	</head>
	<body>'''

		self._body = 'Itunes Search'
		self._close = '''</body>
</html>'''	
	
	def print_out(self):
		return self._head + self._body + self._close

class FormPage(Page):	
	def __init__(self):
		#constructor for the super class
		#Page.__init__()
		super(FormPage, self).__init__()
		self._form_open = '<form method="GET">'
		self._form_close = '</form>'
		self.__inputs = []
		self._form_inputs = ''

	@property
	def inputs(self):
		pass

	@inputs.setter
	def inputs(self, arr):
		#change my private inputs variable
		self.__inputs = arr
		#sort through the mega array and create HTML inputs based on the info there.
		for item in arr:
			self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
			#if there is a third item... add it in...
			try:
				self._form_inputs += '" placeholder="' + item[2] + '" /> <br>'
			#otherwise... end the tag
			except:
				self._form_inputs += '" /> <br>'

	#POLYMORPHISM ALERT!!!-----METHOD OVERRIDE
	def print_out(self):
		return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
