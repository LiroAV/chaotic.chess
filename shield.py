import random
from tkinter import *

SHIELD_1 = 	u"\U0001F6E1"
SHIELD_2 =  u"\U0001F6E1"

shield_1_rounds = 3
shield_2_rounds = 3

is_shield_1_set = False
is_shield_2_set = False

shield_field_button_1 = None
shield_field_button_2 = None

shield_1_counter_label = None
shield_2_counter_label = None

tk = None

def initTk(parentTk):
	tk = parentTk
	
def decreaseRounds():
	global shield_1_rounds, shield_2_rounds
	shield_1_rounds -=1
	shield_2_rounds -=1

def setActionLabel(endbutton_text, action_label):
  if endbutton_text == SHIELD_1 or endbutton_text == SHIELD_2:
    action_label.config(text = "A SHIELD IS PROTECTING YOU!", fg = "red")

def appendRoundsLabel(rounds_label):
	rounds_label["text"] += ", Shield rounds: " + str(shield_1_rounds)

def removeShieldIfExist(shield_button, button_list):
	if shield_button:
		button_list.append(shield_button)
		if shield_button["fg"] == "red":
			clearColorOnShieldField(shield_button)
			button_text = shield_button["text"]
			if button_text == SHIELD_1:
				shield_button["text"] = ''
			elif len(button_text) > 0:
				shield_button["text"] = button_text[0]


def isShieldOnField(field_button):
	return field_button == shield_field_button_1 or field_button == shield_field_button_2

def setColorOnShieldField(field_button):
	field_button.config(fg = "red")

def clearColorOnShieldField(field_button):
	field_button.config(fg = "black")

def getButtonPosition(button):
	x = button.grid_info()["row"]-1
	y = button.grid_info()["column"]-1
	position = x, y
	return position

def placeShield(button_list, players_pos_list, endbutton_pos, shieldText, shield_button):
	removeShieldIfExist(shield_button, button_list)
	
	# find an empty field to place the shield		
	while True:
		shield_button = random.choice(button_list)
		shield_pos = getButtonPosition(shield_button)
		if shield_pos not in players_pos_list and shield_pos != endbutton_pos:
			button_list.remove(shield_button)
			shield_button.config(text=shieldText, fg = "red")
			break
		
	print("SHIELD BUTTON", shield_button)
	print("SHIELD COORDS", shield_pos)
	return shield_button

def placeShield1(button_list, players_pos_list, endbutton_pos):
	global shield_field_button_1, shield_1_rounds
	shield_1_rounds = 4
	removePieceFromShield1()
	shield_field_button_1 = placeShield(button_list, players_pos_list, endbutton_pos, SHIELD_1, shield_field_button_1)
	
def placeShield2(button_list, players_pos_list, endbutton_pos):
	global shield_field_button_2, shield_2_rounds
	shield_2_rounds = 4
	removePieceFromShield2()
	shield_field_button_2 = placeShield(button_list, players_pos_list, endbutton_pos, SHIELD_2, shield_field_button_2)

def isShield1Set(endbuttonPosition):
	global is_shield_1_set
	return is_shield_1_set and endbuttonPosition == getButtonPosition(shield_field_button_1)

def isShield2Set(endbuttonPosition):
	global is_shield_2_set
	return is_shield_2_set and endbuttonPosition == getButtonPosition(shield_field_button_2)

def isShield1Played(endbutton):
	return endbutton == shield_field_button_1

def isShield2Played(endbutton):
	return endbutton == shield_field_button_2

def hasSteppedAwayFromShield1(startbutton):
	return startbutton == shield_field_button_1

def hasSteppedAwayFromShield2(startbutton):
	return startbutton == shield_field_button_2

def removePieceFromShield1():
	global shield_1_counter_label, is_shield_1_set
	if shield_1_counter_label:
		shield_1_counter_label.destroy()
	is_shield_1_set = False

def removePieceFromShield2():
	global shield_2_counter_label, is_shield_2_set
	if shield_2_counter_label:
		shield_2_counter_label.destroy()
	is_shield_2_set = False	

def setShield1(endbutton, startbutton_text, endbutton_text):
	global shield_1_counter_label, is_shield_1_set
	shield_1_counter_label = Label(tk, text = startbutton_text + " " + endbutton_text)
	shield_1_counter_label.grid(row = endbutton.grid_info()["row"], column = endbutton.grid_info()["column"])
	is_shield_1_set = True

def setShield2(endbutton, startbutton_text, endbutton_text):
	global shield_2_counter_label, is_shield_2_set
	shield_2_counter_label = Label(tk, text = startbutton_text + " " + endbutton_text)
	shield_2_counter_label.grid(row = endbutton.grid_info()["row"], column = endbutton.grid_info()["column"])
	is_shield_2_set = True

