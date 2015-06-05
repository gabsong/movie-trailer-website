# coding=utf-8

import media

# The instances of class Movie below store all the relevant movie properties
# as defined in media.py

toy_story = media.Movie("Toy Story",
                        "81 min",
                        "1995",
                        "John Lasseter",
                        "A cowboy toy is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "162 min",
                     "2009",
                     "James Cameron",
                     "A Paraplegic Marine becomes torn between following his orders and protecting the world he feels is his home.",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

inception = media.Movie("Inception",
                        "148 min",
                        "2010",
                        "Christopher Nolan",
                        "A thief who can extract secrets from people's dreams goes on his last mission: implant an idea.",
                        "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

breakfast_at_tiffanys = media.Movie("Breakfast at Tiffany's",
                                    "115 min",
                                    "1961",
                                    "Blake Edwards",
                                    "A young New York socialite becomes interested in a young man who has moved into her apartment building.",
                                    "http://upload.wikimedia.org/wikipedia/en/a/a9/Breakfast_at_Tiffanys.jpg",
                                    "https://youtu.be/-XcLVQCDtbM")

great_expectations = media.Movie("Great Expectations",
                                 "111 min",
                                 "1998",
                                 "Alfonso Cuarón",
                                 "The hapless Finn as a painter in New York pursues his unrequited and haughty childhood love.",
                                 "http://upload.wikimedia.org/wikipedia/en/5/53/Great_expectations_poster.jpg",
                                 "https://youtu.be/6bq8BsIZejE")

lovers_concerto = media.Movie("Lover's Concerto",
                              "106 min",
                              "2002",
                              "Han Lee",
                              "Ji-Hwan departs on a long journey to find his old friends as he confronts a beautiful yet sad secret.",
                              "http://imgmovie.naver.com/mdi/mi/0343/C4362-00.jpg",
                              "https://youtu.be/qdxemeCrqHw")

interstellar = media.Movie("Interstellar",
                           "169 min",
                           "2014",
                           "Christopher Nolan",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg",
                           "https://youtu.be/0vxOhd4qlnA")

leon_the_professional = media.Movie("Léon: The Professional",
                                    "110 min",
                                    "1994",
                                    "Luc Besson",
                                    "Léon and Mathilda form an unusual relationship, as she becomes his protégée and learns the assassin's trade.",
                                    "http://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",
                                    "https://youtu.be/AEYXe8MXuZo")

the_departed = media.Movie("The Departed",
                           "151 min",
                           "2006",
                           "Martin Scorsese",
                           "An undercover cop and a mole in the police attempt to identify each other while infiltrating a gang.",
                           "http://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
                           "https://youtu.be/auYbpnEwBBg")

# The array movies stores the all the movie objects created above.
movies = [toy_story, avatar, inception, breakfast_at_tiffanys, great_expectations, lovers_concerto, interstellar, leon_the_professional, the_departed]
