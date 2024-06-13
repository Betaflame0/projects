import random
import time

cordArr = []
for i in range(3):
  temp = []
  for i in range(3):
    temp.append(" ")
  cordArr.append(temp)

def printBoard(board):
  for i in range(3):
    for j in range(3):
      if j == 2:
        print(" " + board[i][j], end="")
      else:
        print(" " + board[i][j] + " |", end="")
    if i != 2:
      print("\n-––+–––+–––")
  print("\n")

printBoard(cordArr)

def winCheck(cordArr):
  for b in range(3):
    vxCount = 0
    voCount = 0
    column = -1
    for i in cordArr:
      if(i[b]=="X"):
        vxCount+=1
        column=b
      elif(i[b]=="O"):
        voCount+=1
        column=b
      if(vxCount==3 or voCount==3):
        return i[column]
  for i in cordArr:
    hxCount = 0
    hoCount = 0
    for a in i:
      if(a=="X"):
        hxCount+=1
      elif(a=="O"):
        hoCount+=1
      if(hxCount==3 or hoCount==3):
        return a
  if(cordArr[0][0]==cordArr[1][1]==cordArr[2][2] and not(cordArr[0][0]==" ")):
    return cordArr[0][0]
  elif(cordArr[0][2]==cordArr[1][1]==cordArr[2][0] and not(cordArr[0][2]==" ")):
    return cordArr[0][2]
  return "No Winner"

def potentWin(cordArr):
  if(cordArr[0][1]=="X"):
    if(cordArr[0][0]=="X" and cordArr[0][2]!="O"):
      return [0,2]
    if(cordArr[0][2]=="X" and cordArr[0][0]!="O"):
      return [0,0]
  if(cordArr[1][0]=="X"):
    if(cordArr[0][0]=="X" and cordArr[2][0]!="O"):
      return [2,0]
    if(cordArr[2][0]=="X" and cordArr[0][0]!="O"):
      return [0,0]
  if(cordArr[1][2]=="X"):
    if(cordArr[0][2]=="X" and cordArr[2][2]!="O"):
      return [2,2]
    if(cordArr[2][2]=="X" and cordArr[0][2]!="O"):
      return [0,2]
  if(cordArr[2][1]=="X"):
    if(cordArr[2][0]=="X" and cordArr[2][2]!="O"):
      return [2,2]
    if(cordArr[2][2]=="X" and cordArr[2][0]!="O"):
      return [2,0]
  if(cordArr[1][1]=="X"):
    if(cordArr[0][1]=="X" and cordArr[2][1]!="O"):
      return [2,1]
    if(cordArr[1][0]=="X" and cordArr[1][2]!="O"):
      return [1,2]
    if(cordArr[2][1]=="X" and cordArr[0][1]!="O"):
      return [0,1]
    if(cordArr[1][2]=="X" and cordArr[1][0]!="O"):
      return [1,0]
  if(cordArr[0][0]=="X"):
    if(cordArr[0][2]=="X" and cordArr[0][1]!="O"):
      return [0,1]
    if(cordArr[2][0]=="X" and cordArr[1][0]!="O"):
      return [1,0]
  if(cordArr[2][2]=="X"):
    if(cordArr[0][2]=="X" and cordArr[1][2]!="O"):
      return [1,2]
    if(cordArr[2][0]=="X" and cordArr[2][1]!="O"):
      return [2,1]
  if(cordArr[2][2]=="X" and cordArr[0][0]=="X" and cordArr[1][1]!="O"):
      return [1,1]
  if(cordArr[0][2]=="X" and cordArr[2][0]=="X" and cordArr[1][1]!="O"):
      return [1,1]
  if(cordArr[1][0]=="X" and cordArr[1][2]=="X" and cordArr[1][1]!="O"):
      return [1,1]
  if(cordArr[0][1]=="X" and cordArr[2][1]=="X" and cordArr[1][1]!="O"):
      return [1,1]
  if(cordArr[0][0]=="X" and cordArr[1][1]=="X" and cordArr[2][2]!="O"):
    return [2,2]
  if(cordArr[2][2]=="X" and cordArr[1][1]=="X" and cordArr[0][0]!="O"):
    return [0,0]
  if(cordArr[0][2]=="X" and cordArr[1][1]=="X" and cordArr[2][0]!="O"):
    return [2,0]
  if(cordArr[2][0]=="X" and cordArr[1][1]=="X" and cordArr[0][2]!="O"):
    return [0,2]
  return "fail"
  
  # main.py
