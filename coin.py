import random
from tkinter import *

BB = '\u265D'
BN = '\u265E'
BR = '\u265C'

COIN_LIST = [BB, BN, BR]

coin_field_button_1 = None
coin_field_button_2 = None

tk = None

def initTk(parentTk):
	tk = parentTk

def removeCoinIfExist(coin_button, button_list):
	if coin_button:
		button_list.append(coin_button)
		if coin_button["fg"] == "orange":
			coin_button.config(text= "")


def isCoinOnField(field_button):
	return field_button == coin_field_button_1 or field_button == coin_field_button_2

def setColorOnCoinField(field_button):
	field_button.config(fg = "orange")

def clearColorOnCoinField(field_button):
	field_button.config(fg = "black")

def getButtonPosition(button):
	x = button.grid_info()["row"]-1
	y = button.grid_info()["column"]-1
	position = x, y
	return position
	
def placeCoin(button_list, players_pos_list, endbutton_pos, coinText, coin_button):
	removeCoinIfExist(coin_button, button_list)
	
	# find an empty field to place the coin		
	while True:
		coin_button = random.choice(button_list)
		coin_pos = getButtonPosition(coin_button)
		if coin_pos not in players_pos_list and coin_pos != endbutton_pos:
			button_list.remove(coin_button)
			coin_button.config(text=coinText, fg = "orange")
			break
		
	print("COIN BUTTON", coin_button)
	print("COIN COORDS", coin_pos)
	return coin_button

def placeCoin1(button_list, players_pos_list, endbutton_pos):
  global coin_field_button_1
  coin_symbol = random.choice(COIN_LIST)
  coin_field_button_1 = placeCoin(button_list, players_pos_list, endbutton_pos, coin_symbol, coin_field_button_1)


def placeCoin2(button_list, players_pos_list, endbutton_pos):
  global coin_field_button_2
  coin_symbol = random.choice(COIN_LIST)
  coin_field_button_2 = placeCoin(button_list, players_pos_list, endbutton_pos, coin_symbol, coin_field_button_2)


def isCoin1Played(endbutton):
	return endbutton == coin_field_button_1


def isCoin2Played(endbutton):
	return endbutton == coin_field_button_2


# Turns the piece that stepped on the coin into a new piece that is resembled on the coin
#
# endbutton_text: the current name of the end button
# player_color: "B" for black, "W" fot white
# figure:
# returns: the new name of the end button
#
def setCoin(endbutton_text, player_color, figure):
	WB = '\u2657'
	WN = '\u2658'
	WR = '\u2656'
	if player_color == 'B':
		if endbutton_text == BB:
			figure.name = 'BL'
			return BB
		if endbutton_text == BN:
			figure.name = 'BS'
			return BN
		if endbutton_text == BR:
			figure.name = 'BT'
			return BR
	elif player_color == 'W':
		if endbutton_text == BB:
			figure.name = 'WL'
			return WB
		if endbutton_text == BN:
			figure.name = 'WS'
			return WN
		if endbutton_text == BR:
			figure.name = 'WT'
			return WR

def setCoin1(endbutton_text, player_color, figure):	
	print("setCoin1")
	return setCoin(endbutton_text, player_color, figure)

def setCoin2(endbutton_text, player_color, figure):	
	print("setCoin2")
	return setCoin(endbutton_text, player_color, figure)
