

def load_data(artist_file,music_file):
    
    try:
        
        with open(artist_file,'r',encoding='utf8') as artist_file:        # READING THE CONTENTS IN THE ARTIST DATA SET USING FILE HANDLING SYSTEM
            lines=artist_file.readlines()

    except FileNotFoundError:                                            # HANDLING THE FILE NOT FOUND ERROR
        print('FILE  NOT FOUND. REPLACE WITH APPROPRIATE FILE')

    headers=lines[0].strip().split(',')                                  # READ THE HEADERS FROM THE FILE. AS IT PRESENTS IN THE FIRST ROW
    rows=[line.strip().split(',') for line in lines[1:]]                 # READING ALL THE ROWS, SPLITTING BY (',') AND STORE THE VALUES IN A LIST
    
    artist_data=[]
    for row in rows:
        if len(row) == len(headers):
            artist_data.append(dict(zip(headers,row)))                  #APPENDING THE VALUES ALONG WITH THEIR HEADER AS A LIST OF DICTIONARIES

    artist_music={}                                                     # CREATING AN EMPTY DICTIONARY FOR STORING ALL THE RECORDS ALONG WITH THEIR INDEX VALUE
    index=0
    for data in artist_data:
        artist_music[index] = {                                          
            'valence': float(data['valence']),                          # EXTRACTING THE NECESSARY FEATURES FROM THE DATASET AND CONVERT THE NUMERICAL VALUES INTO FLOAT VALUES
            'acousticness': float(data['acousticness']),
            'artists': data['artists'],
            'danceability': float(data['danceability']),
            'energy': float(data['energy']),
            'id': data['id'],
            'liveness': float(data['liveness']),
            'loudness': float(data['loudness']),
            'name': data['name'],
            'popularity': float(data['popularity']),
            'speechiness': float(data['speechiness']),
            'tempo': float(data['tempo']),
        }
        index+=1
        


    music_features={}                                            # CREATING AN EMPTY DICTIONARY FOR STORING THE MUSIC GENRES FEATURES
    index=0
    
    with open(music_file,'r') as music_file:                  # READING THE CONTENTS IN THE MUSIC GENRES DATASET USING FILE HANDLING
        music_file.readline()

        for data in music_file:                                   # EXTRACTING THE NECESSARY FEATURES FROM THE MUSIC GENRES DATASET BY SPLITTING THE DATA USING (',') AS A SEPARATOR
            mode,genres,acousticness,danceability,duration_ms,energy,instrumentalness,liveness,loudness,speechiness,tempo,valence,popularity,key=data.rstrip('\n').split(',')[0:]
            music_features[index]={'mode':float(mode),
                                   'genres':genres,
                                   'acousticness':float(acousticness),
                                   'danceability':float(danceability),
                                   'duration_ms':float(duration_ms),
                                   'energy':float(energy),
                                   'instrumentalness':float(instrumentalness),
                                   'liveness':float(liveness),
                                   'loudness':float(loudness),
                                   'speechiness':float(speechiness),
                                   'tempo':float(tempo),
                                   'valence':float(valence),
                                   'popularity':float(popularity),
                                   'key':float(key)}
            index+=1

    return artist_music,music_features                             # Returning two dictionaries artist_music and music_features


    


