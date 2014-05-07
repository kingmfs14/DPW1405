'''
Matthew King
05/07/2014
DPW
Simple Login Follow Along
'''


import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Catalyst
        about_button = Button()
        about_button.label = 'About Us'
        about_button.show_label()
        #about_button.click()
        contact_button = Button()
        contact_button.label = 'Contact Us'
        contact_button.show_label()

class Button(object):
	def __init__(self):
		print 'constructor method of button ran'
		self.label = '' #public attribute
		self.__size = 60 #private attribute - two underscores
		self._color = '0x00000' #protected attribute - one underscore
		#self.click()
		#self.on_roll_over('Hello!!')

	def click(self):
		print "I've been clicked"

	def on_roll_over(self, message):
		print "You've rolled over my button" + message

	def show_label(self):
		print 'My label is ' + self.label

#never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
