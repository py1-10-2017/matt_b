

def odd_even():

	for num in range(0,2001):

		if num % 2 == 0:

			print "Number is "+str(num)+": This is an even number"
		else:
			print "Number is "+str(num)+": This is an odd number"


# odd_even()


a = [2,4,10,16]


def multiply(a, multiplier):

	multiplier_list = []

	for number in range(0,len(a)):

		multiplier_list.append(a[number] * multiplier)

	return multiplier_list



multiply(a,5)

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array


x = layered_multiples(multiply([2,4,5],3))
print x
