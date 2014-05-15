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

    	#Christie's Loan Information
    	c = Loan()
    	c.name = 'Christie'
    	c.amount = 4500
    	c.years = 7
    	c.interest_rate = 5.5
    	c.calc_payment()
    	c.calc_interest()
    	c.calc_cost()
    	print self.response.write("<br> Christie's Loan will have a payment of " + str(c.payment) + " a month. He will pay a total of " + str(c.total_cost) + " including " + str(c.interest) + " in interest total.")

    	#David's Loan Information
    	d = Loan()
    	d.name = 'David'
    	d.amount = 9000
    	d.years = 3
    	d.interest_rate = 5.5
    	d.calc_payment()
    	d.calc_interest()
    	d.calc_cost()
    	print self.response.write("<br> David's Loan will have a payment of " + str(d.payment) + " a month. He will pay a total of " + str(d.total_cost) + " including " + str(d.interest) + " in interest total.")

    	#Elizabeth's Loan Information
    	e = Loan()
    	e.name = 'Elizabeth'
    	e.amount = 10000
    	e.years = 12
    	e.interest_rate = 3.4
    	e.calc_payment()
    	e.calc_interest()
    	e.calc_cost()
    	print self.response.write("<br> Elizabeth's Loan will have a payment of " + str(e.payment) + " a month. He will pay a total of " + str(e.total_cost) + " including " + str(e.interest) + " in interest total.")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
