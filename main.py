from art import logo
import random  
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continueOrNot = ''
hitOrStand = ''

"""
This list keep the random user num in the zeroth index,sum of the random user num in the first index,
random computer num in the second index and sum of the random computer num in the third index.
"""
randomNumSpecs = []
def listReset(randomNumSpecs):
  randomNumSpecs = [[],[],[],[]]
  return randomNumSpecs

def listSum(list):
  sum = 0
  for i in list:
    sum += i
  return sum
  
def printOnScreenFirstHandle(randomNumSpecs):
  print(f"Your Cards : {randomNumSpecs[0]} ,Current Score : {randomNumSpecs[1]}")
  print(f"Computer's First Card : {randomNumSpecs[2][0]} ")

def printOnScreenFinalHandle(randomNumSpecs):
  print(f"Your Final Handle : {randomNumSpecs[0]} ,Final Score : {randomNumSpecs[1]}")
  print(f"Computer Final Handle : {randomNumSpecs[2]} ,Final Score : {randomNumSpecs[3]}")
"""
If computer win return 1,user win return 2,for withdraw return 0.
"""
def compareDeck(randomNumSpecs):
  if randomNumSpecs[3] == 21:
    return "Computer Win!"
  elif randomNumSpecs[1] == 21:
    return "User Win!"
  elif randomNumSpecs[1] > 21:
    if (11 in randomNumSpecs[0]) == True:
      indexOfAce = randomNumSpecs[0].index(11)
      randomNumSpecs[0][indexOfAce] = 1
      randomNumSpecs[1] = listSum(randomNumSpecs[0])
      if randomNumSpecs[1] > 21:
        return 2
      else:
        return 1     
while (continueOrNot.lower() != 'n'):
    randomNumSpecs = listReset(randomNumSpecs)
    continueOrNot = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    os.system('cls')
    if (continueOrNot.lower() == 'y'):
        print(logo)
        for _ in range(2):
          randomNumSpecs[0].append(random.choice(cards))
          randomNumSpecs[2].append(random.choice(cards))
        randomNumSpecs[1] = listSum(randomNumSpecs[0])
        randomNumSpecs[3] = listSum(randomNumSpecs[2])
        printOnScreenFirstHandle(randomNumSpecs)

        printOnScreenFinalHandle(randomNumSpecs)
        if compareDeck(randomNumSpecs) == 2:
          print("Computer Win!")
        elif compareDeck(randomNumSpecs) == 1:
          print("User Win!")
        elif compareDeck(randomNumSpecs) == 0:
          print("Draw!")

        else:
          hitOrStand = input("Type 'y' to get another card, type 'n' to pass:")
          if(hitOrStand.lower() == 'y'):
            randomNumSpecs[0].append(random.choice(cards))
            randomNumSpecs[1] = listSum(randomNumSpecs[0])
          if(hitOrStand.lower() == 'n'):
            while (randomNumSpecs[3] < 17):
              randomNumSpecs[2].append(random.choice(cards))
              randomNumSpecs[3] = listSum(randomNumSpecs[2]) 
              
          if randomNumSpecs[3] > 21 :
            printOnScreenFinalHandle(randomNumSpecs)
            print("User Win!")
          else:
            if randomNumSpecs[1] == randomNumSpecs[3]:
              printOnScreenFinalHandle(randomNumSpecs)
              print("Draw!")
            elif randomNumSpecs[3] > randomNumSpecs[1]:
              printOnScreenFinalHandle(randomNumSpecs)
              print("Computer Win!")
            elif randomNumSpecs[3] < randomNumSpecs[1]:
              printOnScreenFinalHandle(randomNumSpecs)
              print("User Win!")
    elif (continueOrNot.lower() != 'y' and continueOrNot.lower() != 'n'):
      print("Invalid process.!")
      
print("Program is terminating...")
