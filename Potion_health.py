import random

health = 50
difficulty = input("enter difficulty level easy,medium or hard : ") 

if(difficulty=="easy"):
    potion_health=int(random.randint(25,50)/1)
if(difficulty=="medium"):
    potion_health=int(random.randint(25,50)/2)
if(difficulty=="hard"):
    potion_health=int(random.randint(25,50)/3)


health = health + potion_health

print(health)
