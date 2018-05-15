n = input("nhap so n : ")
A = []
for i in range (1 , n+1):
	A.append(input("nhap phan tu so %d : " % i))
for i in A :
	if( i % 2 ==  0):
		print i
A.sort()
A.reverse()
print A
	
	
