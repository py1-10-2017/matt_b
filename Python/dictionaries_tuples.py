# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


tuple_list = []
for key, value in my_dict.items():

	my_tuple = (key, value)

	tuple_list.append(my_tuple)


print(tuple_list)


#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]