import urllib2 #python classes and code needed to request info, receive, and open
import json

class AlbumView(object):
	"""This class handles how the data is shown to the user"""
	def __init__(self):
		self.__wdos = []
		self.__content = '''<table>
			<tr>
				<td><h3>Albums</h3></td>
			</tr>
		'''

	def update(self):
		count = 0
		for do in self.__wdos:
			remainder = count % 4
			if remainder == 0: 
				self.__content += '<tr>'
				self.__content += '<td><img src="' + do.cover + '" /><br>'
				self.__content += '<h4>' + do.album + '</h4>'
				self.__content +=  '<p>' + do.artist + '</p></td>'
				count += 1
			elif remainder == 3:
				self.__content += '<td><img src="' + do.cover + '" /><br>'
				self.__content += '<h4>' + do.album + '</h4>'
				self.__content +=  '<p>' + do.artist + '</p></td>'
				self.__content += '</tr>'
				count += 1
			else:
				self.__content += '<td><img src="' + do.cover + '" /><br>'
				self.__content += '<h4>' + do.album + '</h4>'
				self.__content +=  '<p>' + do.artist + '</p></td>'
				count += 1
			
		self.__content += '</table>'


	@property
	def content(self):
		return self.__content

	@property
	def wdos(self):
		pass

	@wdos.setter
	def wdos(self, arr):
		self.__wdos = arr
		self.update()

class AlbumModel(object):
	"""This model handles fetching, parsing, and sorting data from Itunes API"""	        
	def __init__(self):
		self.__url = 'https://itunes.apple.com/search?'
		self.__term = ''
		self.__entity = '&entity=album'
		self.__attr = '&attribute=albumTerm'
		self.__limit = '&limit=200'
		self.__jsondoc = ''

	def callApi(self):
		#REQUESTS AND LOADS INFO FROM API
		#assemble the request
		request = urllib2.Request(self.__url + self.__term + self.__entity + self.__attr + self.__limit)
		#use urllib2 to create and object to get the url
		opener = urllib2.build_opener()
		#use the url to get a result - request info from API
		result = opener.open(request)

		#PARSING DATA
		self.__jsondoc = json.load(result)

		#SORTING DATA
		list = self.__jsondoc['results']
		self._dos = []
		for tag in list:
			do = ItunesData()
			do.artist = tag['artistName']
			do.album = tag['collectionName']
			do.cover = tag['artworkUrl100']
			self._dos.append(do)

	@property
	def dos(self):
		return self._dos

	@property	
	def term(self):
		pass

	@term.setter
	def term(self, t):
		self.__term = t	

class ItunesData(object):
	"""this data object holds the data fetched by the model and shown by the view"""
	def __init__(self):
		self.artist = ''
		self.album = ''
		self.cover = ''
