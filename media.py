import webbrowser


class Video():
    """Video: initializes media of type video.

    This is a parent class to Movie and TvShow.
      The __init__ method takes the most basic parameters that describe a
      video.

    Args:
      title (str): The title of the video.
      duration (str): The duration of the video in minutes.

    """

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """Movie: initializes media of type movie with all its attributes.

    This is a child class to Video and takes Video as a parameter.
      The __init__ method takes additional parameters exclusive to a movie.

    Args:
      movie_title (str): The title of the movie.
      duration (str): The duration of the movie in minutes.
      release_date (str): The release date as year.
      director (str): The director of the movie.
      storyline (str): One-sentence synopsis of the movie.
      poster_image (str): url string for an image format file on the web.
      trailer_youtube (str): url string for the trailer link on YouTube.

    Attributes:
      VALID_RATINGS (arr): global constant array, contains movie ratings.

    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, duration, release_date, director,
                 movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, duration)
        self.release_date = release_date
        self.director = director
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """show_trailer: opens and plays a trailer link in the web browser.

        """
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """TvShow: initializes media of type TV show with all its attributes.

    This is a child class to Video and takes Video as a parameter.
      The __init__ method takes additional parameters exclusive to a TV show.

    Args:
      movie_title (str): The title of the TV show.
      duration (str): The duration of the episode in minutes.
      season (str): The season where the episode belongs.
      tv_episode (str): The episode number within the season.
      tv_station (str): The station where the TV show airs.
      local_listing (str): url string for the local listing link.

    Attributes:
      VALID_RATINGS (arr): global constant array, contains movie ratings.

    """

    def __init__(self, tv_title, duration, season, tv_episode, tv_station,
                 local_listing):
        Video.__init__(self, tv_title, duration)
        self.season = season
        self.episode = tv_episode
        self.tv_station = tv_station
        self.local_listing_url = local_listing

    def get_local_listing(self):
        """get_local_listing: opens a local listing link in the web browser.

        """
        webbrowser.open(self.local_listing_url)
