import pytest
from playerclass import *

def test_total_01():
	hand = [2,4]
	assert total(hand) == 6

def test_total_02():
	hand = [4,8]
	assert total(hand) == 12

def test_total_03():
	hand = ["J",4]
	assert total(hand) == 14

def test_total_04():
	hand = ["J","A"]
	assert total(hand) == 21

def test_total_05():
	hand = ["Q","A"]
	assert total(hand) == 21

def test_total_06():
	hand = ["K","A"]
	assert total(hand) == 21

def test_total_07():
	hand = ["A","A"]
	assert total(hand) == 12

def test_total_08():
	hand = ["A",2]
	assert total(hand) == 13

def test_total_09():
	hand = [10,"J"]
	assert total(hand) == 20

def test_total_10():
	hand = [2,4,"J"]
	assert total(hand) == 16

def test_total_11():
	hand = ["J",4,"A"]
	assert total(hand) == 15

def test_total_12():
	hand = ["J",3,"A"]
	assert total(hand) == 14

def test_total_13():
	hand = ["Q","A",2]
	assert total(hand) == 23

def test_total_14():
	hand = ["K","J","A"]
	assert total(hand) == 21

def test_total_15():
	hand = ["A","A","A"]
	assert total(hand) == 13

def test_total_16():
	hand = ["A",2,"K"]
	assert total(hand) == 23

def test_total_17():
	hand = [10,"J","A"]
	assert total(hand) == 21