import random
#Welcome Text
print("----------------------------------")
print("Welcome... to Rock Paper Scissors!")
print("----------------------------------")

#First Set scores
botscore = 0

playerscore = 0

drawscore = 0

items = ["Rock", "Paper", "Scissors"]

#if and elif statements
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
    
    
while (playerscore != 3 and botscore != 3):
 while True:
   playerselection = input("Pick an option: Rock, Paper, or Scissors: ")
   if (playerselection == "Rock" or playerselection == "Paper" or playerselection == "Scissors"):
     break
   else:
     print("Invalid input. Please type Rock, Paper, or Scissors")

#Random bot choice process

 botselection = random.choice(playerselection)

 print("Current Hand: ", playerselection)
 print("Bot's Hand: ", botselection)
 result = winnercheck(playerselection, botselection)
 if (result == "Player"):
  playerscore += 1
 elif(result == "Bot"):
  botscore += 1
 else:
  drawscore += 1
 print ("Your score: ", playerscore, "Bot: ", botscore, "Draws: ", drawscore)