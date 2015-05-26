import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "100 min", 
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)

avatar = media.Movie("Avatar", "140 min", 
                     "A marine on an alien palnet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print(avatar.storyline)
# avatar.show_trailer()

inception = media.Movie("Inception", "120 min", 
                        "A thief who can extract secrets from people's dreams goes on his last mission: implant an idea",
                        "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

# print(inception.storyline)
# inception.show_trailer()

movies = [toy_story, avatar, inception]
# fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)

print(inception.title)
print(inception.duration)
