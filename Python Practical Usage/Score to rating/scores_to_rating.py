def scores_to_rating (score1, score2, score3, score4, score5):
    """
    Turns five scores into rating by averaging the middle three of the five scores and assigning this average to a written ratingself.
    """
def convert_to_numeric(score):
    """
    Convert the score to a float.
    """
    return float(score)

def sum_of_the_middle_three(score):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    max_score = max(score1, score2, score3, score4, score5)
    min_score = min(score1, score2, score3, score4, score5)
    sum = (score1, score2, score3, score4, score5 - max_score - min_score)
    return sum

def score_to_rating_string(av_score):
    """
    Convert the average score, which should be between 0 to 5, into a rating.
    """
    if av_score < 1:
        rating = "Terrible"
    elif av_score <2:
        rating = "Bad"
    elif av_score <3:
        rating = "OK"
    elif av_score <4:
        rating = "Good"
    #Use Else at the very end
    else:
        rating = "Excellent"
    return rating
    #Step 1 Convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #Step 2 and 3 : Find the average of the middle three scores (-min and max)
    average_score = sum_of_the_middle_three(score1, score2, score3, score4, score5)/3

    rating = score_to_rating_string(average_score)

    return rating

print
