points = 180
def which_prize(points):
    if points <= 50 :
        print ("Congratulations! You have won a wooden rabbit!")
    elif points <= 150:
        print ("Oh dear, no prize this time.")
    elif points <= 180:
        print ("Congratulations! You have won a wafer-thin mint!")
    else :
        print ("Congratulations! You have won a penguin!")

which_prize(points)
