#this py has a function

def death():
  print ("wasted")

def survive():
    print ("you live")
    
def win():
    print("you will prosper")
    
print ("you are stuck in the wasteland and must reach the land of prosperity.")
print ("to reach the land of prosperity, you must pass through three traps set by the wastelanders.")
print ("you know that there are three traps but you do not know what they are so you must use your intelligence to persevere through the land.")
print ("as you walk you reach a wall made of scrap with three doors, 1 says scrap, 2 says land of prosperity, 3 says life.")
choice = input ("which door (1,2,3) will you pick:")
if choice == "2":
    death()
elif choice == "3":
    death()
elif choice == "1":
    survive()
    print ("wastelanders love their scrap, no other door would make since.")
    print ("as you pass through the door, you see a stretch of empty land, this is not usuall for the scrap yard which is the wasteland.")
    choice = input ("should you walk through and enjoy the open road (yes,no):")
    if choice == "yes":
        death()
    elif choice == "no":
        survive()
        print ("you guess that the field is full of mines which you then confirm when you see another traveler running in the distance blasted into smitherines.")
        print ("now that you know that the open land is indeed full of landmines, you only have a few options.")
        print ("1) you use the scrap in your bag to throw ahead of you in select spots to check if there is a mine in the location")
        print ("2) you run and jump in hopes you can pass unharmed")
        print ("3) use a military tactic called prodding where you crawl slowly and use a needle to poke around for mines")
        choice = input ("enter your choice:")
        if choice == "1":
            death()
        elif choice == "2":
            death()
        elif choice == "3":
            survive()
            print ("it is a slow method but it's full proof, your only real option.")
            print ("by the grace of God you get through the landmine field.")
            print ("you can see the land of prosperity in the distance causing you to be overwhelmed with joy.")
            print ("your joy is quickly ended when you see a beehemoth of a man wearing a bomb vest with 'trap' written on the front.")
            print ("the man starts running quickly at you and you must quickly decide what to do, you can only think of two options")
            print ("1) you run as fast as you can in hopes you can pass him and reach the gates of the land of prosperity.")
            print ("2) you throw your spear at the man in hope that it will blow him up far enough away from yourself.")
            choice = input ("enter your choice:")
            if choice == "1":
                death()
            elif choice == "2":
                survive()
                print ("you are lucky enough to be far enough from the explosion and you survive the explosion.")
                print ("you approach the gates to the land of prosperity and are welcomed with open arms, everyone is shocked because no one in 126 years have made it through the wasteland.")
                win()
    
    
