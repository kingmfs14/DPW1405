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
    	#Allen's Loan Information
    	a = Loan()
    	a.name = 'Allen'
    	a.amount = 6000
    	a.years = 10
    	a.interest_rate = 6.8
    	a.calc_payment()
    	a.calc_interest()
    	a.calc_cost()
    	print self.response.write("Allen's Loan will have a payment of " + str(a.payment) + " a month. He will pay a total of " + str(a.total_cost) + " including " + str(a.interest) + " in interest total.")

    	#Bob's Loan Information
    	b = Loan()
    	b.name = 'Bob'
    	b.amount = 7000
    	b.years = 2.25
    	b.interest_rate = 6.8
    	b.calc_payment()
    	b.calc_interest()
    	b.calc_cost()
    	print self.response.write("<br> Bob's Loan will have a payment of " + str(b.payment) + " a month. He will pay a total of " + str(b.total_cost) + " including " + str(b.interest) + " in interest total.")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
