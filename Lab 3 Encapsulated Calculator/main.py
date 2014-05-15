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

	page_home = '''<h1>Think Again About Putting Off Paying Off Your Loans...</h1>
		<p>Take a look at these different student loans from friends of mine. You will be surprised at what shocking information you find out. The amount of the loan, interest rate, and length of loan dramatically plays a role in a higher cost for getting a higher education. Click on any of the below links and you will look at their individual loan situations.</p>
		<ul>
			<li><a href="?name={a.name}&amount={a.amount}&years={a.years}&interest_rate={a.interest_rate}&payment={a.payment}&interest={a.interest}&total_cost={a.total_cost}">{a.name}'s $6,000 loan</a></li>
			<li><a href="?name={b.name}&amount={b.amount}&years={b.years}&interest_rate={b.interest_rate}&payment={b.payment}&interest={b.interest}&total_cost={b.total_cost}">{b.name}'s $7,000 loan</a></li>
			<li><a href="?name={c.name}&amount={c.amount}&years={c.years}&interest_rate={c.interest_rate}&payment={c.payment}&interest={c.interest}&total_cost={c.total_cost}">{c.name}'s $4,500 loan</a></li>
			<li><a href="?name={d.name}&amount={d.amount}&years={d.years}&interest_rate={d.interest_rate}&payment={d.payment}&interest={d.interest}&total_cost={d.total_cost}">{d.name}'s $9,000 loan</a></li>
			<li><a href="?name={e.name}&amount={e.amount}&years={e.years}&interest_rate={e.interest_rate}&payment={e.payment}&interest={e.interest}&total_cost={e.total_cost}">{e.name}'s $10,000 loan</a></li>
			<li><a href="?name={f.name}&amount={f.amount}&years={f.years}&interest_rate={f.interest_rate}&payment={f.payment}&interest={f.interest}&total_cost={f.total_cost}">{f.name}'s $10,000 loan</a></li>
			<li><a href="?name={g.name}&amount={g.amount}&years={g.years}&interest_rate={g.interest_rate}&payment={g.payment}&interest={g.interest}&total_cost={g.total_cost}">{g.name}'s $100,000 loan</a></li>
		</ul>
		'''

	page_info = '''<p>Look at what {name} paid on their loan!</p>
		<table>
			<tr>
				<th>Loaned Amount</th>
				<td>${amount}<td>
			</tr>
			<tr>
				<th>Interest Rate</th>
				<td>{interest_rate}%<td>
			</tr>
			<tr>
				<th>Length of Loan</th>
				<td>{years} years<td>
			</tr>
			<tr>
				<th>Monthly Payments</th>
				<td>${payment}<td>
			</tr>
			<tr>
				<th>Total Interest Paid</th>
				<td>${interest}<td>
			</tr>
			<tr>
				<th>Total Paid to the Bank</th>
				<td>${total_cost}<td>
			</tr>
		</table>
		<p><a href="?">Go Back</a></p>
	'''

	page_close = '''</body>
</html>'''

        if self.request.GET:
        	name = self.request.GET['name']
        	title = name + "'s Loan Information"
        	amount = self.request.GET['amount']
        	years = self.request.GET['years']
        	interest_rate = self.request.GET['interest_rate']
        	payment = self.request.GET['payment']
        	interest = self.request.GET['interest']
        	total_cost = self.request.GET['total_cost']
        	page_info = page_info.format(**locals())
        	page_head = page_head.format(**locals())
        	self.response.write(page_head + page_info + page_close)
        else:
        	title = 'Put Off Your Loans?'
        	page_head = page_head.format(**locals())
        	page_home = page_home.format(**locals())
        	self.response.write(page_head + page_home + page_close)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
