import media
import fresh_tomatoes
import os


# This creates a relative path for the file images
directory = os.path.dirname(__file__)
image_file_mbr2049   = os.path.join(directory, "images", "mbr2049.jpg")
image_file_mavatar   = os.path.join(directory, "images", "mavatar.jpg")
image_file_matrix    = os.path.join(directory, "images", "matrix.jpg")
image_file_elysium   = os.path.join(directory, "images", "elysium.jpg")
image_file_mm        = os.path.join(directory, "images", "mm.jpg")
image_file_mautomata = os.path.join(directory, "images", "mautomata.jpg")

# Instances of the movie class to be passed to fresh_tomatoes
blade_runner2049 = media.Movie(
    "Blade Runner 2049",
    "A Cop seeks answers to avert war.",
    image_file_mbr2049,
    "https://www.youtube.com/watch?v=gCcx85zbxz4"
    )


avatar = media.Movie(
    "Avatar",
    "A story about a Marine on an alien planet.",
    image_file_mavatar,
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )


matrix = media.Movie(
    "The Matrix",
    "A hacker learns of the real world.",
    image_file_matrix,
    "https://www.youtube.com/watch?v=tGgCqGm_6Hs"
    )


elysium = media.Movie(
    "Elysium",
    "A dying man seeks life on the most guarded place in the universe.",
    image_file_elysium,
    "https://www.youtube.com/watch?v=oIBtePb-dGY"
    )

mad_max = media.Movie(
    "Mad Max: Fury Road",
    "A story of survival in a post apocalyptic world.",
    image_file_mm,
    "https://www.youtube.com/watch?v=hEJnMQG9ev8"
    )


automata = media.Movie(
    "Automata",
    "A cop learns of machines fixing themselves.",
    image_file_mautomata,
    "https://www.youtube.com/watch?v=Wh_wmaOZcWo"
    )

# Movies list to be used by fresh_tomatoes for proper formatting
movies = [blade_runner2049, avatar, matrix, elysium, mad_max, automata]
fresh_tomatoes.open_movies_page(movies)
