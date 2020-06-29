def rno(n):
	if n in range(l,h+1):
		return True
	else:
		return False
l,h,m=int(input('Enter lowest no: ')),int(input('Enter highest no: ')),int(input('Enter no: '))
if (l>h):
	print('Entered lowest number is greater than highest')
elif(rno(m)):
	print(m,'is within range (',l,',',h,')')
else:
	print(m,'is not within range (',l,',',h,')')