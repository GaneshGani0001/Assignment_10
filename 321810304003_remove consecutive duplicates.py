l=[]
n = int(input("Enter no of elements : ")) 
for i in range(0, n):
	e= int(input()) 
	l.append(e)
i = 0
while i < len(l)-1:
    if l[i] == l[i+1]:
        del l[i]
    else:
        i = i+1
print("list after removing consecutive duplicate",l)        