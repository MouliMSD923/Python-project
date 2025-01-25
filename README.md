# Music Recommendation Engine
## A Statistical and Similarity-Based Approach for Personalized Music Discovery

## Introduction
The Music Recommendation Engine is designed to help users analyze music data, extract insights, and compute similarities between tracks and artists. The project aims to tackle information overload in music streaming services by providing statistical analysis and similarity-based recommendations based on track features such as acousticness, danceability, loudness, tempo, and valence.

This project strictly adheres to low-level Python programming principles such as data structutres, file handling, exception handling, etc, and does not use any high-level libraries such as pandas or numpy, as per the project constraints.

## Features
1. Load and parse music dataset files (data.csv & data_genres.csv).  
2. Perform statistical analysis (mean, variance, min, max) on music features.  
3. Compute similarity between tracks and artists using multiple similarity metrics:  
   Euclidean Distance  
   Cosine Similarity  
   Pearson Correlation  
   Jaccard Similarity  
   Manhattan Distance  
4. Interactive command-line interface for querying statistics and similarity calculations.  

All these functionalities are implemented in a modular approach.

## Future Enhancements  
1. GUI Implementation: A web-based or desktop interface for a better user experience.  
2. Machine Learning Integration: Implement ML-based recommendations using collaborative filtering.  
3. Database Storage: Use SQL/NoSQL databases for persistent data storage.  
4. Improved Performance: Optimize similarity computations for large datasets.   
