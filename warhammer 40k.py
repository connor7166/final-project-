print ("you are a sergeant space marine heading into the heat of battle against the tyranids.")
print ("you are on the dropship when the captain approaches you to discuss your mission.")
print ("what is your name brother?")
name = input("")
print (f"greetings {name}, what is your call sign?")
call_sign = input("")
print (f"praise be to the Emperor, I've heard great stories of your endeavors, you are a great asset to the Imperium.")
print ("tyranids have swarmed a near by area and we have been tasked to purge the heretics before they advance towards our fortress-monastery.")
print (f"alright brothers we are about to land, prepare to advance and push back the enemy tyranids,follow {call_sign}'s lead.")
print (f"{call_sign}, prepare for battle.")
print ("you get off the dropship and quicky must decide where to advance.")
print ("1) advance towards multiple tall bushes.")
print ("2) advance towards a large open field with barriers and machine guns set up from the faction's attempt before you.")
print ("3) advance towards a dug out tunnel that is unkown and unlit.")
print ("4) advance towards tyranid hive in the distance surrounded by trees.")
choice = input("enter your choice:")
if choice == "1":
    print ("tyranids hid in the bushes and ambush your entire faction.")
    exit()
elif choice == "3":
    print ("as your faction approaches the tunnel, swarms of tyranids come out and slaughter you and your faction.")
    exit()
elif choice == "4":
    print ("there is a strong defense at the hive, you burn out 35% of the hive but are overwhelmed.")
    exit()
elif choice == "2":
    print ("there are plenty of supplies prepared and multiple lanes to create a stronghold from the tyranids.")
    print ("the tyranids quickly find your presence and prepare to advance on your position, multiple hormagaunts and termagants swarm from all directions towards your stronghold.")
    print ("1) have the majority of your soldiers man the machine guns while a remaining few use their bolt pistols and bolt carbines to add suppresion fire towards the swarm.")
    print ("2) rush the tyranids with chain swords in hope of protection from your power armor.")
    print ("3) ignore the machine guns and blast away at the tyranids with bolt pistols and bolt carines.")
    print ("4) call in a bomb barrage on your position while hiding behind the barriers.")
    choice = input("enter your choice:")
    if choice == "2":
        print ("your power armor is not strong enough to advert the damage from the heretics.")
        exit()
    elif choice == "3":
        print ("you hold them away at first but eventually there numbers overwhelm you.")
        exit()
    elif choice == "4":
        print ("the bomb barrage is not permitted leaving you with no time to defend yourselves as the tyranids are already swarming your stronghold.")
        exit()
    elif choice == "1":
        print ("you shoot through the hoard of heretics, covering the field with the tyranids remains.")
        print ("you thought that your mission was complete but out of nowhere leapers come down from the sky a few meters ahead of your stronghold.")
        print ("1) take on the leapers with your chain swords.")
        print ("2) once again have your remaining troops man the machine guns and mow down the leapers.")
        print ("3) empty your magaines at the leapers.")
        print ("4) have the flamers of the faction shoot flames towards the leapers while you shoot at them from the sides.")
        choice = input ("enter your choice:")
        if choice == "1":
            print ("the leapers are too strong of melee opponets to succeed.")
            exit()
        elif choice == "2":
            print ("the leapers are to agile for your faction to precisely land enough rounds to hold the leapers back.")
            exit()
        elif choice == "3":
            print ("the leapers are to agile for your faction to precisely land enough rounds to hold the leapers back.")
            exit()
        elif choice == "4":
            print ("the flames hold off the leapers and leave them vulnerable, allowing the rest of the faction to finish off the leapers with their bolt pistols and bolt carbines.")
            print ("the land has been purged of the heretics and you return back to your fortress-monastery held with high regard, praise be to the emperor.")
    