def compWinCheck(cordArr):
  if(cordArr[0][1]=="O"):
    if(cordArr[0][0]=="O" and cordArr[0][2]!="X"):
      return [0,2]
    if(cordArr[0][2]=="O" and cordArr[0][0]!="X"):
      return [0,0]
  if(cordArr[1][0]=="O"):
    if(cordArr[0][0]=="O" and cordArr[2][0]!="X"):
      return [2,0]
    if(cordArr[2][0]=="O" and cordArr[0][0]!="X"):
      return [0,0]
  if(cordArr[1][2]=="O"):
    if(cordArr[0][2]=="O" and cordArr[2][2]!="X"):
      return [2,2]
    if(cordArr[2][2]=="O" and cordArr[0][2]!="X"):
      return [0,2]
  if(cordArr[2][1]=="O"):
    if(cordArr[2][0]=="O" and cordArr[2][2]!="X"):
      return [2,2]
    if(cordArr[2][2]=="O" and cordArr[2][0]!="X"):
      return [2,0]
  if(cordArr[1][1]=="O"):
    if(cordArr[0][1]=="O" and cordArr[2][1]!="X"):
      return [2,1]
    if(cordArr[1][0]=="O" and cordArr[1][2]!="X"):
      return [1,2]
    if(cordArr[2][1]=="O" and cordArr[0][1]!="X"):
      return [0,1]
    if(cordArr[1][2]=="O" and cordArr[1][0]!="X"):
      return [1,0]
  if(cordArr[0][0]=="O"):
    if(cordArr[0][2]=="O" and cordArr[0][1]!="X"):
      return [0,1]
    if(cordArr[2][0]=="O" and cordArr[1][0]!="X"):
      return [1,0]
  if(cordArr[2][2]=="O"):
    if(cordArr[0][2]=="O" and cordArr[1][2]!="X"):
      return [1,2]
    if(cordArr[0][2]=="O" and cordArr[2][1]!="X"):
      return [2,1]
  if(cordArr[2][2]=="O" and cordArr[0][0]=="O" and cordArr[1][1]!="X"):
      return [1,1]
  if(cordArr[0][2]=="O" and cordArr[2][0]=="O" and cordArr[1][1]!="X"):
      return [1,1]
  if(cordArr[1][0]=="O" and cordArr[1][2]=="O" and cordArr[1][1]!="X"):
      return [1,1]
  if(cordArr[0][1]=="O" and cordArr[2][1]=="O" and cordArr[1][1]!="X"):
      return [1,1]
  if(cordArr[0][0]=="O" and cordArr[1][1]=="O" and cordArr[2][2]!="X"):
    return [2,2]
  if(cordArr[2][2]=="O" and cordArr[1][1]=="O" and cordArr[0][0]!="X"):
    return [0,0]
  if(cordArr[0][2]=="O" and cordArr[1][1]=="O" and cordArr[2][0]!="X"):
    return [2,0]
  if(cordArr[2][0]=="O" and cordArr[1][1]=="O" and cordArr[0][2]!="X"):
    return [0,2]
  return "fail"

#Counts total number of mvoes
def countTotal(cordArr):
  total = 0
  for i in cordArr:
    for a in i:
      if(a!=" "):
        total+=1
  return total

#Finds the region of board the users last move was in
def findRegion(y, x):
  region = "unknown"
  if(y==1 and x==1):
    region = "center"
  elif((y==0 and x==0) or (y==0 and x==2) or (y==2 and x==0) or (y==2 and x==2)):
    region = "corner"
  else:
    region = "side"
  return region

