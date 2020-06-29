def ul(n):
	l,u=0,0
	for i in n:
		if i.islower():
			l+=1
		elif i.isupper():
			u+=1
	print('Number of uppercase letters: ',u)
	print('Number of lowercase letters:',l)
m=input('Enter a string: ')
ul(m)