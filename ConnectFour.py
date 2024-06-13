arr = []
for i in range(6):
	temp = []
	for a in range(7):
		temp.append("_")
	arr.append(temp)

def printBoard():
	for i in arr:
		print(i)

def makeMove(plr):
	var = True
	while(var):
		while(0==0):
			col = int(input(f"Player {plr}: Please enter a column 1-7"))-1
			if(col<7 and col>-1):
				break
			else:
				print("Invalid column. Pick again.")
		temp = len(arr)-1
		while(temp>-1 and arr[temp][col]!="_"):
			temp-=1
		if(temp==-1):
			var = True
		else:
			arr[temp][col]=plr
			var = False

def isFull():
	for i in arr:
		for a in i:
			if(a=="_"):
				return False
	return True

def winCheck():
	for i in range(0,len(arr)-3):
		for a in range(0,len(arr[i])):
			t1 = arr[i][a]
			t2 = arr[i+1][a]
			t3 = arr[i+2][a]
			t4 = arr[i+3][a]
			if(t1==t2==t3==t4=="O"):
				return "O"
			if(t1==t2==t3==t4=="X"):
				return "X"
	for i in range(0,len(arr)):
		for a in range(0,len(arr[i])-3):
			t1 = arr[i][a]
			t2 = arr[i][a+1]
			t3 = arr[i][a+2]
			t4 = arr[i][a+3]
			if(t1==t2==t3==t4=="O"):
				return "O"
			if(t1==t2==t3==t4=="X"):
				return "X"
	for i in range(0,len(arr)-3):
		for a in range(0,len(arr[i])-3):
			t1 = arr[i][a]
			t2 = arr[i+1][a+1]
			t3 = arr[i+2][a+2]
			t4 = arr[i+3][a+3]
			if(t1==t2==t3==t4=="O"):
				return "O"
			if(t1==t2==t3==t4=="X"):
				return "X"
	for i in range(3,len(arr)):
		for a in range(0,len(arr[i])-3):
			t1 = arr[i][a]
			t2 = arr[i-1][a+1]
			t3 = arr[i-2][a+2]
			t4 = arr[i-3][a+3]
			if(t1==t2==t3==t4=="O"):
				return "O"
			if(t1==t2==t3==t4=="X"):
				return "X"
	return "n/a"

def playGame():
	while(not(isFull())):
		makeMove("X")
		printBoard()
		if(not(winCheck()=="n/a")):
			print(f"Our winner is Player {winCheck()}")
			break
		makeMove("O")
		printBoard()
		if(not(winCheck()=="n/a")):
			print(f"Our winner is Player {winCheck()}")
			break

printBoard()

playGame()




