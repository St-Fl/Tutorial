while True:
	try:
		first = int(raw_input("Enter first number: "))
		last = int(raw_input("Enter last number: "))
		div1 = int(raw_input("Enter first divide value: "))
		div2 = int(raw_input("Enter second divide value: "))

		if last < first:
			print "The last number needs to be larger than the first one."
		elif last < div1:
			print "Divide value 1 needs to be smaller then last number."
		elif last < div2:
			print "Divide value 2 needs to be smaller then last number."	
		else:
			if div1 == 0 or div2 == 0:
				print "Can't divide zero. Try again ..."
			else:
				break

	except ValueError:
   		print "Please type in a number."


while first < last:
	first = first+1
	x = ""
	if first%div1==0:
		x = "bar"
	if first%div2==0:
		x += "foo"
	if  x != "":
		print first,x
