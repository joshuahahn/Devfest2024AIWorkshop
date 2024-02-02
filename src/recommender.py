import movie
import math

class Recommender:
    """A class that contains the movie dataset and recommendation methods"""
    
    def __init__(self, dataset_path='./dataset.txt', seen_path='./seenmovies.txt'):
        """Initializes the recommender class with the dataset path given."""
        csv = open(dataset_path)
        self.dataset = []
        for line in csv:
            tokens = line.split(",")
            title = tokens[0]
            vector = tokens[1:]
            self.dataset.append(movie.Movie(title, vector))
        csv.close()

        csv = open(seen_path)
        self.seen = []
        for line in csv:
            tokens = line.split(",")
            title = tokens[0]
            vector = tokens[1:]
            self.seen.append(movie.Movie(title, vector))
        csv.close()

    def distance(self, movie1, movie2, metric='Euclidean'):
        if metric == "Euclidean":
            return self.euclidean(movie1, movie2)
        elif metric == "Manhattan":
            return self.manhattan(movie1, movie2)

    def euclidean(self, movie1, movie2):
        distance = 0
        n = len(movie1)

        if len(movie2) != n:
            return -1 # Error

        for i in range(n):
            distance += (movie1[i] - movie2[i])**2
        
        return distance ** 0.5

    def manhattan(self, movie1, movie2):
        distance = 0
        n = len(movie1)

        if len(movie2) != n:
            return -1 # Error
        
        for i in range(n):
            distance += math.abs(movie1[i] - movie2[i])
        
        return distance
    
    def get_recommendation(self, metric='Euclidean'):
        minimum_distance = float('inf')
        recommendation = None

        for M in self.dataset:
            current_distance = 0

            for L in self.seen:
                current_distance += self.distance(M.vector, L.vector, metric)
            
            if current_distance < minimum_distance:
                minimum_distance = current_distance
                recommendation = M.name

        return recommendation
    
    def get_many_recommendations(self, k=10, metric='Euclidean'):
        movie_distances = []

        for M in self.dataset:
            current_distance = 0

            for L in self.seen:
                current_distance += self.distance(M.vector, L.vector, metric)
            
            movie_distances.append((current_distance, M.name))
        
        movie_distances.sort()

        recommendations = []
        for i in range(k):
            recommendations.append(movie_distances[i][1])
        return recommendations

a = Recommender()
recommendation = a.get_recommendation()
print("Single recommendation:\n" + recommendation)
print("===============================")
recommendations = a.get_many_recommendations()
print("Mutiple Recomendations: ")
for recommendation in recommendations:
    print(recommendation)