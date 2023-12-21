### Python Area Calculator
### Brent Mayes
###

from art import *
from math import pi

def splashText(): # uses the art library for fancy ascii art
	AreaText = text2art("AREA",font="alpha")
	print(AreaText)
	CalculatorText = text2art("                 calculator",font="chunky")
	print(CalculatorText)

def menu(funcDict): # function select menu
	print("\n\nFunction Select")
	for funcNum in funcDict.keys(): # iterates through the function dictionary for user display
		print(f"	{funcNum}) {funcDict.get(funcNum)[0]}")
	
	funcDict.get(selFunc := input("\nWhich function do you want? "), lambda: "Invalid")[1]() # calls function user picks

### AREA FUNCTIONS ###
def rectA():
	print(f'Area: {int(l := input("Length? ")) * int(w := input("Width? "))}')

def circleA():
	print(f'Area: {pi * (int(r := input("Radius? "))**2)}')

def triA():
	print(f'Area: {0.5 * int(b := input("Base? ")) * int(h := input("Height? "))}')

def trapA():
	print(f'Area: {0.5 * int(b1 := input("Base 1? ")) * int(b2 := input("Base 2? ")) * int(h := input("Height? "))}')
######################

def main():
	# the dictionary of all the area functions, in format num | english name | function name
	theFuncDict = { "1" : ["Rectangle", rectA],
			"2" : ["Circle", circleA],
			"3" : ["Triangle", triA],
			"4" : ["Trapezoid", trapA],
			"9" : ["Exit", exit], }

	splashText() # calls the splash text visible on opening of program
	
	while True: # while true loop used to always return to the function select menu unless the exit function is called
		menu(theFuncDict)

main()