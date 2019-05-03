import pytest
from playerclass import *

def test_total_01():
	hand = ["A","A","A","A"]
	assert total(hand) == 14

def test_total_02():
	hand = ["J","Q"]
	assert total(hand) == 20

def test_total_03():
	hand = ["A","A"]
	assert total(hand) == 12

def test_total_04():
	hand = [10,"A"]
	assert total(hand) == 21

def test_total_05():
	hand = ["J","Q","A"]
	assert total(hand) == 21

def test_total_06():
	hand = ["K","A","A",9]
	assert total(hand) == 21

def test_total_07():
	hand = ["Q","A","A",9]
	assert total(hand) == 21

def test_total_08():
	hand = ["J","A","A",9]
	assert total(hand) == 21

def test_total_09():
	hand = ["A","A"]
	assert total(hand) == 12

def test_total_10():
	hand = ["A","A",9]
	assert total(hand) == 21

