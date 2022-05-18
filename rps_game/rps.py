from random import randint

playing = input("Do you wanna play? ")
if playing.lower() != "yes":
    quit()
name = input("Choose your name: ")

print("Hello " + name +"! \nLet's play!")

score = 0
enemy_score = 0
weapon_names = ["rock", "paper", "scissors"]
round = 1
while(score<3 and enemy_score<3):
    print("------------------------------------")
    print("Round "+str(round))
    weapon=input("Choose your weapon:\n1)rock\n2)paper\n3)scissors\nor q to leave ").lower()

    if weapon == "q":
        break
    if weapon not in ["1", "2", "3"]:
        continue
    weapon_number = int(weapon)
    weapon_generated = randint(1,3)

#Win Scenario 
    #Rock
    if weapon_number == 1 and weapon_generated == 3: 
        print("Enemy weapon: "+ weapon_names[weapon_generated-1])
        print(name+"'s weapon: "+ weapon_names[weapon_number-1])
        print("You won this round!")    
        score+=1
        print(name+": "+str(score)+" Enemy score: "+str(enemy_score))
    #Paper
    elif weapon_number == 2 and weapon_generated == 1: 
        print("Enemy weapon: "+ weapon_names[weapon_generated-1])
        print(name+"'s weapon: "+ weapon_names[weapon_number-1])
        print("You won this round!")    
        score+=1
        print(name+": "+str(score)+" Enemy score: "+str(enemy_score))
    #Scissors
    elif weapon_number == 3 and weapon_generated == 2: 
        print("Enemy weapon: "+ weapon_names[weapon_generated-1])
        print(name+"'s weapon: "+ weapon_names[weapon_number-1])
        print("You won this round!")    
        score+=1
        print(name+": "+str(score)+" Enemy score: "+str(enemy_score))
#Draw Scenario
    elif weapon_generated == weapon_number:
            print("Enemy weapon: "+ weapon_names[weapon_generated-1])
            print(name+"'s weapon: "+ weapon_names[weapon_number-1])
            print("It's a draw!")
            print(name+": "+str(score)+" Enemy score: "+str(enemy_score))
#Lose Scenario
    else:
        print("Enemy weapon: "+ weapon_names[weapon_generated-1])
        print(name+"'s weapon: "+ weapon_names[weapon_number-1])
        print("You lost this round!")    
        enemy_score+=1
        print(name+": "+str(score)+" Enemy score: "+str(enemy_score))
    round+=1
print("------------------------------------")
print("Final result\n"+name+": "+str(score)+" Enemy score: "+str(enemy_score))