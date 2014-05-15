class Loan(object):
	def __init__(self):
		self.name = ''
		self.amount = 0
		self.years = 0
		self.interest_rate = 0
		self.__payment = 0
		self.__interest = 0
		self.__total_cost = 0

	@property
	def payment(self):
		return self.__payment

	@payment.setter
	def payment(self, new_payment):
		self.__payment = new_payment

	@property
	def interest(self):
		return self.__interest

	@interest.setter
	def interest(self, new_interest):
		self.__interest = new_interest

	@property
	def total_cost(self):
		return self.__total_cost

	@total_cost.setter
	def total_cost(self, new_total_cost):
		self.__total_cost = new_total_cost
