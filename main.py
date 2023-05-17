import random

# guessing number game!

status = 0

rn = int(random.randint(0, 9))

print("welcome! guess the number from 0-9!")

while status < 1:
  ans = float(input())
  if ans == rn:
    print("correct!")
    break
  else:
    print("wrong, try again!")
    continue
