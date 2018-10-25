import Media
import movies_page
#instance = toystory
#constructor for ex - init
toy_story = Media.Movie("Toy Story", "A story of a boy and his toys that comes to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avengers_IW = Media.Movie("Avengers Infinity War", "Heroes around the universe fight against thanos ", "http://www.impawards.com/2018/posters/avengers_infinity_war_ver2.jpg", "https://www.youtube.com/watch?v=6ZfuNTqbHE8&feature=youtu.be")
                     
movies = [toy_story, avengers_IW]
movies_page.open_movies_page(movies)
