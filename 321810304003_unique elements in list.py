l,n,i,c=[],int(input("Enter no of elements : ")),0,0 
for t in range(0, n):
	l.append(input())
print("unique elements are:")
while i < len(l):
    j=0
    while j < len(l):
     if l[i]==l[j] and i!=j:
      c+=1
      break
     j+=1
    if c==0:
     print(l[i])
    i+=1
    c=0    