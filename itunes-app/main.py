 
import webapp2
import urllib2 #python classes and code needed to request info, receive, and open
import json

class MainHandler(webapp2.RequestHandler):
	def get(self):
		p = FormPage()
		p.inputs = [['term', 'text', 'Song Name or Artist'],['album', 'artist', 'song'],['Submit', 'submit']]
		self.response.write(p.print_out())

		if self.request.GET:
			#get info from API
			term = 'term='
			term += self.request.GET['term']
			term = term.replace(' ', '+')
			entity = '&entity='
			attr = '&attribute='
			limit = '&limit=200'
			if self.request.GET['search'] is 'album':
				entity += 'album'
				attr += 'albumTerm'
			elif self.request.GET['search'] is 'artist':
				entity += 'allArtist'
				attr += 'allArtistTerm'
			else:
				entity += 'allTrack'
				attr += 'allTrackTerm'
			url = 'https://itunes.apple.com/search?' + term + entity + attr + limit
			#assemble the request
			request = urllib2.Request(url)
			#use urllib2 to create and object to get the url
			opener = urllib2.build_opener()
			#use the url to get a result - request info from API
			result = opener.open(request)

			print result

			#parsing with JSON
			jsondoc = json.load(result)

			results = jsondoc['results']
			name = results[0]['artistName']
			cd = results[0]['collectionName']
			print jsondoc

			self.response.write("You're Artist Name: "+name+'<br> Their first album: '+cd)

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
		self.__inputs = []
		self._body += '<form method="GET">' #start of form 

	@property
	def inputs(self):
		pass

	@inputs.setter
	def inputs(self, arr):
		#change my private inputs variable
		self.__inputs = arr
		#adding text input
		self._body += '<input type="' + arr[0][1] + '" name="' + arr[0][0] + '" placeholder="' + arr[0][2] + '" /> <br>'
		#adding select option for user
		self._body += '<select name="search"><option value="' + arr[1][0] + '">'+arr[1][0]+'</option><option value="' + arr[1][1] + '">'+arr[1][1]+'</option><option value="' + arr[1][2] + '">'+arr[1][2]+'</option></select> <br>'
		#adding submit button
		self._body += '<input type="' + arr[2][1] + '" name="' + arr[2][0] + '" /> <br>'
		self._body += '</form>' #ending of form

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
