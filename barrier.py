import random
from tkinter import *

BARRIER_1 = u"\U0001F5D9"
BARRIER_2 = u"\U0001F5D9"

barrier_1_rounds = 0
barrier_2_rounds = 0

is_barrier_1_set = False
is_barrier_2_set = False

barrier_field_button_1 = None
barrier_field_button_2 = None

tk = None

def initTk(parentTk):
	tk = parentTk
	
def decreaseRounds():
	global barrier_1_rounds, barrier_2_rounds
	barrier_1_rounds -=1
	barrier_2_rounds -=1

def setActionLabel(endbutton_text, action_label):
  if endbutton_text == BARRIER_1 or endbutton_text == BARRIER_2:
    action_label.config(text = "A BARRIER IS BLOCKING YOU!", fg = "purple")

def removeBarrierIfExist(barrier_button, button_list):
	if barrier_button:
		button_list.append(barrier_button)
		if barrier_button["fg"] == "purple":
			barrier_button.config(text= "")

def isBarrierOnField(field_button):
	return field_button == barrier_field_button_1 or field_button == barrier_field_button_2

def setColorOnBarrierField(field_button):
	field_button.config(fg = "purple")

def clearColorOnBarrierField(field_button):
	field_button.config(fg = "black")

def getButtonPosition(button):
	x = button.grid_info()["row"]-1
	y = button.grid_info()["column"]-1
	position = x, y
	return position

def placeBarrier(button_list, players_pos_list, endbutton_pos, barrierText, barrier_button):
	removeBarrierIfExist(barrier_button, button_list)
	
	# find an empty field to place the barrier		
	while True:
		barrier_button = random.choice(button_list)
		barrier_pos = getButtonPosition(barrier_button)
		if barrier_pos not in players_pos_list and barrier_pos != endbutton_pos:
			button_list.remove(barrier_button)
			barrier_button.config(text=barrierText, fg = "purple")
			break
		
	print("BARRIER BUTTON", barrier_button)
	print("BARRIER COORDS", barrier_pos)
	return barrier_button

def placeBarrier1(button_list, players_pos_list, endbutton_pos):
	global barrier_field_button_1, barrier_1_rounds, is_barrier_1_set
	is_barrier_1_set = True
	barrier_1_rounds = 4
	barrier_field_button_1 = placeBarrier(button_list, players_pos_list, endbutton_pos, BARRIER_1, barrier_field_button_1)

def placeBarrier2(button_list, players_pos_list, endbutton_pos):
	global barrier_field_button_2, barrier_2_rounds, is_barrier_2_set
	is_barrier_2_set = True
	barrier_2_rounds = 4
	barrier_field_button_2 = placeBarrier(button_list, players_pos_list, endbutton_pos, BARRIER_2, barrier_field_button_2)
	
def isBarrier1Played(endbutton):
	return endbutton == barrier_field_button_1

def isBarrier2Played(endbutton):
	return endbutton == barrier_field_button_2

def isBarrier1Set(endbuttonPosition):
	return is_barrier_1_set and endbuttonPosition == getButtonPosition(barrier_field_button_1)

def isBarrier2Set(endbuttonPosition):
	return is_barrier_2_set and endbuttonPosition == getButtonPosition(barrier_field_button_2)
