import random
global hoursleft
global energyleft

def treasure_search():
    treasureinput = input ("Time for a Treasure hunt! /ᐠ｡ꞈ｡ᐟ✿\ \n type 'look' to look for treasure. \n type 'return' to go back to menu.")
    if treasureinput == "look":
        searchtime = 0
        while searchtime == 0: 
            print ("you found...")
            treasure = random.randint(0,10)
            if treasure == 0 or 1 or 2:
                print ("Pom poms! Fluffy balls of playtime fun. \n /ᐠ=ᆽ=ᐟ\"")
            if treasure == 3 or 4:
                print ("Bottle Caps! A reminder to recycle…  \n ฅ/ᐠ｡ᆽ｡ᐟ\"")
            if treasure == 5 or 6:
                print ("Hair ties - 36 of them! You counted them yourself.\n /ᐠ=ᆽ=ᐟ\"")
            if treasure == 7:
                print ("One half of a pair of socks. They say once the other is found, the user gets great power. \n ✧/ᐠ-ꞈ-ᐟ\ ")
            if treasure == 8 or 9:
                ouch = input ("An Old Christmas Ornament. Christmas always comes too early. Knock it off the counter? (y or n)")
                if ouch == "y":
                    if treasure == 8:
                        print ("Ouch! You cut your paw on the sharp ornament. You need time to lick your wound clean. It takes an hour! \n  /ᐠᵕ̥ꞈᵕ̩̥ ᐟ\ﾉ")
                        hoursleft = hoursleft - 1
                    else:
                        print ("CRASH!!! Off it goes. Let's hope your owner notices. \n /ᐠ.ꞈퟑ.ᐟ\"")
            print ("Energy - .5, 1 hour spent playing.")
            hoursleft = hoursleft - 1
            energyleft = energyleft - .5
            searchagain1 = input ("Search Again? (y or n)")
            if searchagain1 == "y":
                searchtime == 1
            if searchagain1 == "n":
                break            
        

def main():
    startgame = input ("It’s time to live out your feline dreams! \n You have 12 hours to do everything a housecat would do. \n Pay attention to both the time you have left in the day and your energy bar. \n Most activities will give you a choice of possible options, and depending on your choice, different things will happen. \n Follow the instructions for inputs, and have fun! \n  ✧/ᐠ-ꞈ-ᐟ\ \n Would you like to play or exit?")
    if startgame == "play":
        hoursleft = 12
        energyleft = 10
        print ("Good Morning, Whiskers! It's a wonderful day to be a cat.")
        while hoursleft > 0 and energyleft > 0: 
            action = input ("What would you like to do? Hours: [hoursleft] Energy: [energyleft] \n To Pester Owner, Press 1. \n To Play with Toys, Press 2. \n To Take a Nap, Press 3. \n To Go in the Yard, Press 4. \n To Search for Treasures, Press 5. \n To Grab a Snack, Press 6. \n To Exit, Press 7." )
            if action == "1":
                pester_owner()
            elif action == "2":
                toy_play()
            elif action == "3":
                take_nap()
            elif action == "4":
                go_yard()
            elif action == "5":
                treasure_search()
            elif action == "6":
                grab_snack()
            elif action == "7":
                break
        print ("Looks like the day is over! What a wonderful cat day. \n You had [hoursleft] hours left and [energyleft] energy left.")
        print ("Thank you for playing with us today! \n /ᐠ . ֑ . ᐟ\ﾉ")
    elif startgame == "exit":
        print ("Thank you for playing with us today! \n /ᐠ . ֑ . ᐟ\ﾉ")

main()
