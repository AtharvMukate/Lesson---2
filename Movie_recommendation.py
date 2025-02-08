import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.matrix.pearwise import cosine_similarity
from textblob import textblob
from colorama import init, Fore
import time
import sys
init(autoreset = True)
def load_data(file_path = '/Users/atharvmukate/Desktop/Codingal/Lesson - 2 /imdb_top_1000 (1).csv' ):
    try:
        df = pd.read_csv(file_path)
        df['combined_feature'] = df['Genre'].fillna('')+''+df['overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED+f"error: the file {file_path} was not found")
        exit()

movies_df = load_data()
tfidf = TfidfVectorizer(stop_words = 'English')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_feature'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
def list_Genres(df):
    return sorted(set(genre.strip()for sublist in df['Genre'].dropna().str.split(',')for genre in sublist))
genres = list_genres(movies_df)
def recommened_movies(genre = None,rating = none,top_n = 5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre,case = False, na = False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating']>= rating]
    filtered_df = filtered_df.sample(frac = 1).reset_index(drop = True)
    recommenedations = []
    for idx, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview.sentiment.polarity)
        if (mood and ((TextBlob(mood).sentiment.polarity <0 and polarity >0) or polarity >=0)) or not mood:
            recommenedations.append(row['Series_Title'], polarity)
        if len(recommenedations) == top_n:
            break
    return recommenedations if recommenedations else 'no suitable movie recommendations found'

def display_recommendation(recs, name):
    print(Fore.YELLOW+f"\n ?? AI - Analyzed movie recommendation for{name}:")
    for idx, (title,polarity) in enumerate(recs, 1):
        sentiment = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'
        print(f'{Fore.CYAN}{idx}.{title}(polarity:{polarity:.2f}, {sentiment})')

def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW+'.',end = '', flush = True)
        time.sleep(0.5)

def handle_ai(name):
    print(Fore.BLUE+'\n Lets find a perfect movie for you!')
    print(Fore.GREEN+'Available genres:', end = '')
    for idx, genre in enumerate(genres,1):
        print(f"{Fore.CYAN}{idx}.{genre}")
    print()
    while True:
        genre_input = input(Fore.YELLOW+'Enter genre number or name: ').strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input)-1]
            break
        elif genre_input.title()in genres:
            genre = genre_input.title()
            break
        print(Fore.RED+"Invalid input, please try again")
    mood = input(Foree.YELLOW+"How do you feel Today?").strip()
    print(Fore.BLUE+"\n analyzing mood", end = '', flush = True)
    processing_animation()
    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = 'positive' if polarity >0 else ' negative' if polarity <0 else 'neutral'
    print(f'\n {Fore.GREEN} Your mood is {mood_desc}(polarity:{polarity:.2f})')
    while True:
        rating_input = input(Fore.YELLOW+"Enter minimum IMDB rating (7.6 - 9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED+"Rating out of range please try again")
        except ValueError:
            print(Fore.RED+"Invalid input, please try again")
    print(Fore.BLUE+"\n AI is finding the best movie for you", end = '', flush = True)
    processing_animation()
    recs = recommened_movies(genre = genre, rating = rating, mood = mood, top_n = 5)
    if isinstance(recs, str):
        print(Fore.RED+recs+'\n')
    else:
        display_recommendation(recs, name)
    while True:
        rating_input = input(Fore.YELLOW+" Enter minimum IMBD rating :").strip().lower()
        if action == 'no':
            print(Fore.BLUE+f"Enjoy your movie picks, {name}!")
            break
        elif action == 'yes':
            recs = recommened_movies(genre = genre, rating = rating, mood = mood, top_n = 5)
            if isinstance(recs, str):
                print(Fore.RED+recs+'\n')

            else:
                display_recommendation(recs, name)
        else:
            print(Fore.RED+"Invalid choice, please try again")
def main():
    print(Fore.BLUE+"Welcome to Movie Recommendation AI")
    name = input(Fore.YELLOW+"Enter your name: ").strip().title()
    print(Fore.GREEN+f"Hello, {name}!")
    handle_ai(name)

if __name__ == '__main__':
    main()