class Category:
	name = ""
	
	def __init__(self, name_1):
		self.name = name_1
		self.ledger = list()
		self.total = 0
		self.spending = 0

	def deposit(self, amount, *des):		#tiengui
		try:
			self.total += amount
			obj = {"amount":amount, "description":des[0]}
			self.ledger.append(obj)
		except:
			obj = {"amount":amount, "description":""}
			self.ledger.append(obj)

	def check_funds(self, amount):
		if amount > self.total:
			return False
		else:
			return True

	def withdraw(self, amount, *des): 	#ruttien
		if self.check_funds(amount) == False:
			return False
		else:
			self.total -= amount
			self.spending += amount
			try:
				obj = {"amount":-amount, "description":des[0]}
				self.ledger.append(obj)
			except:
				obj = {"amount":-amount, "description":""}
				self.ledger.append(obj)
			return True

	def get_balance(self):	#return sodu
		return self.total

	def transfer(self, amount, budget):
		if self.check_funds(amount) == False:
			return False
		else:
			#transfer to
			self.total -= amount
			self.spending += amount
			des_to = "Transfer to " + budget.name
			obj_to = {"amount":-amount, "description":des_to}
			self.ledger.append(obj_to)
			#transfer from
			budget.total += amount
			des_from = "Transfer from " + self.name
			obj_from = {"amount":amount, "description":des_from}
			budget.ledger.append(obj_from)
			return True

	def printf(self):
		#name
		if len(self.name)%2 != 0:
			left_star = int((30 - len(self.name))/2)
			right_star = left_star + 1
			print("*"*left_star + self.name + "*"*right_star)
		else:
			star = int((30 - len(self.name))/2)
			print("*"*star + self.name + "*"*star)
		#ledgerlist
		for i in self.ledger:
			print(format(i['description'][0:23], '23') + str(format(i['amount'], '7.2f'))[0:7])
		print("Total: " + str(format(self.total, '.2f')))
		
def creat_spend_chart(*budgets):
	#extract spending rates 
	rates = list()
	rates_end = list()
	budgets_list = list()
	for budget in budgets:
		rates.append(int(100*budget.spending/(budget.total+budget.spending)))
		budgets_list.append(budget)
	for rate in rates:
		if rate%10 >= 5:
			rates_end.append(int((rate - rate%10 + 10)/10))
		else:
			rates_end.append(int((rate - rate%10)/10))
	#sort rates & budgets
	for i in range(0, len(rates_end)-1, 1):
		for j in range(i, len(rates_end), 1):
			if rates_end[i] < rates_end[j]:
				shipper = rates_end[i]
				rates_end[i] = rates_end[j]
				rates_end[j] = shipper
				shipper = budgets_list[i]
				budgets_list[i] = budgets_list[j]
				budgets_list[j] = shipper
	#display on screen
	print("Percentage spent by category")
	a = list()
	k = 0
	for i in range(100, -1, -10):
		a.append(str(format(i, '3')) + "|")
		for j in range(len(rates_end)):
			if rates_end[j]*10 >= i:
				a[k] += " "*2 + "o"
		k += 1
	for i in a:
		print(i)
	print(" "*4 + "-"*3*len(budgets_list) + "-"*2)
	b = list()
	max_name = 0
	for budget in budgets_list:
		if len(budget.name) > max_name:
			max_name = len(budget.name)
	for i in range(max_name):
		b.append(" "*4)
	for budget in budgets_list:
		for i in range(max_name):
			if len(budget.name) >= i+1:
				b[i] += " "*2 + budget.name[i]
			else:
				b[i] += " "*3
	for i in b:
		print(i)

#instant
food = Category("Food")
food.deposit(1000, "initial deposit")
clothing = Category("Clothing")
auto = Category("Auto")
auto.deposit(500, "initial deposit")
auto.withdraw(499, "buy house")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
food.transfer(500, clothing)
clothing.transfer(100, auto)
food.printf()
clothing.printf()
auto.printf()
creat_spend_chart(food, clothing, auto)
input()