#this py has a conditional
print ("enter racer name:")
name = input ("")
print ("enter car number:")
car = input ("")
print (f"{name}, you have gone down in history as one of the best 12 car drivers in history and if you win this tournament, you will be put in the 12 car hall of fame.")
print ("this tournament is your lastn and you aren't off too a great start.")
print ("you have lost every race you have participated in this year which normally causes you to be eliminated from the 12 car championship race, due to a cheating racer you have been told to pick a number from 1-12 to determin whether or not you will be the 12th racer.")
x = input ("what number will it be:")
if x > "3":
    print ("you are removed from the championship race, never choose to be off the podium.")
elif x <= "3":
    print ("you are approved as the 12th racer.")
    print ("now that you have been aproved you must get your head in the game, what will you do to prepare for the race?")
    print ("1) drink a coffee and eat some small sugary biscuts.")
    print ("2) listen to hype music and call your wife.")
    print ("3) go over a game plan with your crew and review your lines for the track.")
    print ("4) drink a beer and hope for the best.")
    choice = input ("enter your choice:")
    if choice == "1":
        print ("you get sick before the race and can't participate.")
        exit()
    elif choice == "2":
        print ("your wife distracts you from the race at hand.")
        exit()
    elif choice == "4":
        print ("you idiot, you can't drink before a race.")
        exit()
    elif choice == "3":
        print ("you and your crew come up with a good plan and you find new lines for the track.")
        print ("you now line up, do your practice lap and warm up your tires, you are ready for the last race of your career.")
        print ("the race begins in 3...2...1...GO!!!")
        print ("you have a great start in this 5 lap race and pass 7 of the 12 racers.")
        print ("your in 5th place after the third lap, you must find a way to pass the rest of the opposition.")
        print ("the 4th place racer crashes into the 3rd place racer causing a stop in the race, due to this both the 4th and 3rd place racers can't continue to race.")
        print ("you are now in 3rd, how will you pass the remaining 2 racers to win your final race?")
        print ("1) stick to the original lines in hope that you'll pass both drivers.")
        print ("2) you crash into both drivers too knock them out of the race.")
        print ("3) you slam on the gas and go faster than the recommended speed on turns in hope that your worn tires will hold.")
        print ("4) you attempt the new lines you saw when going over the track before the race even though it isn't proven to be the best route.")
        choice = input ("enter your choice:")
        if choice == "1":
            print ("you manage to pass the 2nd driver but the lines where not good enough to pass the 1st driver.")
            exit()
        elif choice == "2":
            print ("you are ejected from the race and shamed, you will no longer have the chance to be in the hall of fame.")
        elif choice == "3":
            print ("your tires blow up and you slam into the wall")
            exit()
        elif choice == "4":
            print ("your new lines where more optimal than both the 2nd and 1st driver, you win the race!!!")
            print (f" as {name} stands on the podium for the last time holding the cup he is content with his accomplishments and can finally retire {car} from use in 12 car racing.")
            
        
        
    
    
    