i = 1

while True:
	if i != 10:
		print(i, end=', ')
	else:
		print(i)
	
	i += 1
	
	if i == 11:
		break
		
print('You got i =', i)
