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
		<title>{title}</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" />
	</head>
	<body>'''	

	page_form = '''<h1>Enter Your Profile Information Below</h1>
		<form method="GET">
			<p>
				<label>First Name: </label><input type="text" name="f_name" style="width:290px;" />
				<label>Last Name: </label><input type="text" name="l_name" style="width:290px;" />
			</p>
			<p>
				<label>Email: </label><input type="text" name="email" style="width:290px;" />
				<label>Phone: </label><input type="text" name="phone" style="width:290px;" />
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
			<p>
				<label>Additional Information: </label><textarea name="info" style="width:390px;"></textarea>
			</p>
			<input type="submit" value="Submit" />
		</form>'''

	page_info = '''<p>Aloha! Mahalo for taking the time to fill out our form. Please verify that your information is correct.</p>
		<table>
			<tr>
				<th>First Name</th>
				<td>{f_name}<td>
			</tr>
			<tr>
				<th>Last Name</th>
				<td>{l_name}<td>
			</tr>
			<tr>
				<th>Phone Number</th>
				<td>{phone}<td>
			</tr>
			<tr>
				<th>Email Address</th>
				<td>{email}<td>
			</tr>
			<tr>
				<th>Contact By</th>
				<td>{contact}<td>
			</tr>
			<tr>
				<th>Expert In</th>
				<td>{expertise}<td>
			</tr>
			<tr>
				<th>Additional Information</th>
				<td>{info}<td>
			</tr>
		</table>
	'''

	page_close = '''</body>
</html>
        '''

        if self.request.GET:
        	title = 'Your Profile Information'
        	f_name = self.request.GET['f_name']
        	l_name = self.request.GET['l_name']
        	email = self.request.GET['email']
        	phone = self.request.GET['phone']
        	contact = self.request.GET['contact']
        	expertise = self.request.GET.getall('expertise')
        	info = self.request.GET['info']
        	page_info = page_info.format(**locals())
        	page_head = page_head.format(**locals())
        	self.response.write(page_head + page_info + page_close)
        else:
        	title = 'Profile Information Form'
        	page_head = page_head.format(**locals())
        	self.response.write(page_head + page_form + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
