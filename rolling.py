def rollingString(s,operations):
	
	for op in operations:
		l,r,direction = op.split(" ")
		# print(l,r,direction)
		s = change(int(l),int(r),list(s),direction)
	# print(s)




def change(l,r,s,direction):
	print (s)
	if direction == "L":
		diff = -1
	else:
		diff = 1
	for i in range(l,r+1):
		#print(i,s)
		s[i] = chars[(ord(s[i])-97+diff+26)%26]

	return "".join(s)
# print(change(0,0,list(a),"L"))

s="abc"
chars = list("abcdefghijklmnopqrstuvwxyz")
operations = ['0 0 L','2 2 L','0 2 R']

rollingString(s, operations)

