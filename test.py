import entertainment_center
import fresh_tomatoes
import media

# Tests for media.Movie methods
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)

# This code executes the code in fresh_tomatoes.py and entertainment_center.py
# A static page with the movies defined in entertainment_center gets generated
fresh_tomatoes.open_movies_page(entertainment_center.movies)
