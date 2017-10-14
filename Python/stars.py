



x = [4, 6, 1, 3, 5, 7, 25]


for number in range(0,len(x)):


	print x[number] * "*"



x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


for index in range(0,len(x)):

	if isinstance(x[index], basestring):
		print x[index][0].lower() * len(x[index])
	else:
		print x[index] * "*"