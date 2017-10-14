name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]



def create_dictionary(list_1, list_2):

	new_dictionary = {}

	for item in range(0,len(list_1)):

		new_dictionary[list_1[item]] = list_2[item]

	print new_dictionary

create_dictionary(name, favorite_animal)