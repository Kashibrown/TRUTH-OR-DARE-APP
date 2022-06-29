# a truth or dare game
from random import shuffle


print("Single game")
names = ["Jenny" , "kashi", "Emmanuel", "Bunmi" ," victor", "Stefan", "Patricia","Bola"]
for p in names:
    shuffle(names)
print(p, "it is your turn")
question = input("Truth or Dare: ")
if question == "Truth".lower():
    input("What do you love most: ") 
elif question =="Dare".lower():
    print("Do 5 pushups!") 
else:
    print("Next!", end=" ")
    
for p in names:
    shuffle(names)
print(p,"it is your turn ")
question_2= input("Truth or Dare: ")
if question_2 == "Truth".lower():
    input("What is your best color: ")
elif question_2 == "Dare".lower():
    input("Slap the person next to you")
else:
    print("Next",end=" ")

for p in names:
    shuffle(names)
print(p, "it is your turn")
question_3= input("Truth or Dare: ")
if question_3 =="Truth".lower():
    input("Who was your first heartbreak: ")
elif question_3 == "Dare".lower():
    print("Kiss the person next to you")
else:
    print("Next!", end=" ")
    
    
for p in names:
    shuffle(names)
print(p, "it is your turn")
question_4= input("Truth or Dare: ")
if question_4 =="Truth".lower():
    input("What is your biggest regret?: ")
elif question_4 == "Dare".lower():
    print("Remove a piece of clothing")
else:
    print("Next!", end=" ")
    

for p in names:
    shuffle(names)
print(p, "it is your turn")
question_5= input("Truth or Dare: ")
if question_5 =="Truth".lower():
    input("Who do you wish to have sex with in this room: ")
elif question_5 == "Dare".lower():
    print("spit on the floor and lick it")
else:
    print("Next!", end=" ")
    

for p in names:
    shuffle(names)
print(p, "it is your turn")
question_6= input("Truth or Dare: ")
if question_6 =="Truth".lower():
    input("Who do you dislike most in this room: ")
elif question_6 == "Dare".lower():
    print("slap the person closer to you personally in this room")
else:
    print("Next!", end=" ")
    
    

