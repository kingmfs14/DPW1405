'''
Matthew King
05/20/2014
DPW 1405
Lab 4 What Does the Fox Say
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
