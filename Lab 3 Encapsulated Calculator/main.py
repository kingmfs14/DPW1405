'''
Matthew King
05/14/2014
DPW 1405
Lab 3 Encapsulated Calculator
'''

import webapp2 
from loans import Loan

class MainHandler(webapp2.RequestHandler):
    def get(self): 


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
