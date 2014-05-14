'''
Matthew King
05/13/2014
DPW 1405
Lab 2 Server Side Form
'''

import webapp2 

class MainHandler(webapp2.RequestHandler):
    def get(self): 
    	page_head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>Profile Information Form</title>
	</head>
	<body>'''	

	page_close = '''</body>
</html>
        '''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
