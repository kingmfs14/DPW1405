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


