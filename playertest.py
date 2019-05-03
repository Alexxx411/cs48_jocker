import unittest
from playerclass import *


class testPlayerClass(unittest.TestCase):

	#testPlayer=player("Alex","alex123",500)

	def test_name(self):
		self.assertEqual("Alex",testPlayer.name)

	def test_password(self):
		self.assertEqual("alex123",testPlayer.password)

	def test_money(self):
		self.assertEqual(500,testPlayer.money)

	testPlayer=player("Alex","alex123",500)
	#testPlayer.changename("Alice")
	#testPlayer.changepassword("alice123")
	#testPlayer.getmoney(10)

	def test_changename(self):
		self.testPlayer.changename("Alice")
		self.assertEqual("Alice",self.testPlayer.name)

	def test_changepassword(self):
		self.testPlayer.changepassword("alice123")
		self.assertEqual("alice123",self.testPlayer.password)

	def test_getmoney(self):
		self.testPlayer.getmoney(10)
		self.assertEqual(510,self.testPlayer.money)

	def test_losemoney(self):
		self.testPlayer.losemoney(20)
		self.assertEqual(490,self.testPlayer.money)
			

if __name__=='__main__':
	testPlayer=player("Alex","alex123",500)
	#testPlayer.showinfo()
	unittest.main()