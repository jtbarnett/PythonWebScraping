import random
import requests
from bs4 import BeautifulSoup

# IMDB URL - web scrape the top 250 movies on the website and recommend one
URL = 'http://www.imdb.com/chart/top'

def main():
    response = requests.get(URL)

    # Used to parse the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the data we want to record
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    # Used to get the year of the movie
    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        # Last item 
        year = moviesplit[-1]
        return year

    years = [get_year(tag) for tag in movietags]
    # Access attribute 'title'
    actors_list =[tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    # Access attribute 'data-value'
    ratings = [float(tag['data-value']) for tag in ratingtags]

    n_movies = len(titles)

    # Ask the user if they want to continue with movie recommendations
    # If no, then exit the script
    while(True):
        idx = random.randrange(0, n_movies)
        
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

        user_input = input('Do you want another movie (y/[n])? ')
        if user_input != 'y':
            break


if __name__ == '__main__':
    main()