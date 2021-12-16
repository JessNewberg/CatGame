import random

def go_yard():
    print ("\n * \n * \n * \n * \n * \n")
    yardinput = input ("what a nice day it is! truly beautiful. \n /ᐠ‸⑅‸ ᐟ\ﾉ \n Would you like to play outside? type 'play' to find something to do in the yard. \n type 'return'to go back to menu.")
    if yardinput == "play":
        yardtime = 0
        while yardtime == 0:
            yardplay = random.randint(0,10)
            if yardplay == 0:
                print ("...nothing to do. what a cat-astrophe.")
            elif yardplay == 1 or yardplay == 2:
                print ("You got the zoomies! Runrunrunrunrunrunrun! \n /ᐠⓛ ﻌ ⓛᐟ\)")
            elif yardplay == 3 or yardplay == 4:
                print ("You found an excellent sunny spot, and decide to doze in it for a while.\n /ᐠ=ᆽ=ᐟ\"" )
            elif yardplay == 5 or yardplay == 6:
                print ("APEX PREDATOR!!! You stalk a bird in a tree, and then POUNCE. \n sadly, it escapes. Maybe next time. /ᐠﹷ ‸ ﹷ ᐟ\ﾉ")
            elif yardplay == 7:
                print ("No better place to groom yourself than outside... you have to look your best at all times. \n ✧/ᐠ-ꞈ-ᐟ\ ")
            elif yardplay == 8 or yardplay == 9:
                uhoh = input ("OH NO! The neighbors have their vicious dog out! \n  /ᐠ۪. ̱ .۪ᐟ\ﾉ \n It's on the other side of the fence, so it can't get to you... \n do you want to hiss at it or go inside? \n (you can come back out later.) input 'hiss' or 'inside'. ")   
                if uhoh == "hiss":
                    print ("you yowl and hiss at the dog... and he runs away. what a ferocious creature you are! \n /ᐠ ̥  ̮  ̥ ᐟ\ฅ")
                if uhoh == "inside":
                    print ("time to go inside! very wise.")
                    break
            playagain1 = input ("Play More in the Yard? (y or n)")
            if playagain1 == "y":
                yardtime == 0
            if playagain1 == "n":
                break
        
def treasure_search():
    print ("\n * \n * \n * \n * \n * \n")
    treasureinput = input ("Time for a Treasure hunt! /ᐠ｡ꞈ｡ᐟ✿\ \n type 'look' to look for treasure. \n type 'return' to go back to menu.")
    if treasureinput == "look":
        searchtime = 0
        while searchtime < 1: 
            print ("you found...")
            treasure = random.randint(0,10)
            if treasure == 0:
                print ("...nothing. what a cat-astrophe.")
            if treasure == 1 or treasure == 2:
                print ("Pom poms! Fluffy balls of playtime fun. \n /ᐠ=ᆽ=ᐟ\"")
            if treasure == 3 or treasure == 4:
                print ("Bottle Caps! A reminder to recycle…  \n ฅ/ᐠ｡ᆽ｡ᐟ\"")
            if treasure == 5 or treasure == 6:
                print ("Hair ties - 36 of them! You counted them yourself.\n /ᐠ=ᆽ=ᐟ\"")
            if treasure == 7:
                print ("One half of a pair of socks. They say once the other is found, the user gets great power. \n ✧/ᐠ-ꞈ-ᐟ\ ")
            if treasure == 8 or treasure == 9:
                ouch = input ("An Old Christmas Ornament. Christmas always comes too early. Knock it off the counter? (y or n)")
                if ouch == "y":
                    if treasure == 8:
                        print ("Ouch! You cut your paw on the sharp ornament. /ᐠᵕ̥ꞈᵕ̩̥ ᐟ\ﾉ")
                    else:
                        print ("CRASH!!! Off it goes. Let's hope your owner notices. \n /ᐠ.ꞈퟑ.ᐟ\"")
            searchagain1 = input ("Search Again? (y or n)")
            if searchagain1 == "y":
                searchtime == 0
            if searchagain1 == "n":
                break

def grab_snack():
    print ("\n * \n * \n * \n * \n * \n")
    snackinput = input ("Eating: One of a cat's favorite chores. \n Thankfully, your owner has recently filled your wet food and dry food bowl! \n ᶠᵉᵉᵈ ᵐᵉ /ᐠ-ⱉ-ᐟ\ﾉ \n would you like wet food, dry food, or.... something else? \n For Wet Food, Press 1. For Dry Food, Press 2. For Something else... Press 3.")
    if snackinput == "1":
        print ("Yum! A delicious, crunchy snack. +1 health! (Just Kidding.) \n /ᐠ ̥ ̣̮ ̥ ᐟ\ﾉ")
    elif snackinput == "2":
        print ("This stuff smells awful, but it is definitely wet. \n /ᐠ . ֑ . ᐟ\ﾉ")
    elif snackinput == "3":
        weirdsnack = input ("You want to eat... something else? Whatever floats your boat,I guess. \n What do you want to eat? (Type anything!)")
        print ("Alright, you eat " + weirdsnack + ". Not very nutritious.")
    else: "Sorry, that isn't a valid input. Please type 'return' to return to the selection menu."
    

def main(username):
    print ("Hello, " + username + "!")
    startgame = input ("It’s time to live out your feline dreams! \n \n Most activities will give you a choice of possible options, and depending on your choice, different things will happen. \n Follow the instructions for inputs, and have fun! \n  ✧/ᐠ-ꞈ-ᐟ\ \n Would you like to play or exit?")
    if startgame == "play":
        print ("\n * \n * \n * \n")
        gametime = 1
        print ("Good Morning, Whiskers! It's a wonderful day to be a cat.")
        while gametime > 0:
            print ("\n * \n * \n * \n * \n * \n")
            action = input ("What would you like to do? \n To Pester Owner, Press 1. \n To Play with Toys, Press 2. \n To Take a Nap, Press 3. \n To Go in the Yard, Press 4. \n To Search for Treasures, Press 5. \n To Grab a Snack, Press 6. \n To Exit, Press 7." )
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
                gametime = gametime - 1
            else:
                print ("Sorry, that isn't a valid input.")
                break
        print ("\n * \n * \n * \n * \n * \n")
        print ("Looks like the day is over! What a wonderful cat day.")
        print ("Thank you for playing with us today! \n /ᐠ . ֑ . ᐟ\ﾉ")
    elif startgame == "exit":
        print ("Thank you for playing with us today! \n /ᐠ . ֑ . ᐟ\ﾉ")

main("User")
