class player:

	def __init__ (self, name, password, money,line_posi):
		self.name=name
		self.password=password
		self.money=money
		self.line_posi = line_posi
		##line position starts at 0

	def getLine_posi(self):
		return self.line_posi

	def getBalance(self):
		return self.money
	def getName(self):
		return self.name

	def getPassword(self):
		return self.password

	def changename(self,newname):
		self.name=newname
		return self.name

	def changepassword(self,newpassword):
		self.password=newpassword
		return self.password

	def showinfo(self):
		print "Name : ", self.name, ", Balance : ", self.money

	def checkpassword(self):
		print self.password

	def winmoney(self,betamount):
		self.money+=betamount
		return self.money

	def losemoney(self,betamount):
		self.money=self.money-betamount
		return self.money

if __name__ == "__main__":
	player1=player("alex","alex123",500)
	player1.showinfo()
	player1.checkpassword()
	player1.changename("alice")
	player1.changepassword("alice123")
	player1.winmoney(10)
	player1.showinfo()
	player1.checkpassword()