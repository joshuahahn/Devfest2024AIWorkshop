"""
Joshua Hahn
Jan 2024
"""

import random
from numpy import random as nprandom
import movie

# Global genre list
GENRES = ["Action", "Romance", "Mystery", "Comedy", "Horror", "Crime", "Thriller"]
VEC_LENGTH = len(GENRES)

# Global attribute list
ATTRIBUTES = ["Amazing", "Awesome", "Boring", "Cool", ]

# Global movie name list
TYPE = ["Movie", "Indie Film", "Film", "Animation", "Live-action Film"]


def generate_movie():
    """
    Generates a movie object with randomly generated attributes.
    One movie is selected as the 'primary genre' with a normal 
    distribution centered around 7, and another movie is selected as the 
    'secondary genre' with a normal distribution centered around 4.
    Every other genre gets some small noise.
    """

    primary_genre = random.randint(0,VEC_LENGTH-1)
    secondary_genre = random.randint(0,VEC_LENGTH-1)
    if secondary_genre == primary_genre:
        secondary_genre = (secondary_genre + random.randint(1, VEC_LENGTH-1)) % VEC_LENGTH

    vector = [0] * VEC_LENGTH
    vector[primary_genre] = min(10, nprandom.normal(7, 0.7))
    vector[secondary_genre] = min(10, nprandom.normal(4, 0.7))

    for i in range(VEC_LENGTH):
        vector[i] = min(10, vector[i] + nprandom.normal(1, 0.3))

    title = []
    title.append(random.choice(ATTRIBUTES))
    title.append(GENRES[primary_genre])
    title.append(GENRES[secondary_genre])
    title.append(random.choice(TYPE))
    title = " ".join(title)

    return (title, vector)

def generate_dataset(n=100):
    file = open('dataset.txt', 'w')
    for _ in range(n):
        title, vector = generate_movie()
        curr_line = [title] + vector
        for i in range(1, len(curr_line)):
            curr_line[i] = str(curr_line[i])
        file.write(','.join(curr_line))
        file.write('\n')
    file.close()

generate_dataset()
        