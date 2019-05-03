class player:

	def __init__ (self, name, password, money):
		self.name=name
		self.password=password
		self.money=money

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

	def getmoney(self,amount):
		self.money+=amount
		return self.money

	def losemoney(self,amount):
		self.money-=amount
		return self.money

if __name__ == "__main__":
	player1=player("alex","alex123",500)
	player1.showinfo()
	player1.checkpassword()
	player1.changename("alice")
	player1.changepassword("alice123")
	player1.getmoney(10)
	player1.showinfo()
	player1.checkpassword()