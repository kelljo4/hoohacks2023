import random

print("----------------------------------")
print("Welcome... to Rock Paper Scissors!")
print("----------------------------------")

### Set up variables
cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["Rock","Paper","Scissors"]

def winnercheck(playerselection, botselection):
  if(playerselection == "Rock" and botselection == "Paper"):
    print("You lost! Better luck next time! +0 points")
    return "Cpu"
  elif(playerselection == "Rock" and botselection == "Scissors"):
    print("You have won! Congrats! +1 point ")
    return "Player"
  elif(playerselection == "Scissors" and botselection == "Paper"):
    print("You have won! Congrats! +1 point ")
    return "Player"
  elif(playerselection == "Scissors" and botselection == "Rock"):
    print("You lost! Better luck next time! +0 points")
    return "Cpu"
  elif(playerselection == "Paper" and botselection == "Rock"):
    print("You have won! Congrats! +1 point ")
    return "Player"
  elif(playerselection == "Paper" and botselection == "Scissors"):
    print("You lost! Better luck next time! +0 points")
    return "Cpu"
  else:
    print("Its a draw!")
    return "Draw"

### Start game loop
while(playerScore != 3 and cpuScore != 3):
  ### Validate input
  while True:
    playerHand = input("\nPick a hand. Rock, Paper, or Scissors: ")
    if(playerHand == "Rock" or playerHand == "Paper" or playerHand == "Scissors"):
      break
    else:
      print("Invalid input. Try again.")
  
  ### Generate computer pick
  computerHand = random.choice(possibleHands)

  ### Print results
  print("Your hand: ", playerHand)
  print("Cpu hand: ", computerHand)
  result = winnercheck(playerHand, computerHand)
  if(result == "Player"):
    playerScore += 1
  elif(result == "Cpu"):
    cpuScore += 1
  else:
    tieScore += 1
  print("Your score: ", playerScore, "CPU: ", cpuScore, "Ties: ", tieScore)