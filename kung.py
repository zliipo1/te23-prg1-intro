# en version av kung king, nånting
# Två speleare 
# pelare 1 rullar tärning 
# spelare 2 rullar tärning
# vem rullade högst 
# upprepa, till vi har en vinnare av spelet, bäst av tre 

from random import randint 

play_game = "J"
player_one_score = 0
player_two_score = 0
    

while play_game.upper() == "J":


    player_one_roll = randint(1,6)
    player_two_roll = randint(1,6) 
   
    if player_one_roll > player_two_roll:
        print(f"spelare ett vinner")

    elif player_two_roll > player_one_roll: 
        print(f"spelare två vinner")
    else: 
        print(f"ingen spelare vinner")

elif player_two_score > 2: 

play_game = input("vill du spela igen?:[J/N]:")


# at göra, komma ihåg vilken spelare som har vunnit
# spela tills vi har en bäst av tre
# sedan fråga om vi vill spela igen    