#Checks to find an open corner to move to
def findCorner(cordArr):
  corners = [[0,0],[0,2],[2,0],[2,2]]
  for i in range(3):
    for a in range(3):
      for x in corners:
        if(cordArr[i][a]==" " and [i,a]==x):
          return x

def findSide(cordArr):
  sides = [[0,1],[2,1],[1,2],[1,0]]
  for i in range(3):
    for a in range(3):
      for x in sides:
        if(cordArr[i][a]==" " and [i,a]==x):
          return x

def twoOnSideCheck(cordArr, y, x):
  if(findRegion(y,x)=="side"):
    if(cordArr[0][1]=="X" and cordArr[1][0]=="X" and cordArr[0][0]==" "):
      return [0,0]
    elif(cordArr[0][1]=="X" and cordArr[1][2]=="X" and cordArr[0][2]==" "):
      return [0,2]
    elif(cordArr[2][1]=="X" and cordArr[1][0]=="X" and cordArr[2][0]==" "):
      return [2,0]
    elif(cordArr[2][1]=="X" and cordArr[1][2]=="X" and cordArr[2][2]==" "):
      return [2,2]
  return None
      
#Makes a move when a win or a win block isn't required
def makeMove(cordArr, y, x):
  area = findRegion(y, x)
  totalMoves = countTotal(cordArr)
  if(totalMoves==1):
    if(area == "center"):
      return [0,0]
    elif(area=="corner"):
      return [1,1]
    elif(area=="side"):
      return [1,1]
  elif(twoOnSideCheck(cordArr,y,x)!=None):
    return twoOnSideCheck(cordArr,y,x)
  elif(findCorner(cordArr)!=None):
    return findCorner(cordArr)
  elif(findSide(cordArr)!=None):
    return findSide(cordArr)
  else:
    return [1,1]
  
def compMove(cordArr, y, x):
  loseResult = potentWin(cordArr)
  winResult = compWinCheck(cordArr)
  move = makeMove(cordArr, y, x)
  if(winResult!="fail"):
    cordArr[winResult[0]][winResult[1]] = "O"
  elif(loseResult!="fail"):
    cordArr[loseResult[0]][loseResult[1]] = "O"
  else:
    cordArr[move[0]][move[1]] = "O"
  
  
def playGame(cordArr):
  while(winCheck(cordArr)=="No Winner"):
    y = int(input("Pick a row(0,1,2): "))
    x = int(input("Pick a column(0,1,2): "))
    if(y<=2 and x<=2 and cordArr[y][x]==" "):
      cordArr[y][x] = "X"
      printBoard(cordArr)
      if(winCheck(cordArr)=="No Winner"):
        compMove(cordArr, y, x)
        printBoard(cordArr)
        if(winCheck(cordArr)!="No Winner"):
          print(f"The winner is: {winCheck(cordArr)}")
      else:
        print(f"The winner is: {winCheck(cordArr)}")
    else:
      print("Pick another space. This one is already taken or is outside bounds.")

def simGame(cordArr, numSims):
  xCount=0
  oCount=0
  drawCount=0
  for i in range(numSims):
    while(winCheck(cordArr)=="No Winner" and countTotal(cordArr)!=9):
      x = random.randint(0,2)
      y = random.randint(0,2)
      while(cordArr[y][x]!=" "):
        x = random.randint(0,2)
        y = random.randint(0,2)
      cordArr[y][x] = 'X'
      if(winCheck(cordArr)=="No Winner"):
          compMove(cordArr, y, x)
          if(winCheck(cordArr)=="X"):
            xCount+=1
          elif(winCheck(cordArr)=="O"):
            oCount+=1
      else:
          if(winCheck(cordArr)=="X"):
            xCount+=1
          elif(winCheck(cordArr)=="O"):
            oCount+=1
    if(countTotal(cordArr)==9):
      drawCount+=1
    for i in range(len(cordArr)):
        for a in range(len(cordArr[i])):
          cordArr[i][a] = " "
  print(f"X-Wins: {xCount}, O-Wins: {oCount}, Draws: {drawCount}")
  
playGame(cordArr)
    
      
    
      
      






