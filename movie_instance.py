# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:20:07 2021

@author: glen_
"""

class Movie:
    
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating
        
my_favorite_movie = Movie(title ="Pride and Prejudice",year= 2005 , language="English",rating= 4.8)
your_favorite_movie = Movie(title ="Titanic", year=1997, language="English",rating= 4.6)

print("My Favorite Movie:")
print(my_favorite_movie.title)
print(my_favorite_movie.year)
print(my_favorite_movie.language)
print(my_favorite_movie.rating)

print("Your Favorite Movie:")
print(your_favorite_movie.title)
print(your_favorite_movie.year)
print(your_favorite_movie.language)
print(your_favorite_movie.rating)


