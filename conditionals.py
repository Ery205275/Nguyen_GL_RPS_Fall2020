#set up a variables, check its alue, and then g down difference paths depending on the outcome
temperature = int(input("input a value between 0 and 100: "))

if (temperature <= 4):
	#water is frozen
	print("water's state is solid (ice)")
elif (temperature < 100):
	#water is liquid
	print("water's state is liquid")
else:
	#water is boiling, steam
	print("water is vapor")
