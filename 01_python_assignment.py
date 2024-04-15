import numpy as np
import matplotlib.pyplot as plt
import random

def generate_random_set(min_val, max_val, set_length):
  return set(np.random.choice(np.arange(min_val, max_val, 1), size=set_length, replace=False))

def generate_rock_paper_scissors(rounds):
  return [random.choice(['R', 'P', 'S'])+random.choice(['R', 'P', 'S']) for _ in range(rounds)]

def problem_one(A, B, C):
  """ solves problem one """
  #(A intersect B) Union C
  #step 1, get intersection of A and B
  D = set.intersection(A,B)
  #step 2, get union of a ∩ B and C
  return D | C

def problem_two(A, B, C):
  """ solves problem two """
  #(A U C) ∩ (B U C)
  #step 1, get A U C
  D = A | C
  #step 2, get B U C
  E = set.intersection(B | C)
  #step 3, get their intersection
  return set.intersection(D,E)

def problem_three(A, B, C):
  """ solves problem three """
  #does problem_1 equal problem_2
  #step 1, find out what they are
  D = problem_one(setA,setB,setC)
  E = problem_two(setA,setB,setC)
  #step two, compare them 
  return True if D == E else False

def problem_four(games):
  """ solves problem four """
  #this is where things get interesting
  #we are to estimate the average number of rounds, but how do we do that
  #the average mathmatically is rounds / wins.
  #in rock paper scissors ties only happen when both sides choose the same thing, so to determine a win we just do an if, else statement
  # we need a count of rounds, and we need a count of wins
  #we also need a way to loop through all rounds

  #step 1, generate the rock paper scissocrs
  gamesSet = generate_rock_paper_scissors(games)
  #step 2, initialize other needed variables
  numberrounds = 0
  numberwins  = 0
  #step 3, loop through all games
  for element in gamesSet:
      #step 4, increment wins count if they aren't the same, increment rounds count either way
      if (element[0] ==  element[1]):
        numberrounds += 1
      else:
        numberrounds +=1
        numberwins +=1
  #step 5, return the average
  return numberrounds / numberwins
        

def problem_five(number_of_games):
  """ solves problem five """
  #This is the most difficult one, apparently i'm to plot a histogram on the length of every game
  #you'd think this would be similar to the last problembut I didnt need to know how long each specific game lasted... i'll figure out how to do that
  #ok so we're tasked to do number of games, to calculate the games we must have a loop and if they both give the same value we go again and if they have a different value
  #we call it a game. We should also collect a set showing the number of rounds it took to complete a game, since that is what this assignment is all about

  gamesplayed = 0
  roundsList = []
  #Step 1, get the data
  while gamesplayed < number_of_games:
      #start rounds at 0
      rounds = 0
      #set roundOver flag to false
      roundOver = False

      #let the game play out!
      while roundOver == False:
        #generate a round
        rounds+=1
        round = generate_rock_paper_scissors(1)
        for element in round:
          #see if it's a winner or not
          if element[0] != element[1]:
             gamesplayed+=1
             roundsList.append(rounds)
             roundOver = True
        
  plt.xlabel("Rounds")  
  plt.ylabel("Games")  


  #I used ChatGPT to do this part, I wanted the formatting to be nice for the histogram

  # Plotting the histogram
  plt.hist(roundsList, bins=np.arange(min(roundsList), max(roundsList)+2) - 0.5, edgecolor='black')
  # Setting X and Y axis ticks
  plt.xticks(np.arange(min(roundsList), max(roundsList)+1, 1))  # Set x ticks with step of 1
  plt.yticks(np.arange(0, max(np.histogram(roundsList, bins=np.arange(min(roundsList), max(roundsList)+2))[0])+1, 1))  # Set y ticks with step of 1
 
 

  
  return roundsList


if __name__== "__main__":
  #Generate the sets
  setA = generate_random_set(1,9,3)
  setB = generate_random_set(1,9,3)
  setC = generate_random_set(1,9,3)
  #let us know what the sets are
  print("Set A = " + str(setA))
  print("Set B = " + str(setB))
  print("Set C = " + str(setC))
  #test number 1
  print("1: (A ∩ B) U C: " + str(problem_one(setA,setB,setC)))
  #test number 2
  print("2: (A U C) ∩ (B U C) : " + str(problem_two(setA,setB,setC)))
  #test nuber 3
  print("3: does 1 = 2? " + str(problem_three(setA,setB,setC)))
  #test number 4
  print("4: Average number of rounds: " + str(problem_four(300)))
  #test number 5
  print("Test 5!")
  print("5: games histogram: " + str(problem_five(8) ))
  plt.show()