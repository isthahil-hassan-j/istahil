import turtle
import random
player_one = turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,100)
die = [1,2,3,4,5,6]
for i in range(20):
    if player_one.pos()>=(300,100):
        print("player one wins!")
        break
    elif player_two.pos()>=(300,100):
        print("player two wins!)
              else:
                  player_one_turn = ("press 'enter' to roll the dice")
                  die_outcome = random.choice(die)
                  print("the result of the die roll is: ")
                  print(die_outcome)
                  print("the number of steps will be: ")
                  print(20*die_outcome)
                  player_one.fd(20*die_outcome)
                  player_two_turn = input("press 'enter' to roll the dice")
                  die_outcome = random.choice(die)
                  print("the result of the dice roll is: ")
                  print(die_outcome)
                  print("the number of the steps will be: ")
                  print(20*die_outcome)
                  player_two.fd(20*die_outcome)
                  
