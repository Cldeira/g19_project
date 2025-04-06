# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:48:58 2025

@author: Pedro
"""
from classes.gclass import Gclass

class Book(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_books_id', '_books_title', '_genre', '_publication_year']
    
    des = ['Id', 'Title', 'Genre', 'Publication Year']
    
    def __init__(self, id, title, genre, publication_year):
        super().__init__()
        
        id = Book.get_id(id)
        self._id = id
        self._title = title
        self._genre = genre
        self._publication_year = int(publication_year)
        
        Book.obj[id] = self 
        Book.lst.append(id) 
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value
    
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, value):
        self._genre = value
    
    @property
    def publication_year(self):
        return self._publication_year
    
    @publication_year.setter
    def publication_year(self, value):
        self._publication_year = int(value)
        
        

