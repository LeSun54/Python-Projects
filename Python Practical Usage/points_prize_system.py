def which_prize(points):
#"""Returns the number of prize-winning message, given a number of points"""
    prize = None
    if points <= 50 :
        prize =  "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181 :
        prize = "a penguin"

    if prize:
        print("Congradulation! You have won " + prize + "!")
    else:
        print("Oh dear, no prize this time.")

which_prize (152)
