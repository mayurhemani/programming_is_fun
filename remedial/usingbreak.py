usercommand = ""
while True:
	usercommand = input("Enter your command: ")
	if usercommand == "exit":
		break

	print("running your command sir")
	
	if usercommand == "stars":
		print("****************")
	elif usercommand == "dashes":
		print("----------------")
	else:
		print("nothing for you")
	
print("program end")
