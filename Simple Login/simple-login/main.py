'''
Matthew King
05/12/2014
DPW
Simple Login
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Catalyst
    	page_head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>Simple Form</title>
	</head>
	<body>'''	

	page_body = '''<form method="GET">
			<label>Name: </label><input type="text" name="user" />
			<label>Email: </label><input type="text" name="email" />
			<input type="submit" value="Submit" />'''

	page_body = '''<a href="?email=mickey@disney.com&user=Mickey">Click Here if your email is mickey@disney.com</a><br>
			<a href="?email=donald@disney.com&user=Donald">Click Here if your email is donald@disney.com</a><br>
			<a href="?email=pluto@disney.com&user=Pluto">Click Here if your email is pluto@disney.com</a><br>
			<a href="?email=goofy@disney.com&user=Goofy">Click Here if your email is goofy@disney.com</a><br>
	'''

	page_close = '''</form>
	</body>
</html>
        '''
        if self.request.GET:
        	user = self.request.GET['user']
        	email = self.request.GET['email']
        	self.response.write(page_head + user + ' ' + email + ' ' + page_close) #PRINT
        else:
        	self.response.write(page_head + page_body + page_close) #PRINT

#never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
