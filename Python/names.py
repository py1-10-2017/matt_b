students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def dic_read(dictionary):


	for item in range(0,len(dictionary)):

		value_text = ""

		for value in dictionary[item].values():

			value_text+=" "+value
			
		print value_text[1:]


dic_read(students)



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def read_users(dictionary):


	for key in dictionary.keys():

		value_text = ""

		print "# " + key

	

		for item in range(0,len(dictionary[key])):

			value_text = ""

			value_counter = 0

			for value in dictionary[key][item].values():

		 		 value_text+=" "+value
		 		 value_counter+=1
			
			print "# "+str(item+1)+" - " + value_text[1:] +" - "+str(len(value_text[1:])-1)


read_users(users)





#  Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13