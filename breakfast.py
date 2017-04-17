def mix():
	print("get the ingredients")
	print("mix the ingredients")

def cook():
	print("Warm the pan on the stove")
	print("pour oil and let it warm")
	print("When oil is warm, pour the mixture")

def makeBreakfast(type_of_breakfast,ingredients = []):
	mix()
	cook()
	
	print("Flip %s from side to side"%type_of_breakfast)
	if len(ingredients) > 0:
		print("Serve the "+type_of_breakfast+" with "+",".join(ingredients))
		breakfast = "------Serve the {} with {} ------".format(type_of_breakfast,",".join(ingredients))
	else:
		print("Serve the "+type_of_breakfast)
		breakfast = "------Serve the {} ------".format(type_of_breakfast)
	
	return breakfast

#makeBreakfast('eggs')
makeBreakfast('pancake')
makeBreakfast('pancake',['garlic','tomatoes'])