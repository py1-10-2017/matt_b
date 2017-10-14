

# x   1  2  3  4  5  6  7  8   9  10  11  12

num_list = [1,2,3,4,5,6,7,8,9,10,11,12]


print "x 1 2 3 4 5 6 7 8 9 10 11 12" 

number_string = ""

for out_number in num_list:

	number_string+=str(out_number)

	for inner_number in num_list:

		number = out_number * inner_number

		number_string+=" "+str(number)

	number_string+="\n"

print number_string
	
