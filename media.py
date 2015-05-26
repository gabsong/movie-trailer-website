import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        
class Movie(Video):
    """docstring"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    def __init__(self, tv_title, duration, season, tv_episode, tv_station, local_listing):
        Video.__init__(self, tv_title, duration)
        self.season = season
        self.episode = tv_episode
        self.tv_station = tv_station
        self.local_listing_url = local_listing

    def get_local_listing(self):
        webbrowser.open(self.local_listing_url)
