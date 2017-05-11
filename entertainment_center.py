# Create multiple instances of class "Movie"

import media
import fresh_tomatoes


# Use the following format to add a new instance of class "Movie"
# movie_name = media.Movie("Title", "Storyline", "Image link", "Trailer Link")


guardians_galaxy = media.Movie("Guardians of the Galaxy",
                               "A group of intergalactic criminals are forced \
                               to work together to stop a fanatical warrior \
                               from taking control of the universe.",
                               "https://s3.us-east-2.amazonaws.com/bentocodeimages/GOTG-poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=B16Bo47KS2g")

fifth_element = media.Movie("The Fifth Element",
                            "In the colorful future, a cab driver unwittingly \
                             becomes the central figure in the search for a \
                             legendary cosmic weapon to keep Evil and Mr Zorg \
                             at bay.",
                            "https://s3.us-east-2.amazonaws.com/bentocodeimages/the-fifth-element.jpg",  # noqa
                            "https://www.youtube.com/watch?v=199EvXTKucc")


star_trek_darkness = media.Movie("Star Trek Into Darkness",
                                 "After the crew of the Enterprise find an \
                                 unstoppable force of terror from within \
                                 their own organization, Captain Kirk leads a \
                                 manhunt to a war-zone world to capture a \
                                 one-man weapon of mass destruction.",
                                 "https://s3.us-east-2.amazonaws.com/bentocodeimages/StarTrekIntoDarkness_FinalUSPoster.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=QAEkuVgt6Aw")

# movie_name = media.Movie("Title", "Storyline", "Image link", "Trailer Link")


movies = [guardians_galaxy, fifth_element,
          star_trek_darkness]  # Create a list of movies


# Open a web page to display the movies listed
fresh_tomatoes.open_movies_page(movies)
