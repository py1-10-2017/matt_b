import numbers



 #input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"




def type_list(list_input):

	type_list = []

	my_string = ""

	my_number = 0

	for item in list_input:

		type_list.append(type(item))

		if isinstance(item, basestring):

			my_string+=item

		elif isinstance(item, numbers.Number):

			my_number+=item


	if len(set(type_list)) > 1:

		print "Mix type list"

	else:

		print "Only one type in list"



	print my_string
	print my_number

type_list(l)