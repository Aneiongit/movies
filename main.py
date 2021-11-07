import random
from datetime import date


class Movie:
    def __init__(self, title, release_date, genre, number_of_views):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.number_of_views = number_of_views

    def __str__(self):
        return f'"{self.title} ({self.release_date})"'

    def play(self):
        self.number_of_views += 1


class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'"{self.title} {self.season_number}{self.episode_number}"'

    def play(self):
        self.number_of_views += 1


class Blockbuster:

    def __init__(self, movies_list=None):
        if movies_list is None:
            movies_list = list()
        self.movies_list = movies_list or []

    def all_movies(self):
        print("\n".join([str(entry) for entry in self.movies_list]))

    def get_all(self):
        return self.movies_list.copy()

    def get_movies(self):
        return [line for line in self.movies_list if not isinstance(line, Series)]

    def get_series(self):
        return [line for line in self.movies_list if isinstance(line, Series)]

    def search(self):
        title = input("Podaj tytuł: ")
        watch_list = [line.title for line in self.movies_list if line.title == title]
        print(watch_list)

    def generate_views(self):
        for i in range(10):
            movie = random.choice(self.movies_list)
            movie.number_of_views += random.randint(0, 100)
        return movie

    def top_titles(self):
        sorted_top_titles = sorted(self.movies_list, key=lambda best_movies: best_movies.number_of_views, reverse=True)
        sorted_top_movies_titles = [line.title for line in sorted_top_titles]
        best_movies = sorted_top_movies_titles[0:3]
        today = date.today()
        today_date = today.strftime("%d.%m.%Y")
        print(f"Najpopularniejsze filmy i seriale dnia {today_date}")
        print(best_movies)


if __name__ == '__main__':

    movieshelf = Blockbuster([
        Movie(title='The Shawshank Redemption', release_date=1994, genre='Drama', number_of_views=0),
        Movie(title='2001:A space Odyssey', release_date=1968, genre='Science fiction', number_of_views=0),
        Movie(title='The Godfather', release_date=1972, genre='Thriller', number_of_views=0),
        Movie(title='Citizen Kane', release_date=1941, genre='Drama', number_of_views=0),
        Movie(title='Raiders of the Lost Ark', release_date=1981, genre='Action and adventure', number_of_views=0),
        Movie(title='Seven Samurai', release_date=1954, genre='Action and adventure', number_of_views=0),
        Movie(title='Goodfellas', release_date=1990, genre='Thriller', number_of_views=0),
        Movie(title='City Lights', release_date=1931, genre='Comedy', number_of_views=0),
        Movie(title='Alien', release_date=1979, genre='Science fiction', number_of_views=0),
        Series(title='House', release_date=2004, genre='Drama', season_number='S01', episode_number='E05',
               number_of_views=0),
        Series(title='Sons of Anarchy', release_date=2008, genre='Crime', season_number='S01', episode_number='E02',
               number_of_views=0),
        Series(title='Sons of Anarchy', release_date=2008, genre='Crime', season_number='S01', episode_number='E03',
               number_of_views=0),
        Series(title='Sons of Anarchy', release_date=2008, genre='Crime', season_number='S01', episode_number='E04',
               number_of_views=0),
        Series(title='The Sopranos', release_date=1999, genre='Crime', season_number='S01', episode_number='E01',
               number_of_views=0),
        Series(title='The Sopranos', release_date=1999, genre='Crime', season_number='S01', episode_number='E02',
               number_of_views=0),
        Series(title='The Sopranos', release_date=1999, genre='Crime', season_number='S01', episode_number='E03',
               number_of_views=0),
        Series(title='The Sopranos', release_date=1999, genre='Crime', season_number='S01', episode_number='E04',
               number_of_views=0),
        Series(title='The Sopranos', release_date=1999, genre='Crime', season_number='S01', episode_number='E05',
               number_of_views=0)])

    movieshelf.all_movies()
    movieshelf.generate_views()
    movieshelf.top_titles()
