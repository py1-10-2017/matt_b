# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python


person_dic = {
	
	"name": "Matt",
	"age": 34,
	"country": "US",
	"language": "Python"
}


print "My name is "+person_dic["name"]
print "My age is "+str(person_dic["age"])
print "My country of birth is "+person_dic["country"]
print "My favorite language is "+ person_dic["language"]



def dic_read(dictionary):

	for key, value in dictionary.items():

		print key, value


dic_read(person_dic)