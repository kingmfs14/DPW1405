 
import webapp2
import urllib2 #python classes and code needed to request info, receive, and open
import json

class MainHandler(webapp2.RequestHandler):
	def get(self):
		p = Page()
		self.response.write(p.print_out())
		f = FormPage()
		f.inputs = [['term', 'text', 'Song Name or Artist'],['Submit', 'submit']]

		if self.request.GET:
			self.response.write(f.print_out())
			if self.request.GET['search'] is 'album':
				entity += 'album'
				attr += 'albumTerm'
			elif self.request.GET['search'] is 'artist':
				entity += 'allArtist'
				attr += 'allArtistTerm'
			else:
				entity += 'allTrack'
				attr += 'allTrackTerm'
			#get info from API
			term = 'term='
			term += self.request.GET['term']
			term = term.replace(' ', '+')
			entity = '&entity='
			attr = '&attribute='
			limit = '&limit=200'
			url = 'https://itunes.apple.com/search?' + term + entity + attr + limit
			#assemble the request
			request = urllib2.Request(url)
			#use urllib2 to create and object to get the url
			opener = urllib2.build_opener()
			#use the url to get a result - request info from API
			result = opener.open(request)

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
		<title>iTunes Search Application</title>
	</head>
	<body>'''
		#create a navigation to specify search request type
		self._body = '''<h1>What Do You Want to Search For?</h1>
		<ul>
			<li><a href='search="album"'>An Album</a></li>
			<li><a href='search="artist"'>An Artist</a></li>
			<li><a href='search="song"'>A Song</a></li>
		</ul>'''
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
		for item in arr:
			self._body += '<input type="' + item[1] + '" name="' + item[0]
			#if there is a third item... add it in...
			try:
				self._body += '" placeholder="' + item[2] + '" /> <br>'
			#otherwise... end the tag
			except:
				self._body += '" /> <br>'

		self._body += '</form>' #ending of form

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
