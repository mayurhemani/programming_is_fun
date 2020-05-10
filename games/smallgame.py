import Tkinter as T

tk = T.Tk()
C = T.Canvas(tk, bg="white", height=800, width=1000)
C.pack()
x = 10
y = 10
C.create_oval(715, 715, 765, 765, fill="red", outline="#fff")

while True:
	C.create_oval(x, y, x + 50, y + 50, fill="blue", outline="#fff")
	command = raw_input("Command:> ")
	bx = x
	by = y
	if command == "left":
		x = x - 100
	elif command == "right":
		x = x + 100
	elif command == "exit":
		break
	elif command == "up":
		y = y - 100
	elif command == "down":
		y = y + 100
	C.create_oval(bx, by, bx + 50, by + 50, fill="white", outline="#fff")
	
tk.mainloop()
