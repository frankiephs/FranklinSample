import random

def start():
  print("game activated!")
  print("type 'play' to play!")
  print("type 'lb' to check the leaderboards")
start()
# infinite loop status
gamestatus = 0
# 0 is at home
# 1 is at play
# 2 is at lb

# leaderboards list
leaderboards = []
username = ""
score = []
userdict = {username: score}





# statuses
# checks if you are playing a game
playstatus = 0

# checks if you are in the leaderboards panel
lbstatus = 0









# game function
def guess():
  print("enter your name: ")
  rn = int(random.randint(0, 9))
  points = 0
  number_of_points = []
  gameusername = str(input())
  print("ur name is..", (gameusername))
  gameuserdict = {gameusername: number_of_points}
  
  attempts = 0
  print("welcome! guess the number from 0-9!")

  while playstatus < 1:
    ans = float(input())
    if ans == rn:
      print("correct!")
      points = 100 - attempts
      number_of_points.append(points)
      break
    else:
      print("wrong, try again!")
      attempts = attempts + 1
      continue







leaderboardsdict

#leaderboards function
def lbspace():
  print(leaderboards[0])
  print(leaderboards[1])
  print(leaderboards[2])
  print("type 'return' to return")
  rtn = "return"
  
  while lbstatus > 1:
    ans = str(input())
    if ans == rtn:
      break
    else:
      print("type 'return'")
      continue





  




# home

# play
while gamestatus < 1:
  userinp = str(input())
  if userinp == "play":
    guess()
    start()
    
    # leaderboards
  if userinp == "lb":
    guess()

  if userinp != "play" "lb":
    print("invalid syntax dummy")
    continue




  

