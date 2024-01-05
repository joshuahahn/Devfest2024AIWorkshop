# Devfest 2024 AI Workshop Outline
## Joshua Hahn jyh2134

### Outline
1. Guiding Questions
    - What makes a program "intelligent"?
    - How should we store movie data?
    - How can we define movie similarity?
    - How do we define a good recommendation?
    - Digging deeper:
        - KNN algorithm
        - Notions of distance
        - Time-efficient approximations
            - Sampling
                - Follow-up: modified bootstrap aggregation (bagging)
        - Space-efficient approximations
            - Lower-dimension vector embeddings
        - Hyperparameter tuning
            - Determining weights for weighted distance
        - Profile-based movie recommendation systems
            - How can we build a system that recommends movies to a user's spectrum of interests?

2. What makes a program "intelligent"?
    - Adaptability
    - Learning context

3. How should we store movie data?
    - Ask the audience: what is a reasonable way that we can turn movie data into something that the computer can store?
    - Vector-based embeddings
    - Representing in 1D, 2D, higher dimensions

4. How should we define movie similarity?
    - Given two points on the plane, how can we calculate movie similarity?
        - Euclidean distance
        - Manhattan distance
        - Weighted Euclidean / Manhattan distance
    - What are the pros and cons of each definition?
        - Euclidean distance
            - Pro: Intuitive definition of distance
            - Con: Can introduce awkward 
        - Manhattan distance
            - Pro: Easy to calculate
            - Con: No notion of weight (give an example where weight matters)
        - Euclidean distance
    - How can we determine the weights?
        - Hyperparameters

5. How do we define a good movie recommendation?
    - Ask audience what good notions of movie recommendations are
        - Closest movies?
            - Sometimes, a good movie recommendation system may focus on introducing new movies you may like.
            - In this case, may be far apart, but might be what the user wants.
        - For our case, we will define movies that are close together as good movies.