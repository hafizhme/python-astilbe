ret = ''
for i in range(0,10):
  if i != 9:
    ret += str(i+1) + ', '
  else:
    ret += str(i+1)
	
	if i != 9:
		continue
	print(ret)
