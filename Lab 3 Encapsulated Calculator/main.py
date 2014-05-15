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

    	a = Loan()
    	a.name = 'Allen'
    	a.amount = 6000
    	a.years = 10
    	a.interest_rate = 6.8
    	a.calc_payment()
    	a.calc_interest()
    	a.calc_cost()

    	b = Loan()
    	b.name = 'Bob'
    	b.amount = 7000
    	b.years = 2.25
    	b.interest_rate = 6.8
    	b.calc_payment()
    	b.calc_interest()
    	b.calc_cost()

    	c = Loan()
    	c.name = 'Christie'
    	c.amount = 4500
    	c.years = 7
    	c.interest_rate = 5.5
    	c.calc_payment()
    	c.calc_interest()
    	c.calc_cost()

    	d = Loan()
    	d.name = 'David'
    	d.amount = 9000
    	d.years = 3
    	d.interest_rate = 5.5
    	d.calc_payment()
    	d.calc_interest()
    	d.calc_cost()

    	e = Loan()
    	e.name = 'Elizabeth'
    	e.amount = 10000
    	e.years = 12
    	e.interest_rate = 3.4
    	e.calc_payment()
    	e.calc_interest()
    	e.calc_cost()

    	f = Loan()
    	f.name = 'Francis'
    	f.amount = 10000
    	f.years = 5
    	f.interest_rate = 3.4
    	f.calc_payment()
    	f.calc_interest()
    	f.calc_cost()

    	g = Loan()
    	g.name = 'Gesen'
    	g.amount = 100000
    	g.years = 8
    	g.interest_rate = 6.7
    	g.calc_payment()
    	g.calc_interest()
    	g.calc_cost()

    	page_head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>{title}</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" />
	</head>
	<body>'''	

	page_home = '''
		'''

	page_close = '''</body>
</html>'''

        if self.request.GET:
        	pass
        else:
        	title = 'Put Off Your Loans?'
        	page_head = page_head.format(**locals())
        	self.response.write(page_head + page_home + page_close)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
