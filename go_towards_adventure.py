##final course assignment

##introductions!
##get user_name and have user choose an item
user_name = input("Please enter name > ")
print("Hello {}, welcome to your adventure game!".format(user_name))
print("You are only capable of handling one item.")
print("Please choose from one of teh avaliable items.")
print("A shiny sword | Sturdy Bow and Arrows | Your pet dog")
user_item = input("> ")


##response to chooing an item
if user_item == "a shiny sword":
  print("I see a fierce warrior ready to take on any challenge!")
elif user_item == "sturdy bow and arrows":
  print("A strategic warrior that will confuse the enemy into surrender!")
elif user_item == "your pet dog":
  pet = input("AWWW your dog is so cute!! What's their name? > ")
  print("Well its very noce to meet you {}! I hope you have a great adventure!".format(pet))
else: 
  print("We don't have that item.")

##if user chose a pet, have a seperate condition 
if pet == " ":
  print("Now brave warrior and trusty companion, let me tell you about your adventure!")
else:
  print("Now warrior, let me tell you about your adventure!")



##have user choose the best path to get to the end: land, sea, air
## land warrior will need to fight the chubacabra
## air/sky warrior will solve a puzzel that gargolye gives
## sea warrior will need to solve a riddle
##add code that tells the the warrior about thier adventure. 
##as the crowds cheer they can tell the user
##the stories they heard