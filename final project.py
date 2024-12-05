#the goal is to make multiple text adventure games and allow the user to pick which game they want to play.
#I will make three text adventures and use my original text adventure to be equivalent to three labs done on my own and a additional previos lab just for a additional game and then I will use things learned further in the semester and tie it in.
#I will make each text adventure in a seperate py file and then will have the player choose one of the three games and the code will call the given game.
#this py file has a list and a loop
print ("game library:")
my_list = ["warhammer 40k.py", "the last race.py", "wasteland.py"]
for i in my_list:
    print (i)

filename = input ("enter game you'd like to play (enter full title with .py):")
handle = open(filename)
exec(handle.read())


