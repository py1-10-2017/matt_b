import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...


for number in range(0,10):

	random_num = random.randint(60,100)

	print "Score and Grades"

	if random_num>=60 and random_num<=69:
		grade = "D"
	elif random_num>=70 and random_num<=79:
		grade = "C"
	elif random_num>=80 and random_num<=89:
		grade = "B"

	else:
		grade = "A"


	print "Score: "+ str(random_num) + "; Your grade is: " + str(grade)



