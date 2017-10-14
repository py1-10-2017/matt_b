import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...


heads = 0
tails = 0

for number in range(1,5001):

	print "Starting the program...."

	random_num = random.randint(1,2)

	if random_num == 1:
		heads+=1
		throw = "heads"
	else:
		tails+=1
		throw = "tails"

	print "Attempt #"+str(number)+": Throwing a coin... It's a "+str(throw)+"! ... Got "+str(heads)+" head(s) so far and "+str(tails)+" tail(s) so far"





