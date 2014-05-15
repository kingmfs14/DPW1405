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

	def calc_payment(self):
		self.__month = self.years * 12
		self.__month = self.__month * (-1)
		self.__ir = (self.interest_rate / 100) / 12
		self.__calc = (1 + self.__ir) ** self.__month
		self.__payment = self.amount * (self.__ir / (1 - self.__calc))

	@property
	def interest(self):
		return self.__interest

	@interest.setter
	def interest(self, new_interest):
		self.__interest = new_interest

	def calc_interest(self):
		self.__month = (self.years * 12) * (-1)
		self.__ir = (self.interest_rate / 100) / 12
		self.__calc = (1 + self.__ir) ** self.__month
		self.__pay = self.amount * (self.__ir / (1 - self.__calc))
		self.__interest = ((self.__month * (-1)) * self.__pay) - self.amount

	@property
	def total_cost(self):
		return self.__total_cost

	@total_cost.setter
	def total_cost(self, new_total_cost):
		self.__total_cost = new_total_cost
