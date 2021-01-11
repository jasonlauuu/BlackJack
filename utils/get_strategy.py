#This util module defines a strategy importer for computer player.
#Import csv to convert a csv strategy to a hashmap
#Current strategy version: from wikipedia
"""
Class
------
Player
    attribute:
		hard_strategy: without ace
		soft_strategy: with
		pair_strategy: card split
    method:
        import_computer_strategy: mapping key= current hand&dealer hand -> value= one strategy from{hit stand double surrender split}

"""
import csv
class Computer_Strategy:
	hard_strategy = {}
	soft_strategy = {}
	pair_strategy = {}

	def __init__(self, file):
		self.file = file

	def import_computer_strategy(self):
		hard = 21
		soft = 21
		pair = 20

		with open(self.file) as strategy_csv:
			reader = csv.DictReader(strategy_csv, delimiter = ';')
			for row in reader:
				if hard >= 5:
					self.hard_strategy[hard] = row
					hard -= 1 
				elif soft >= 12:
					self.soft_strategy[soft] = row
					soft -= 1
				elif pair >= 4:
					self.pair_strategy[pair] = row
					pair -= 2

		return self.hard_strategy, self.soft_strategy, self.pair_strategy