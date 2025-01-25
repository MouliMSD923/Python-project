import math

def euclidean_similarity(feature1,feature2):          # CALCULATING THE ECULIDEAN DISTANCE BETWEEN TWO FEATURES
    sum_of_squares=0
    for i in range(len(feature1)):
        sum_of_squares+=((feature1[i]-feature2[i])**2)
    ecu_similarity = math.sqrt(sum_of_squares)
    return ecu_similarity

def cosine_similarity(feature1,feature2):              # CALCULATING THE COSINE SIMILARITY BETWEEN TWO FEATURES
    sum_of_product=0
    sum_of_squares_feature1 = 0
    sum_of_squares_feature2 = 0
    for m,n in zip(feature1,feature2):
        sum_of_product+=(m * n)
        sum_of_squares_feature1+=(m*m)
        sum_of_squares_feature2+=(n*n)
    return sum_of_product /(math.sqrt(sum_of_squares_feature1) * math.sqrt(sum_of_squares_feature2))
    

def pearson_similarity(feature1,feature2):            # CALCULATING THE PEARSON SIMILARITY BETWEEN TWO FEATURES
    covarience=0
    std_feature1 = 0
    std_feature2 = 0
    feature1_mean=sum(feature1)/len(feature1)
    feature2_mean=sum(feature2)/len(feature2)
    for a,b in zip(feature1,feature2):
        covarience+=((a-feature1_mean) * (b-feature2_mean))
        std_feature1+=(a-feature1_mean)**2
        std_feature2+=(b-feature2_mean)**2
    return covarience / (math.sqrt(std_feature1)*(math.sqrt(std_feature2)))

    

def jaccard_similarity(feature1,feature2):                  # CALCULATING THE JACCARD SIMILARITY BETWEEN TWO FEATURES
    features_intersection = len(set(feature1) & set(feature2))
    features_union = len(set(feature1) | set(feature2))
    jaccard_distance = features_intersection / features_union
    return jaccard_distance


def manhattan_similarity(feature1,feature2):                # CALCULATING THE MANHATTAN SIMILARITY BETWEEN TWO FEATURES
    manhattan_distance=0
    for i in range(len(feature1)):
        manhattan_distance+=abs(feature1[i]-feature2[i])
    return manhattan_distance


def similarity_between_tracks(music_data,id1,id2,sim_fun):              # FUNCTION FOR CALCULATING THE SIMILARITIES BETWEEN TWO MUSIC TRACKS
    id1_values=list(music_data[id1].values())
    id2_values=list(music_data[id2].values())                           # EXTRACRTING THE VLAUES FROM THE DICTIONARY AND CONVERTING INTO LIST
    id2_values.pop(1)
    id1_values.pop(1)                                                   # REMOVING THE OBJECT DATA FROM THE LIST OF VALUES USING POP FUNCTION
    return sim_fun(id1_values,id2_values)

def similarity_between_artists(artist_data,id1,id2,sim_fun):            # FUNCTION FOR CALCULATING THE SIMILARITIES BETWEEN TWO ARTIST ID'S
    artist1_id_values=list(artist_data[id1].values())
    artist2_id_values=list(artist_data[id2].values())                   # EXTRACRTING THE VLAUES FROM THE DICTIONARY AND CONVERTING INTO LIST
    artist1_id_values.pop(2)
    artist1_id_values.pop(4)
    artist1_id_values.pop(6)                                             # REMOVING THE OBJECT DATA FROM THE LIST OF VALUES USING POP FUNCTION
    artist2_id_values.pop(2)
    artist2_id_values.pop(4)
    artist2_id_values.pop(6)
    return sim_fun(artist1_id_values,artist2_id_values)