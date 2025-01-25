''' IMPORTING THE OTHER THREE MODULES INTO THE MAIN MODULE BY USING THE IMPORT STATEMENT'''

from load_data_module import load_data
from stats_module import mean,mode,variance,standard_deviation,maximum,minimum
from similarity_module import euclidean_similarity,cosine_similarity,pearson_similarity,jaccard_similarity,manhattan_similarity,similarity_between_tracks,similarity_between_artists



def main():
    artist_data,music_data=load_data('data.csv','data_genres.csv')     # LOADING THE DATASETS
    while True:
        print('****Menu****')                                                                 # MENU FOR THE USER TO CALCULATE THE STATS VALUES, SIMILARITY VLAUES OF DIFFERENT FEATURES 
        print('Enter 1 for finding statistical values of the data')
        print('Enter 2 for finding similarities between music features')
        print('Enter 3 for finding similarities between music tracks')
        print('Enter 4 for finding similarities between artists')
        print('Enter 5 for exit the program')

        option = input('Enter your choice from the above Main menu : ')                      # SEEKING INPUT FROM USER

        if option == '1':
            print('Statistical Menu: ')                                       # MENU FOR CALCULATING DIFFERENT STATISTICAL VALUES
            print('Enter 1 for finding  Mean ')
            print('Enter 2 for finding Mode')
            print('Enter 3 for finding variance')
            print('Enter 4 for finding standard Deviation')
            print('Enter 5 for finding Maximum value')
            print('Enter 6 for finding Minimum value')

            statistical_choice=input('Enter your choice from the above statistical menu: ')      # USER ENTER THE CHOICE FROM THE STATISTICAL MENU
            print('Features:  mode,acousticness, danceability,duration_ms,energy,instrumentalness,liveness,loudness,speechiness,tempo,valence,popularity,key')
            feature = input(' Enter the feature name to analyze the data using statistical functions : ')
            feature_data=[]
            count=0
            for tracks in music_data.values():
                feature_data.append(tracks[feature])                 # EXTRACTING THE VALUES FROM THE FEATURE FOR FINDING THE STATISTICAL VALUE
                count+=1

            if statistical_choice == '1':
                print(f'Mean of feature {feature} : {mean(feature_data)}')
            elif statistical_choice == '2':
                print(f'Mode of feature{feature} : {mode(feature_data)}')
            elif statistical_choice == '3':
                print(f'variance of  {feature} : {variance(feature_data)}')
            elif statistical_choice=='4':
                print(f'Standard Deviation of {feature} : {standard_deviation(feature_data)}')
            elif statistical_choice=='5':
                print(f'Maximum  value of {feature} : {maximum(feature_data)}')
            elif statistical_choice == '6':
                print(f'Minimum value of {feature} : {minimum(feature_data)}')
            else:
                print('Invalid Choice. Please enter the valid option from the above list of statistical functions ')

        elif option == '2':
            print('Features:  mode, acousticness, danceability, duration_ms, energy, instrumentalness, liveness, loudness, speechiness, tempo, valence, popularity, key')
            print('Enter the features from the above list of options :')  # PRINTING THE LIST OF FEATURES FOR SELECTING TWO FEATURES
            feature1 = input('Enter the first feature to find the similarity :')
            feature2 = input('Enter the second feature to find the similarity :')
            feature1_values=[]
            count1=0
            for tracks in music_data.values():
                feature1_values.append(tracks[feature1])             # EXTRACTING THE FIRST FEATURE VALUES
                count1+=1

            feature2_values=[]
            count2=0
            for tracks in music_data.values():
                feature2_values.append(tracks[feature2])             # EXTRACTING THE SECOND FEATURE VALUES
                count2+=1
            ''' 
            PRINTING THE LIST OF SIMILARITY FUNCTIONS FOR CHOOSING ONE OF THE FUNCTION FOR CALCULATING 
            THE SIMILARITIE SCORES BETWEEN TWO FEATURES ENTERED BY THE USER

            '''
            similarity = input('Enter the similarity function 1.euclidean 2.cosine 3.pearson 4.jaccard 5.manhattan :').strip().lower() 
            if similarity == 'euclidean':
                print(f'Euclidean similarity between {feature1} and {feature2} : {euclidean_similarity(feature1_values,feature2_values)}')
            elif similarity == 'cosine':
                print(f'Cosine similarity between {feature1} and {feature2} : {cosine_similarity(feature1_values,feature2_values)}')
            elif similarity == 'pearson':
                print(f'pearson similarity between {feature1} and {feature2} : {pearson_similarity(feature1_values,feature2_values)}')
            elif similarity == 'jaccard':
                print(f'Jaccard similarity between {feature1} and {feature2} : {jaccard_similarity(feature1_values,feature2_values)}')
            elif similarity == 'manhattan':
                print(f'Manhattan similarity between {feature1} and {feature2} : {manhattan_similarity(feature1_values,feature2_values)}')
            else:
                print('Invalid similarity funnction')
                continue

        elif option=='3':

            '''
            READING TWO MUSIC ID'S FOR FINDING THE SIMILARITY SCORES BETWEEN THOSE ID'S
            '''

            id1= eval(input('Enter the first music id to find the similarity :'))
            id2= eval(input('Enter the second music id to find the similarity :'))
            similarity = input('Enter the similarity function 1.euclidean 2.cosine 3.pearson 4.jaccard 5.manhattan :').strip().lower()
            if similarity == 'euclidean':
                print(f'Euclidean similarity between {id1} and {id2} : {similarity_between_tracks(music_data,id1,id2,euclidean_similarity)}')
            elif similarity == 'cosine':
                print(f'Cosine similarity between {id1} and {id2} : {similarity_between_tracks(music_data,id1,id2,cosine_similarity)}')
            elif similarity == 'pearson':
                print(f'pearson similarity between {id1} and {id2} : {similarity_between_tracks(music_data,id1,id2,pearson_similarity)}')
            elif similarity == 'jaccard':
                print(f'Jaccard similarity between {id1} and {id2} : {similarity_between_tracks(music_data,id1,id2,jaccard_similarity)}')
            elif similarity == 'manhattan':
                print(f'Manhattan similarity between {id1} and {id2} : {similarity_between_tracks(music_data,id1,id2,manhattan_similarity)}')
            else:
                print('Invalid similarity funnction')
                continue

            
        elif option=='4':
            
            '''
            READING TWO ARTIST ID'S FOR FINDING THE SIMILARITY SCORES BETWEEN THOSE ID'S
            '''

            artist1_id= eval(input('Enter the first artist id to find the similarity :'))
            artist2_id= eval(input('Enter the second artist id to find the similarity :' ))
            similarity = input('Enter the similarity function 1.euclidean 2.cosine 3.pearson 4.jaccard 5.manhattan :').strip().lower()
            if similarity == 'euclidean':
                print(f'Euclidean similarity between {artist1_id} and {artist2_id} : {similarity_between_artists(artist_data,artist1_id,artist2_id,euclidean_similarity)}')
            elif similarity == 'cosine':
                print(f'Cosine similarity between {artist1_id} and {artist2_id} : {similarity_between_artists(artist_data,artist1_id,artist2_id,cosine_similarity)}')
            elif similarity == 'pearson':
                print(f'pearson similarity between {artist1_id} and {artist2_id} : {similarity_between_artists(artist_data,artist1_id,artist2_id,pearson_similarity)}')
            elif similarity == 'jaccard':
                print(f'Jaccard similarity between {artist1_id} and {artist2_id} : {similarity_between_artists(artist_data,artist1_id,artist2_id,jaccard_similarity)}')
            elif similarity == 'manhattan':
                print(f'Manhattan similarity between {artist1_id} and {artist2_id} : {similarity_between_artists(artist_data,artist1_id,artist2_id,manhattan_similarity)}')
            else:
                print('Invalid similarity funnction')
                continue

        elif option=='5' :
            print('Exit the program ')   # PROVIDING THE FLEXIBILITY FOR THE USER TO EXIT THE PROGRAM BY USING THE BREAK STATEMENT
            break
        else:
            print('Invalid input')

if __name__ =='__main__':
    main()                             # CALLING THE MAIN FUNTION, TO START THE EXECUTION PROCESS

            
            

    
