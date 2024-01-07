import random
from tkinter import *


tk = None

bomb_list = []
BOMB_SYMBOL = "\U0001F4A3"
BOMB_ROUNDS = 3

# Represents a Bomb on the table
class Bomb:
	def __init__(self, button, label, isSet, rounds, button_list):
		self.button = button
		self.label = label
		self.isSet = isSet
		self.rounds = rounds
		self.button_list = button_list

	def decreaseRounds(self):
		if self.isSet:
			self.rounds-=1
			self.label.config(text = self.rounds)

	def removeIfNotSet(self):
		if self.isSet == False:
			self.button.config(text= "") 
			self.button_list.append(self.button)
			

	def set(self, rounds):
		global tk
		self.isSet = True
		self.rounds = rounds
		self.label = Label(tk, text = rounds, fg = "white", bg = "black")
		self.label.grid(row = self.button.grid_info()["row"], column = self.button.grid_info()["column"])
		print("Bomb set at position: ", self.button.grid_info()["row"] - 1,  ", ", self.button.grid_info()["column"] - 1)

	def destroy(self):
		self.label.destroy()



def initTk(parentTk):
	tk = parentTk
	

def decreaseRounds():
	global bomb_list
	for bomb in bomb_list:
		bomb.decreaseRounds()


def isBombOnField(field_button):
	global bomb_list
	for bomb in bomb_list:
		if field_button == bomb.button:
			return True
	return False


def setColorOnBombField(field_button):
	field_button.config(fg = "green")

def clearColorOnBombField(field_button):
	field_button.config(fg = "black")


# if the destination field and bomb field are the same
# let the player know that he picked up a bomb
def setActionLabel(endbutton, action_label):
	global bomb_list
	for bomb in bomb_list:
		if endbutton == bomb.button:
			action_label.config(text = "YOU PICKED UP A BOMB!", fg = "black")
			return
		

def removeAllBombsIfNotSet():
	global bomb_list
	for bomb in bomb_list:
		bomb.removeIfNotSet()

	bomb_list = list(filter(lambda b: b.isSet, bomb_list))


def getButtonPosition(button):
	x = button.grid_info()["row"]-1
	y = button.grid_info()["column"]-1
	position = x, y
	return position


def placeBomb(button_list, players_pos_list, endbutton_pos):
	# find an empty field to place the bomb		
	while True:
		bomb_button = random.choice(button_list)
		bomb_pos = getButtonPosition(bomb_button)
		if bomb_pos not in players_pos_list and bomb_pos != endbutton_pos:
			button_list.remove(bomb_button)
			# bomb_button is the randomly selected button, that we will place our bomb item on
			# we visualize our bomb by editing the buttons text to the bomb symbol
			bomb_button.config(text=BOMB_SYMBOL, fg = "green") 
			break
		
	print("BOMB BUTTON", bomb_button)
	print("BOMB COORDS", bomb_pos)
	return bomb_button


def placeBomb1(button_list, players_pos_list, endbutton_pos):
	global bomb_list
	bomb_button = placeBomb(button_list, players_pos_list, endbutton_pos)
	bomb = Bomb(bomb_button, None, False, BOMB_ROUNDS, button_list)
	bomb_list.append(bomb)


def placeBomb2(button_list, players_pos_list, endbutton_pos):
	placeBomb1(button_list, players_pos_list, endbutton_pos)


def obtainBombPosition(button):
		bomb_row = button.grid_info()["row"]
		new_bomb_row = bomb_row-1
		bomb_col = button.grid_info()["column"]
		new_bomb_col = bomb_col-1
		return (new_bomb_row, new_bomb_col)


def setBombCellColors(button_list, row, col):
	#print("setBombCellColors ", row, col)	
	# set color of 3x3 cells around (row, col) to black
	for r in range(max(0, row-1), min(8, row+2)):
		for c in range(max(0, col-1), min(8, col+2)):
			#print("loop ", r, c)
			button_list[r][c].config(bg = "black")
	return


def resetBombCellColors(button_list, row, col):
	#print("resetBombCellColors ", row, col)	
	# restore color of 3x3 cells around (row, col)
	explodePositions = []
	for r in range(max(0, row-1), min(8, row+2)):
		for c in range(max(0, col-1), min(8, col+2)):
			explodePositions.append((r,c))
			if (r + c) % 2 == 1:
				button_list[r][c].config(bg = "gray")  
			else:	
				button_list[r][c].config(bg = "white")
	return explodePositions


def setBombIfPlayerSteppedOnBombField(button_list, endbutton):
	global bomb_list
	for bomb in bomb_list:	
		if endbutton == bomb.button:
			bomb.set(BOMB_ROUNDS)
			bomb_pos = obtainBombPosition(endbutton)
			setBombCellColors(button_list, bomb_pos[0], bomb_pos[1])
			return


def explodeBombIfTimerExpired(button_list):
	global bomb_list
	for bomb in bomb_list:	
		if bomb.isSet and bomb.rounds == 0:
			bomb_pos = obtainBombPosition(bomb.button)
			bomb.destroy()
			bomb_list.remove(bomb)
			# reset color of cells around bomb (to white or grey)
			return resetBombCellColors(button_list, bomb_pos[0], bomb_pos[1])

