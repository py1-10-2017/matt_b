words = "It's thanksgiving day. It's my birthday,too!"

print(words.find('day'))

words = words.replace("day","mouth")

print(words)

x = [2,54,-2,7,12,98]

print(max(x))
print(min(x))

x = ["hello",2,54,-2,7,12,98,"world"]

print(x[0], x[-1])

new_x = [x[0], x[-1]]

print(new_x)

x = [19,2,54,-2,7,12,98,32,10,-3,6]


x_sort = sorted(x)

half = len(x_sort) / 2

sort_array = [x_sort[:half], ]

for each in x_sort[half:]:
	sort_array.append(each)


print(sort_array)
