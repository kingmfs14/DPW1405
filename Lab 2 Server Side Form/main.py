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

	page_form = '''<h1>Enter Your Profile Information Below</h1>
		<form method="GET">
			<p>
				<label>First Name: </label><input type="text" name="f_name" /> <br>
				<label>Last Name: </label><input type="text" name="l_name" />
			</p>
			<p>
				<label>Email: </label><input type="text" name="email" /> <br>
				<label>Phone: </label><input type="text" name="phone" />
			</p>
			<p>
				<label>Contact by: <label>
				<select name="contact">
					<option value="phone"> Phone </option>
					<option value="email"> Email </option>
				</select>
			</p>
			<p>
				<label>Expertise: </label><br>
				<input type="checkbox" name="expertise" value="HTML5" />HTML5 
				<input type="checkbox" name="expertise" value="CSS3" />CSS3 
				<input type="checkbox" name="expertise" value="JavaScript" />JavaScript 
				<input type="checkbox" name="expertise" value="PHP" />PHP 
				<input type="checkbox" name="expertise" value="Python" />Python 
			</p>
			<input type="submit" value="Submit" />
		</form>'''

	page_close = '''</body>
</html>
        '''

        if self.request.GET:
        	pass
        else:
        	self.response.write(page_head + page_form + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
